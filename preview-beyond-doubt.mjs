import puppeteer from 'file:///C:/Users/Habib/AppData/Roaming/npm/node_modules/puppeteer/lib/puppeteer/puppeteer.js';
import { mkdir, readFile, writeFile } from 'node:fs/promises';
import { createHash } from 'node:crypto';

await mkdir('.impeccable/review', { recursive: true });
const browser = await puppeteer.launch({ headless: true, pipe: true, executablePath: 'C:/Users/Habib/AppData/Local/ms-playwright/chromium-1243/chrome-win64/chrome.exe', args: ['--no-sandbox'] });
const reports = [];
const pause = ms => new Promise(resolve => setTimeout(resolve, ms));
try {
  for (const [name, width, height] of [['desktop',1440,900],['mobile',390,844],['small-mobile',360,640],['landscape',844,390]]) {
    const page = await browser.newPage();
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    await page.setViewport({width,height,isMobile:name.includes('mobile'),hasTouch:name.includes('mobile')});
    await page.emulateMediaFeatures([{name:'prefers-reduced-motion',value:'reduce'}]);
    await page.goto('file:///C:/Users/Habib/Kids-Store/index-beyond-doubt.html', {waitUntil:'domcontentloaded'});
    await page.waitForSelector('.item');
    await pause(500);
    const images = await page.evaluate(async()=>{
      const backgrounds = [...document.querySelectorAll('.art')].flatMap(el=>{
        const src=getComputedStyle(el).backgroundImage.slice(5,-2);
        return [src,src.replace('-front.png','-back.png')];
      });
      return await Promise.all(backgrounds.map(src=>new Promise(resolve=>{const im=new Image();im.onload=()=>resolve({src,loaded:true,width:im.naturalWidth,height:im.naturalHeight});im.onerror=()=>resolve({src,loaded:false});im.src=src;})));
    });
    const motionControl = await page.$eval('.motion-toggle',el=>{const r=el.getBoundingClientRect();return {visible:r.width>0&&r.height>0&&getComputedStyle(el).visibility==='visible',x:r.x,y:r.y,right:r.right,bottom:r.bottom};});
    await page.screenshot({path:`.impeccable/review/${name}.png`});
    await page.click('.next');
    await pause(100);
    const advanced = await page.$eval('.index-kind',el=>el.textContent);
    await page.click('.item');
    await pause(150);
    const opened = await page.$eval('.panel',el=>!el.inert&&el.getAttribute('aria-hidden')==='false');
    await page.click('[aria-label="Back view"]');
    const back = await page.$eval('.item[aria-expanded="true"] .art',el=>el.style.backgroundImage.includes('-back.png'));
    await page.screenshot({path:`.impeccable/review/${name}-detail.png`});
    const detailBounds = await page.$eval('.panel',el=>{const r=el.getBoundingClientRect();return {x:r.x,y:r.y,right:r.right,bottom:r.bottom,width:r.width};});
    await page.keyboard.press('Escape');
    await pause(100);
    await page.click('.menu');
    const drawerOpen = await page.$eval('dialog',el=>el.open);
    await page.screenshot({path:`.impeccable/review/${name}-about.png`});
    await page.keyboard.press('Escape');
    const drawerClosed = await page.$eval('dialog',el=>!el.open);
    const overflow = await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth);
    const links = await page.$$eval('a',els=>els.map(el=>({text:el.textContent.trim()||el.getAttribute('aria-label'),href:el.getAttribute('href')})));
    reports.push({name,width,height,errors,images,advanced,opened,back,drawerOpen,drawerClosed,overflow,detailBounds,motionControl,links});
    await page.close();
  }
  const page = await browser.newPage();
  await page.setViewport({width:1440,height:900});
  await page.goto('file:///C:/Users/Habib/Kids-Store/index-beyond-doubt.html',{waitUntil:'domcontentloaded'});
  await pause(3000);
  await page.click('.motion-toggle');
  await page.mouse.move(50,500); await pause(200);
  const before = await page.$eval('.ghost',el=>el.style.transform);
  await page.mouse.move(1300,600); await pause(250);
  const after = await page.$eval('.ghost',el=>el.style.transform);
  await page.mouse.move(750,470); await page.mouse.down(); await page.mouse.move(950,470,{steps:10}); await page.mouse.up(); await pause(100);
  await page.click('.item'); await pause(650);
  const clickAfterDrag = await page.$eval('.hero',el=>el.classList.contains('detail'));
  reports.push({motion:{parallaxMoves:before!==after,clickAfterDrag}});
  await page.close();
  const mobile = await browser.newPage();
  await mobile.setViewport({width:360,height:640,isMobile:true,hasTouch:true});
  await mobile.goto('file:///C:/Users/Habib/Kids-Store/index-beyond-doubt.html',{waitUntil:'domcontentloaded'});
  await pause(3000);
  await mobile.click('.motion-toggle'); await pause(800);
  await pause(1200);
  const pausedBefore = await mobile.$eval('.item',el=>{const m=new DOMMatrix(getComputedStyle(el).transform);return [m.a,m.b,m.c,m.d,m.e,m.f];});
  await pause(900);
  const pausedAfter = await mobile.$eval('.item',el=>{const m=new DOMMatrix(getComputedStyle(el).transform);return [m.a,m.b,m.c,m.d,m.e,m.f];});
  const pauseLabel = await mobile.$eval('.motion-toggle',el=>el.textContent);
  await mobile.click('.motion-toggle'); await pause(800);
  const playLabel = await mobile.$eval('.motion-toggle',el=>el.textContent);
  const restingDelta=Math.max(...pausedBefore.map((v,i)=>Math.abs(v-pausedAfter[i])));
  reports.push({mobileMotion:{restsWhenPaused:restingDelta<0.1,restingDelta,pauseLabel,playLabel}});
  await mobile.close();
  const templateHash = createHash('sha256').update(await readFile('index.html')).digest('hex');
  reports.push({templatePreserved:templateHash==='41234d92add801689f8571b25264e31b682c65b44ea28cba0cebf4a899103e54',templateHash});
  await writeFile('.impeccable/review/checks.json',JSON.stringify(reports,null,2));
  console.log(JSON.stringify(reports.map(({links,images,...rest})=>({...rest,...(images?{allProductsLoaded:images.every(im=>im.loaded),highResolutionProducts:images.every(im=>im.width>=1000&&im.height>=1000)}:{})})),null,2));
} finally {
  await browser.close();
}
