# Image quality follow-up

Replaced all ten low-resolution product derivatives with cutouts using the matching original JPG pixels from Downloads. Original photos are 2000×2000 (Chase 2001×2001); native garment cutouts span 765–815 pixels, compared with approximately 190 pixels in the background-removal previews. Output canvases are 1000×1000 at the existing 87.2% normalized occupancy.

The transparent previews provide a silhouette guide only. OpenCV refines that guide against the full-resolution edges. Mild output sharpening preserves the photographed artwork. No generated detail was added.

Visual inspection: all five back views on chalk and dark fields, desktop and portrait mobile detail screenshots, and a same-size before/after comparison. Original lettering, white fabric and garment contours remain intact. Existing design and page source required no changes.

Automated browser verification: all ten 1000×1000 images load; no script errors or horizontal overflow at 1440×900, 390×844, 360×640 and 844×390. Previous/next, product details, front/back, business drawer, parallax, click after dragging and mobile pause pass. Raster provenance scan: 12 rasters, zero missing.

Original index.html SHA256 remains 41234d92add801689f8571b25264e31b682c65b44ea28cba0cebf4a899103e54.

Evidence: checks.json, image-quality-comparison.png, high-resolution-cutouts.jpg and current viewport screenshots in this directory. Before assets and captures are retained in image-quality-before.
