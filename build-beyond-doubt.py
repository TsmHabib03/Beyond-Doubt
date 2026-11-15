from pathlib import Path
import re

html = Path('index.html').read_text(encoding='utf-8')
html = html.replace('BUNTO° — Soft things for small people', 'Beyond Doubt — Apparel & Clothing')
html = html.replace('Premium organic-cotton basics for ages 1–6: rompers, dungarees, tees, cardigans and hats in soft peach, pink, sage and butter.', 'Explore Beyond Doubt jerseys, front and back. Shop on Shopee or Lazada, and find our North Fairview, Quezon City contact details.')
html = html.replace('--bg: #F9F2E9', '--bg: #EDEDE8').replace('--ghost: #F5E6D9', '--ghost: #DCDCD5').replace('--ink: #3E3A3C', '--ink: #21221F').replace('--muted: #716D71', '--muted: #60615A').replace('--line: #E6D9D2', '--line: #CDCEC6').replace('--dot: #CFC6C2', '--dot: #B8BAB1')
html = re.sub(r'      --sheet:.*\n', '', html)
html = html.replace('  <script>document.documentElement', '  <link rel="icon" type="image/png" href="assets/beyond-doubt/favicon.png">\n  <meta name="theme-color" content="#EDEDE8">\n  <meta property="og:title" content="Beyond Doubt — Apparel & Clothing">\n  <meta property="og:description" content="Explore the jersey collection. North Fairview, Quezon City.">\n  <script>document.documentElement')
css = '''
    /* Beyond Doubt: retain the original stage and orbit; use the supplied identity. */
    body { color-scheme: light; }
    ::selection { background: var(--ink); color: var(--bg); }
    :focus-visible { outline: 2px solid var(--ink); outline-offset: 5px; }
    .logo { width: clamp(155px, calc(220 * var(--n)), 280px); min-height: 44px; display: flex; align-items: center; top: calc(25 * var(--n)); }
    .logo img { width: 100%; height: auto; filter: brightness(0); }
    .tagline { top: calc(35 * var(--n)); letter-spacing: .2em; }
    .nav { top: calc(25 * var(--n)); gap: 22px; }
    .menu { border: 0; background: none; min-height: 44px; font-size: 10px; letter-spacing: .18em; }
    .shop-link { min-height: 44px; display: flex; align-items: center; gap: 16px; border-bottom: 1px solid var(--ink); font-size: 10px; letter-spacing: .18em; transition: opacity .2s ease; }
    .shop-link svg { width: 14px; height: 14px; }
    .shop-link:hover { opacity: .6; }
    .left-label { letter-spacing: .2em; }
    .right-label { letter-spacing: .18em; }
    .right-label span { display: block; color: var(--muted); font-size: 9px; margin-top: 4px; }
    .vertical-label { letter-spacing: .25em; }
    .ghost { top: calc(151 * var(--u)); padding: 0 calc(100 * var(--u)); line-height: 0; }
    .ghost img { width: 100%; height: auto; filter: brightness(0); opacity: .055; }
    .shadow { background: radial-gradient(ellipse, rgba(38,40,32,.14), rgba(38,40,32,.045) 55%, transparent 100%); }
    .art, .art2 { background-size: contain; background-position: center; filter: drop-shadow(0 12px 10px rgba(24,26,20,.12)); }
    .item { border: 0; background: transparent; }
    .close { min-width: 44px; min-height: 44px; background: var(--bg); }
    .panel { top: calc(300 * var(--u)); width: calc(400 * var(--u)); }
    .product-name { --order: 0; font-size: calc(40 * var(--u)); font-weight: 600; margin: 0 0 calc(15 * var(--u)); text-wrap: balance; }
    .category { --order: 1; letter-spacing: .18em; margin-bottom: 18px; }
    .description { --order: 2; }
    .view-switch { --order: 3; display: flex; gap: 6px; margin: 25px 0; width: fit-content; border-bottom: 1px solid var(--line); }
    .view-button { min-height: 44px; padding: 0 17px; background: none; border: 0; border-bottom: 2px solid transparent; color: var(--muted); font-size: 10px; letter-spacing: .15em; text-transform: uppercase; transition: color .2s ease, border-color .2s ease; }
    .view-button[aria-checked="true"] { color: var(--ink); border-bottom-color: var(--ink); }
    .view-button:hover { color: var(--ink); }
    .product-shops { --order: 4; display: flex; flex-wrap: wrap; gap: 12px; align-items: center; }
    .store-button { min-height: 44px; display: inline-flex; align-items: center; justify-content: center; gap: 15px; padding: 0 18px; background: var(--ink); color: var(--bg); border: 1px solid var(--ink); font-size: 10px; letter-spacing: .12em; transition: background .2s ease, color .2s ease; }
    .store-button svg { width: 13px; height: 13px; }
    .store-button:hover { background: var(--bg); color: var(--ink); }
    .store-button.secondary { color: var(--ink); background: transparent; border-color: var(--line); }
    .store-button.secondary:hover { border-color: var(--ink); }
    .stock-note { --order: 5; color: var(--muted); font-size: 11px; line-height: 1.5; margin: 15px 0 0; }
    .index-window { font-variant-numeric: tabular-nums; }
    .index-labels { letter-spacing: .2em; }
    .scroll-hint { gap: 12px; letter-spacing: .2em; }
    .scroll-hint > svg { display: none; }
    .explore-controls { right: calc(40 * var(--n)); bottom: calc(45 * var(--n)); display: flex; gap: 9px; }
    .explore-controls .round { width: 44px; height: 44px; }
    .explore-controls svg { width: 15px; height: 15px; }
    .motion-toggle { border: 0; background: none; color: var(--muted); font-size: 9px; letter-spacing: .15em; padding: 0 12px; min-height: 44px; }
    .detail .explore-controls, .detail .scroll-hint { opacity: 0; pointer-events: none; visibility: hidden; }
    .skip-link { position: fixed; top: 10px; left: 10px; z-index: 1500; background: var(--ink); color: var(--bg); padding: 12px 18px; transform: translateY(-180%); }
    .skip-link:focus { transform: none; }
    .sr-only { position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip-path: inset(50%); white-space: nowrap; border: 0; }
    .business-drawer { position: fixed; inset: 0 0 0 auto; max-width: 530px; width: 100%; height: 100dvh; max-height: none; padding: 0; margin: 0; border: 0; background: var(--bg); color: var(--ink); box-shadow: -20px 0 80px rgba(30,32,25,.13); overflow-y: auto; scrollbar-color: var(--muted) var(--bg); scrollbar-width: thin; }
    .business-drawer::backdrop { background: rgba(28,30,25,.3); }
    .drawer-inner { padding: 35px 44px 50px; }
    .drawer-head { display: flex; align-items: center; justify-content: space-between; margin-bottom: 45px; }
    .drawer-head img { width: 190px; filter: brightness(0); }
    .drawer-close { width: 44px; height: 44px; }
    .drawer-close svg { width: 15px; height: 15px; }
    .business-drawer h2 { font-size: 34px; font-weight: 500; letter-spacing: -.03em; margin: 0 0 16px; }
    .business-drawer p { color: var(--muted); font-size: 14px; line-height: 1.65; }
    .verified { display: flex; align-items: center; gap: 8px; font-size: 12px; }
    .verified svg { width: 17px; height: 17px; }
    .business-drawer h3 { font-size: 12px; font-weight: 600; letter-spacing: .13em; text-transform: uppercase; margin: 34px 0 12px; }
    .store-list { display: flex; flex-direction: column; }
    .store-list a { display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid var(--line); padding: 17px 0; min-height: 54px; font-size: 18px; transition: padding .2s ease; }
    .store-list a:hover { padding-left: 8px; }
    .store-list svg { width: 16px; height: 16px; }
    .business-drawer address { font-size: 14px; line-height: 1.7; font-style: normal; color: var(--muted); }
    .contact-link { display: inline-flex; align-items: center; min-height: 44px; border-bottom: 1px solid var(--ink); font-size: 13px; margin-top: 8px; }
    .profile-note { border-top: 1px solid var(--line); margin-top: 30px; padding-top: 15px; }
    .profile-note p { font-size: 11px; }
    .asset-warning { position: absolute; z-index: 450; left: 50%; top: 90px; transform: translateX(-50%); padding: 12px 18px; background: var(--ink); color: var(--bg); font-size: 12px; max-width: 90%; text-align: center; }
    @media (max-width: 820px) and (min-height: 521px) {
      .logo { width: 160px; top: 17px; left: 20px; }
      .nav { top: 17px; right: 20px; gap: 14px; }
      .menu { display: block; font-size: 9px; }
      .shop-link { font-size: 9px; gap: 8px; }
      .shop-link svg { width: 11px; }
      .stage { top: 43%; }
      .ghost { top: calc(145 * var(--u)); padding: 0 calc(455 * var(--u)); }
      .panel { left: calc(50% - 260 * var(--u)); top: calc(548 * var(--u)); width: calc(520 * var(--u)); }
      .product-name { font-size: 28px; margin-bottom: 8px; }
      .category { font-size: 9px; margin-bottom: 10px; }
      .description { font-size: 12px; }
      .view-switch { margin: 10px 0 13px; }
      .stock-note { font-size: 10px; margin-top: 10px; }
      .product-shops { gap: 8px; }
      .store-button { font-size: 9px; padding: 0 14px; }
      .index { bottom: 28px; }
      .index-labels { min-width: 12em; font-size: 8px; }
      .scroll-hint { bottom: 105px; right: auto; left: 50%; transform: translateX(-50%); }
      .scroll-hint span { display: block; font-size: 8px; }
      .explore-controls { right: 20px; bottom: 22px; gap: 5px; }
      .motion-toggle { padding: 0 5px; font-size: 8px; }
      .explore-controls .round { width: 44px; height: 44px; }
      .drawer-inner { padding: 25px 25px 40px; }
    }
    @media (max-width: 380px) { .logo { width: 135px; } .nav { gap: 9px; } .motion-toggle { display: none; } }
    @media (max-height: 520px) {
      .tagline, .left-label, .right-label { display: none; }
      .logo { width: 160px; top: 12px; left: 25px; }
      .nav { top: 10px; right: 25px; }
      .panel { left: calc(900 * var(--u)); top: calc(210 * var(--u)); width: calc(500 * var(--u)); }
      .product-name { font-size: 23px; margin-bottom: 8px; }
      .category { font-size: 9px; margin-bottom: 9px; }
      .description { font-size: 11px; }
      .view-switch { margin: 6px 0; }
      .stock-note { font-size: 9px; margin-top: 7px; }
      .index { bottom: 20px; }
      .scroll-hint { bottom: 30px; }
      .explore-controls { bottom: 15px; }
    }
    @media (prefers-reduced-motion: reduce) { *, *::before, *::after { scroll-behavior: auto !important; } .business-drawer, .store-list a, .store-button, .view-button { transition: none; } }
'''
html = html.replace('  </style>', css+'  </style>')
start = html.index('  <main class="hero"')
end = html.index('  <script>\n    (() =>', start)
arrow = '<svg viewBox="0 0 16 16" stroke-width="1.3" aria-hidden="true"><path d="M3 13 13 3M3 3h10v10"/></svg>'
close_icon = '<svg viewBox="0 0 16 16" stroke-width="1.3" aria-hidden="true"><path d="m4 4 8 8M12 4l-8 8"/></svg>'
html = html[:start]+f'''  <a class="skip-link" href="#collection">Skip to collection</a>
  <main class="hero" aria-label="Beyond Doubt apparel collection">
    <a class="logo chrome rv" href="index-beyond-doubt.html" aria-label="Beyond Doubt home"><img src="assets/beyond-doubt/wordmark.png" alt="Beyond Doubt" width="1480" height="282"></a>
    <div class="tagline chrome caps rv">CHASE WHAT’S AHEAD.<br>BEYOND DOUBT.</div>
    <nav class="nav chrome rv" aria-label="Main">
      <button class="menu caps" type="button" aria-haspopup="dialog" aria-controls="business-drawer">ABOUT</button>
      <a class="shop-link caps" href="https://shopee.ph/beyond.doubt" target="_blank" rel="noopener noreferrer">SHOP {arrow}</a>
    </nav>
    <div class="left-label chrome caps rv">THE JERSEYS — 5 DESIGNS</div>
    <div class="right-label chrome caps rv">BEYOND DOUBT<span>NORTH FAIRVIEW, QC</span></div>
    <div class="vertical-label chrome caps rv">APPAREL &amp; CLOTHING · NORTH FAIRVIEW, QC</div>
    <div class="stage" id="collection" role="region" aria-label="Interactive jersey collection" tabindex="-1" aria-describedby="collection-help">
      <h1 class="sr-only">Beyond Doubt jersey collection</h1>
      <div class="ghost rv" aria-hidden="true"><img src="assets/beyond-doubt/wordmark.png" alt="" width="1480" height="282"></div>
      <div class="shadow rv" aria-hidden="true"></div>
      <div class="dots rv" aria-hidden="true"><i class="dot active"></i><i class="dot"></i><i class="dot"></i><i class="dot"></i><i class="dot"></i></div>
      <button class="close round" type="button" aria-label="Back to collection" tabindex="-1">{close_icon}</button>
      <section class="panel" aria-labelledby="product-name" aria-hidden="true" inert>
        <h2 class="product-name" id="product-name"></h2>
        <div class="category caps"></div>
        <p class="description"></p>
        <div class="view-switch" role="radiogroup" aria-label="Product view">
          <button class="view-button" type="button" role="radio" aria-label="Front view" aria-checked="true">Front</button>
          <button class="view-button" type="button" role="radio" aria-label="Back view" aria-checked="false" tabindex="-1">Back</button>
        </div>
        <div class="product-shops">
          <a class="store-button" href="https://shopee.ph/beyond.doubt" target="_blank" rel="noopener noreferrer">SHOP SHOPEE {arrow}</a>
          <a class="store-button secondary" href="https://www.lazada.com.ph/shop/beyond-doubt" target="_blank" rel="noopener noreferrer">LAZADA {arrow}</a>
        </div>
        <p class="stock-note">Check current prices, sizes &amp; availability in our shops.</p>
      </section>
    </div>
    <div class="index chrome rv">
      <div class="index-window"><span class="index-number">01</span></div>
      <div class="index-bar" aria-hidden="true"></div>
      <div class="index-labels caps">
        <div class="index-label collection-label"><span class="index-kind">CHASE</span><br>JERSEY COLLECTION</div>
        <div class="index-label choose-label">FRONT &amp; BACK<br>EXPLORE THE DETAILS</div>
      </div>
    </div>
    <div class="scroll-hint chrome caps rv"><span id="collection-help">DRAG OR SCROLL TO EXPLORE</span></div>
    <div class="explore-controls chrome rv" aria-label="Collection controls">
      <button class="motion-toggle" type="button" aria-label="Pause automatic rotation" aria-pressed="false">PAUSE</button>
      <button class="previous round" type="button" aria-label="Previous jersey"><svg viewBox="0 0 16 16" stroke-width="1.3" aria-hidden="true"><path d="M13 8H3m5-5L3 8l5 5"/></svg></button>
      <button class="next round" type="button" aria-label="Next jersey"><svg viewBox="0 0 16 16" stroke-width="1.3" aria-hidden="true"><path d="M3 8h10M8 3l5 5-5 5"/></svg></button>
    </div>
    <p class="asset-warning" role="status" hidden>Some product images could not load. Reload the page or browse the collection on Shopee.</p>
    <p class="sr-only" id="collection-status" role="status" aria-live="polite"></p>
  </main>
  <dialog class="business-drawer" id="business-drawer" aria-labelledby="business-title">
    <div class="drawer-inner">
      <div class="drawer-head"><img src="assets/beyond-doubt/wordmark.png" alt="Beyond Doubt" width="1480" height="282"><button class="drawer-close round" type="button" aria-label="Close business information">{close_icon}</button></div>
      <h2 id="business-title">Beyond Doubt.</h2>
      <p>Apparel &amp; clothing.<br>Find your next jersey. Chase what’s ahead.</p>
      <div class="verified"><svg viewBox="0 0 20 20" stroke-width="1.4" aria-hidden="true"><path d="m10 1 2.2 2 3-.1.6 2.9L18 8l-1 2.8.4 3-2.7 1.2-1.5 2.5-2.9-.7-2.8 1-1.8-2.4-2.8-.9.1-3L1 9l1.9-2.3.3-3 3-.3Z"/><path d="m6 9.5 2.7 2.7 4.8-4.8"/></svg>Meta Verified on Facebook</div>
      <p>90% recommend · 5 Facebook reviews</p>
      <h3>Find us online</h3>
      <div class="store-list">
        <a href="https://shopee.ph/beyond.doubt" target="_blank" rel="noopener noreferrer">Shopee {arrow}</a>
        <a href="https://www.lazada.com.ph/shop/beyond-doubt" target="_blank" rel="noopener noreferrer">Lazada {arrow}</a>
        <a href="https://www.tiktok.com/@beyonddoubt.clothing" target="_blank" rel="noopener noreferrer">TikTok {arrow}</a>
      </div>
      <h3>North Fairview, Quezon City</h3>
      <address>Blk 27 Lot 12 Pechayan Kanan<br>Namasape HOA, Commonwealth Ave.<br>North Fairview QC, Quezon City<br>Philippines, 1121</address>
      <a class="contact-link" href="https://www.google.com/maps/search/?api=1&amp;query=Blk%2027%20Lot%2012%20Pechayan%20Kanan%20Namasape%20HOA%20North%20Fairview%20Quezon%20City" target="_blank" rel="noopener noreferrer">View location on Google Maps</a>
      <h3>Get in touch</h3>
      <a class="contact-link" href="tel:+639055079634">0905 507 9634</a>
      <p>Find “Beyond Doubt” on Messenger.<br>Call to confirm opening hours before visiting.</p>
      <div class="profile-note"><p>Facebook profile created July 26, 2023.<br>Verification and recommendations are from the supplied Facebook profile information.</p></div>
    </div>
  </dialog>
  <noscript><style>.hero {{display:none}} html,body {{overflow:auto}} .business-drawer {{display:block; position:relative; height:auto; margin:auto; box-shadow:none}} .drawer-close {{display:none}}</style><p style="padding:20px;text-align:center">Enable JavaScript to explore the interactive collection. Our shops and contact information are below.</p></noscript>
'''+html[end:]
# Reuse the original orbit, inertia, zoom and reveal implementation; adapt its content model.
html = html.replace("const swatches = [...document.querySelectorAll('.swatch')];", "const swatches = [...document.querySelectorAll('.view-button')];")
html = re.sub(r"      const add =.*\n      const bag =.*\n      const badge =.*\n", "      const shopLinks = [...document.querySelectorAll('.product-shops a')];\n      const drawer = document.querySelector('.business-drawer');\n      const menu = document.querySelector('.menu');\n      const status = document.querySelector('#collection-status');\n      const motionToggle = document.querySelector('.motion-toggle');\n", html)
start = html.index("      const colours =")
end = html.index("      const clamp =",start)
html = html[:start]+'''      const colours = ['Front', 'Back'];
      const products = [
        { id: 'chase', kind: 'Chase', category: 'BLACK & WHITE · LONG-SLEEVE JERSEY', description: 'Checkerboard graphics with the Beyond Doubt wordmark. Turn it around for “Chase What’s Ahead.”' },
        { id: 'electric', kind: 'Electric', category: 'CYAN & MAGENTA · LONG-SLEEVE JERSEY', description: 'A white base with bold cyan and magenta graphics. The front carries the wordmark; the back features the geometric BD emblem.' },
        { id: 'wave', kind: 'Wave', category: 'BLACK & WHITE · LONG-SLEEVE JERSEY', description: 'Monochrome wave artwork across the sleeves and hem, with a larger circular graphic on the back.' },
        { id: 'sunset', kind: 'Sunset', category: 'GRAY & ORANGE · LONG-SLEEVE JERSEY', description: 'A sunset graphic on gray, with warm color accents along the sleeves and a geometric emblem on the back.' },
        { id: 'race', kind: 'Race', category: 'BLACK & WHITE · LONG-SLEEVE JERSEY', description: 'Checkerboard sleeve details and a bold front wordmark. The back pairs Beyond Doubt lettering with crossed racing flags.' }
      ];
      const CX = 718, CY = 418, R = 411, DROP = 110, S0 = .97, TILT = 9;
      const N = products.length, STEP = 2 * Math.PI / N, OMEGA = STEP / 7;
'''+html[end:]
html = html.replace("const crop = (col, row) => `${col * 25}% ${row * 33.333}%`;", "const crop = (col, row) => `url(\"assets/beyond-doubt/${products[col].id}-${row === 0 ? 'front' : 'back'}.png\")`;")
html = html.replace('let bagCount = 0, addedTimer = 0, hovered = null;', 'let hovered = null, paused = motion.matches, manualUntil = 0, navigation = null;\n      let pointer = { x: 0, y: 0 }, parallax = { x: 0, y: 0 };\n      let frontIndex = 0, previousFront = -1;')
html = html.replace("[[1,0], [2,1], [0,2], [3,3], [4,1], [3,2]].map(([col, row], i)", "products.map((product, i)")
html = html.replace("const el = document.createElement('div');\n        el.className = 'item';", "const col = i, row = 0;\n        const el = document.createElement('button');\n        el.type = 'button'; el.className = 'item';")
html = html.replace('backgroundPosition', 'backgroundImage')
html = html.replace("setIndex(1, 'Romper')", 'setIndex(frontIndex + 1, products[frontIndex].kind)')
html = html.replace("return phone.matches ? { x: 716, y: 300, scale: .86 } : { x: 470, y: 425, scale: 1.12 };", "return phone.matches ? { x: 716, y: 290, scale: .79 } : { x: 470, y: 425, scale: 1.12 };")
html = html.replace('panel.inert = false;', "document.querySelector('.explore-controls').inert = true; panel.inert = false;")
html = html.replace("hero.classList.remove('detail'); panel.inert", "hero.classList.remove('detail'); document.querySelector('.explore-controls').inert = false; panel.inert")
html = html.replace("document.querySelector('.menu').addEventListener('click', event => event.preventDefault());", '''menu.addEventListener('click', () => drawer.showModal());
      document.querySelector('.drawer-close').addEventListener('click', () => drawer.close());
      drawer.addEventListener('click', event => { if (event.target === drawer && event.clientX < drawer.getBoundingClientRect().left) drawer.close(); });
      drawer.addEventListener('close', () => menu.focus({ preventScroll: true }));
      function setPaused(value) {
        paused = value; motionToggle.textContent = paused ? 'PLAY' : 'PAUSE';
        motionToggle.setAttribute('aria-label', paused ? 'Play automatic rotation' : 'Pause automatic rotation');
        motionToggle.setAttribute('aria-pressed', String(paused));
      }
      setPaused(paused);
      motionToggle.addEventListener('click', () => setPaused(!paused));
      function step(direction) {
        if (selected || drawer.open || drag) return;
        const index = (frontIndex + direction + N) % N;
        const turns = Math.round((base + index * STEP) / (2 * Math.PI));
        const destination = -index * STEP + turns * 2 * Math.PI;
        navigation = { from: base, to: destination, start: performance.now() };
        fling = 0; manualUntil = performance.now() + 5500;
        status.textContent = `${index + 1} of ${N}: ${products[index].kind} jersey`;
      }
      document.querySelector('.previous').addEventListener('click', () => step(-1));
      document.querySelector('.next').addEventListener('click', () => step(1));
      hero.addEventListener('wheel', event => {
        if (selected || drawer.open) return;
        event.preventDefault(); navigation = null;
        base -= clamp(event.deltaY + event.deltaX, -100, 100) * .002;
        manualUntil = performance.now() + 4000;
      }, { passive: false });
      hero.addEventListener('pointermove', event => {
        if (event.pointerType === 'touch' || motion.matches) return;
        pointer = { x: (event.clientX / innerWidth - .5) * 2, y: (event.clientY / innerHeight - .5) * 2 };
      });
      hero.addEventListener('pointerleave', () => { pointer = { x: 0, y: 0 }; });''')
html = html.replace("if (event.key === 'Escape') closeItem();", "if (drawer.open) return;\n        if (event.key === 'Escape') closeItem();\n        if (!selected && (event.key === 'ArrowLeft' || event.key === 'ArrowRight')) { event.preventDefault(); step(event.key === 'ArrowLeft' ? -1 : 1); }")
html = html.replace('[close, ...swatches.filter(s => s.tabIndex === 0), add]', '[close, ...swatches.filter(s => s.tabIndex === 0), ...shopLinks]')
html = html.replace('(row + 1) % 4', '(row + 1) % 2').replace('(row + 3) % 4', '(row + 1) % 2').replace("event.key === 'End') next = 3", "event.key === 'End') next = 1")
html = html.replace("selected = item; hovered = null; drag = null;", "selected = item; hovered = null; drag = null; navigation = null;")
html = html.replace("if (selected || (event.pointerType", "if (event.target.closest('.panel, .close') || selected || (event.pointerType")
html = html.replace("suppressClick = false;", "suppressClick = false; navigation = null;",1) if False else html
html = html.replace("        suppressClick = false;\n      });", "        suppressClick = false; navigation = null;\n      });")
html = html.replace("drag = null; stage.classList.remove('dragging');", "drag = null; stage.classList.remove('dragging');\n        if (wasDrag) setTimeout(() => { suppressClick = false; }, 0);")
start = html.index('      function landed()')
end = html.index('      function render(now)',start)
html = html[:start]+html[end:]
html = html.replace("if (entered && !selected && !drag) {", "if (entered && !selected && !drag && !drawer.open) {\n            if (navigation) {\n              const progress = motion.matches ? 1 : clamp((now-navigation.start)/650);\n              base = mix(navigation.from, navigation.to, cubic(progress));\n              if (progress === 1) navigation = null;\n            }")
html = html.replace('if (!motion.matches) base += OMEGA * dt * autoWeight;', 'if (!motion.matches && !paused && !hovered && !navigation && now > manualUntil && !stage.contains(document.activeElement)) base += OMEGA * dt * autoWeight;')
html = html.replace('let front = 0, best = -Infinity;', '''parallax.x = mix(parallax.x, motion.matches ? 0 : pointer.x, Math.min(1, dt * 5));
          parallax.y = mix(parallax.y, motion.matches ? 0 : pointer.y, Math.min(1, dt * 5));
          document.querySelector('.ghost').style.transform = `translate(${-parallax.x * 13}px, ${-parallax.y * 9}px)`;
          let front = 0, best = -Infinity;''')
html = html.replace('y += (1 - reveal) * 36;', 'x += parallax.x * (10 + p.k * 9) * (1-d); y += parallax.y * (6 + p.k * 6) * (1-d);\n            y += (1 - reveal) * 36;')
html = html.replace('dots.forEach((dot, i)', "frontIndex = front;\n          if (front !== previousFront && !hovered && !selected) { setIndex(front + 1, products[front].kind); previousFront = front; }\n          dots.forEach((dot, i)")
html = html.replace("'.index', '.scroll-hint'", "'.index', '.scroll-hint', '.explore-controls'")
html = html.replace("if (!motion.matches) return;\n        revealAnimations", "if (!motion.matches) return;\n        setPaused(true); navigation = null;\n        revealAnimations")
start = html.index('      const sheet = new Image();')
end = html.index('      setTimeout(entrance, 2500);',start)
html = html[:start]+'''      const preloads = products.flatMap((product, col) => [0, 1].map(row => new Promise(resolve => {
        const image = new Image(); image.onload = resolve;
        image.onerror = () => { document.querySelector('.asset-warning').hidden = false; resolve(); };
        image.src = `assets/beyond-doubt/${product.id}-${row === 0 ? 'front' : 'back'}.png`;
      })));
      Promise.all(preloads).then(entrance);
'''+html[end:]
html = html.replace('title.textContent = `${colours[selected.row]} ${product.kind}`;', 'title.textContent = `${product.kind} jersey`;')
html = html.replace("selected.el.setAttribute('aria-label', title.textContent);", "selected.el.setAttribute('aria-label', `${title.textContent}, ${colours[selected.row].toLowerCase()} view`);")
html = html.replace('min-width: 16em', 'min-width: 12em')
html = html.replace('<div class="index-label choose-label">FRONT &amp; BACK<br>EXPLORE THE DETAILS</div>', '<div class="index-label choose-label">FRONT &amp; BACK<br>JERSEY DETAILS</div>')
html = html.replace('.drawer-head img { width: 190px;', '.drawer-head img { height: auto; width: 190px;')
html = html.replace('<script>document.documentElement.classList.add(\'js\');</script>', '')
html = html.replace('.js .rv { opacity: 0; }', '')
html = html.replace('  </style>', '''
    .menu, .shop-link, .motion-toggle, .view-button, .store-button { font-size: 11px; letter-spacing: .12em; }
    .caps, .index-labels, .index-kind, .right-label span, .category, .scroll-hint span { font-size: max(11px, calc(10.5 * var(--n))); }
    .index-labels { min-width: 12em; letter-spacing: .13em; }
    .stock-note { font-size: 12px; }
    .profile-note p { font-size: 12px; }
    .view-switch { border-bottom: 0; }
    .view-button { border-bottom: 1px solid var(--line); }
    .view-button[aria-checked="true"] { border-bottom-width: 2px; }
    .index-number { transition-duration: .35s; }
    @media (max-width: 820px) and (min-height: 521px) {
      .index-labels { min-width: 0; max-width: 135px; }
      .collection-label { max-width: 135px; }
      .index-window { font-size: 30px; }
      .index-bar { margin: 0 10px; }
      .motion-toggle { display: block; position: fixed; right: 20px; bottom: 78px; padding: 0 12px; min-width: 66px; border: 1px solid var(--line); background: var(--bg); }
      .detail .index { visibility: hidden; }
      .stock-note { font-size: 12px; }
      .scroll-hint { bottom: 155px; }
      .scroll-hint span { font-size: 11px; letter-spacing: .13em; }
      .tagline { display: block; top: 103px; width: 100%; font-size: 11px; }
      .detail .tagline { visibility: hidden; }
    }
    @media (max-height: 520px) {
      .panel { left: calc(865 * var(--u)); top: calc(172 * var(--u)); width: calc(690 * var(--u)); max-height: calc(100dvh - 92px); overflow-y: auto; scrollbar-width: thin; }
      .product-name { font-size: 22px; }
      .category { margin-bottom: 8px; font-size: 11px; letter-spacing: .1em; }
      .view-switch { margin: 3px 0 6px; }
      .view-button { min-height: 40px; padding: 0 12px; }
      .store-button { padding: 0 10px; gap: 9px; font-size: 11px; }
      .product-shops { gap: 8px; }
      .stock-note { margin-top: 8px; font-size: 12px; }
      .detail .index { visibility: hidden; }
    }
    @media (max-width: 350px) and (min-height: 521px) { .index-labels { max-width: 105px; } }
  </style>''')
Path('index-beyond-doubt.html').write_text(html,encoding='utf-8')
print('Created index-beyond-doubt.html from the preserved template.')
