from pathlib import Path
from PIL import Image, ImageFilter
from PIL.PngImagePlugin import PngInfo
import cv2
import numpy as np
import json
import subprocess

source = Path('C:/Users/Habib/Downloads')
target = Path('assets/beyond-doubt')
target.mkdir(parents=True, exist_ok=True)
products = {
    'wave': '885150895_1811498543086760_5402289809886314320_n-removebg-preview.png',
    'sunset': '885359889_985341477384161_6781199192129791877_n-removebg-preview.png',
    'chase': '887578877_1066799613081901_5662893024735941349_n-removebg-preview.png',
    'electric': '884529948_1434153752242046_980529619281778697_n-removebg-preview.png',
    'race': '881185482_1804739770727460_6043172799559884311_n-removebg-preview.png',
}
manifest = {}


def extract_original(original, preview, side):
    """Use original photo pixels; the preview supplies only a silhouette guide."""
    width, height = original.size
    guide = preview.getchannel('A').resize((width, height), Image.Resampling.LANCZOS)
    # Refine the low-resolution guide along the actual full-resolution edges.
    seed = (np.asarray(guide) >= 128).astype(np.uint8)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15))
    interior = cv2.erode(seed, kernel)
    exterior = cv2.dilate(seed, kernel)
    labels = np.full(seed.shape, cv2.GC_BGD, dtype=np.uint8)
    labels[exterior != 0] = cv2.GC_PR_BGD
    labels[seed != 0] = cv2.GC_PR_FGD
    labels[interior != 0] = cv2.GC_FGD
    # Restrict the region to the garments; the photo's brand/caption are excluded.
    bounds = Image.fromarray(exterior * 255).getbbox()
    x0, y0, x1, y1 = bounds
    pixels = np.asarray(original)[y0:y1, x0:x1].copy()
    local_labels = labels[y0:y1, x0:x1].copy()
    cv2.grabCut(cv2.cvtColor(pixels, cv2.COLOR_RGB2BGR), local_labels, None,
                np.zeros((1, 65), np.float64), np.zeros((1, 65), np.float64),
                3, cv2.GC_INIT_WITH_MASK)
    matte = np.where((local_labels == cv2.GC_FGD) | (local_labels == cv2.GC_PR_FGD), 255, 0).astype(np.uint8)
    # Keep original garment contours, with subpixel antialiasing at their edges.
    matte = cv2.GaussianBlur(matte, (3, 3), .55)
    rgba = Image.fromarray(pixels).convert('RGBA')
    rgba.putalpha(Image.fromarray(matte))
    full = Image.new('RGBA', original.size)
    full.alpha_composite(rgba, (x0, y0))
    midpoint = width // 2
    box = (0, 0, midpoint, height) if side == 'front' else (midpoint, 0, width, height)
    cutout = full.crop(box)
    cutout = cutout.crop(cutout.getbbox())
    return cutout


for name, filename in products.items():
    original_filename = filename.replace('-removebg-preview.png', '.jpg')
    original = Image.open(source / original_filename).convert('RGB')
    preview = Image.open(source / filename).convert('RGBA')
    for side in ['front', 'back']:
        image = extract_original(original, preview, side)
        native_size = image.size
        canvas = Image.new('RGBA', (1000, 1000))
        # Retain the exact 87.2% product occupancy used by the existing layout.
        size = min(872 / image.width, 872 / image.height)
        image = image.resize((round(image.width * size), round(image.height * size)), Image.Resampling.LANCZOS)
        alpha = image.getchannel('A')
        image = image.convert('RGB').filter(ImageFilter.UnsharpMask(radius=.65, percent=65, threshold=3)).convert('RGBA')
        image.putalpha(alpha)
        canvas.alpha_composite(image, ((1000-image.width)//2, (1000-image.height)//2))
        metadata = PngInfo()
        operation = f'extract {side} from full-resolution original, refine preview alpha guide against original edges, normalize 1000px canvas, mild output sharpening'
        origin = f'User supplied: {source / original_filename}; alpha guide: {source / filename}; {operation}. No generated artwork.'
        metadata.add_text('Origin', origin)
        metadata.add_text('impeccable:provenance', origin)
        canvas.save(target / f'{name}-{side}.png', pnginfo=metadata, optimize=True)
        manifest[f'{name}-{side}.png'] = {
            'source': original_filename, 'alpha_guide': filename,
            'source_dimensions': list(original.size), 'native_cutout_dimensions': list(native_size),
            'output_dimensions': list(canvas.size), 'operation': operation,
        }

logo = Image.open(source / 'Beyond-Doubt.jpg').convert('RGB')
alpha = logo.convert('L').point(lambda value: max(0, min(255, (value-15)*255//220)))
logo_white = Image.new('RGBA', logo.size, (255, 255, 255, 0))
logo_white.putalpha(alpha)
logo_white = logo_white.crop(alpha.getbbox())
metadata = PngInfo()
origin = f'User supplied: {source / "Beyond-Doubt.jpg"}; trimmed blank background and extracted white wordmark alpha.'
metadata.add_text('Origin', origin)
metadata.add_text('impeccable:provenance', origin)
logo_white.save(target / 'wordmark.png', pnginfo=metadata, optimize=True)
manifest['wordmark.png'] = {'source': 'Beyond-Doubt.jpg', 'operation': 'trim background, white wordmark alpha'}
favicon = logo_white.copy()
favicon.thumbnail((300, 80), Image.Resampling.LANCZOS)
favicon.save(target / 'favicon.png', pnginfo=metadata)
manifest['favicon.png'] = {'source': 'Beyond-Doubt.jpg', 'operation': 'wordmark favicon'}
manifest['duplicate'] = {'source': '887578877_1066799613081901_5662893024735941349_n-removebg-preview (1).png', 'duplicate_of': products['chase']}
(target / 'sources.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
launcher = Path('C:/Users/Habib/.agents/skills/impeccable/scripts/impeccable.cmd')
if launcher.exists():
    for filename, entry in manifest.items():
        if filename == 'duplicate':
            continue
        guide_note = f' Alpha guide: {source / entry["alpha_guide"]}.' if 'alpha_guide' in entry else ''
        origin = f'Origin: User supplied {source / entry["source"]}.{guide_note} Operation: {entry["operation"]}. No generated artwork.'
        subprocess.run([str(launcher), 'embed-prompt', str(target / filename), '--prompt', origin], check=True)
print(f'Prepared {len(products)} actual designs with front/back views and the supplied wordmark.')
