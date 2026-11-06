"""Capture and check the premium hero locally without sending external requests."""
from pathlib import Path
import json
from playwright.sync_api import sync_playwright
BASE='http://127.0.0.1:8000';out=Path('/workspace/reports/mega7/premium-hero');out.mkdir(parents=True,exist_ok=True)
checks=[]
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 for w,h in [(1366,768),(1920,1080),(360,800),(390,844),(430,932)]:
  c=b.new_context(viewport={'width':w,'height':h},reduced_motion='reduce')
  c.route('**/*',lambda r:r.continue_() if r.request.url.startswith(BASE) else r.abort())
  page=c.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
  page.goto(BASE+'/prodentim/');page.locator('#decline-ads').click()
  im=page.locator('.premium-hero img');im.wait_for();page.wait_for_function('document.querySelector(".premium-hero img").complete')
  assert im.evaluate('(i)=>i.naturalWidth===815&&i.naturalHeight===621')
  assert im.evaluate('(i)=>i.currentSrc.endsWith(".webp")')
  assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
  img=im.bounding_box();title=page.locator('h1').bounding_box();cta=page.locator('.premium-hero .button').bounding_box()
  assert img['width']>270 and img['height']>200
  assert cta['height']>=48
  if w>700:
   assert img['x']>=title['x']+title['width']
   assert img['y']+img['height']<=h
  else:
   assert img['y']>=title['y']+title['height']
   assert cta['y']>=img['y']+img['height']
  assert page.locator('.premium-hero .button').get_attribute('href')=='https://prodentim24.com/text.php?aff=Saulohenri4'
  page.screenshot(path=str(out/f'after-{w}x{h}.png'))
  page.screenshot(path=str(out/f'after-{w}x{h}-full.png'),full_page=True)
  assert not errors,errors
  checks.append({'viewport':[w,h],'image':img,'cta':cta,'console_errors':errors,'webp':True})
  c.close()
 b.close()
(out/'checks.json').write_text(json.dumps(checks,indent=2));print(json.dumps(checks,indent=2))
