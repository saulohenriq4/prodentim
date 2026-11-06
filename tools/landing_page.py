"""Check the continuous landing page, including images and all six sections."""
from pathlib import Path
import json, os
from playwright.sync_api import sync_playwright
BASE=os.environ.get('MEGA7_TEST_URL','http://127.0.0.1:8000');out=Path(os.environ.get('MEGA7_REPORT_DIR','/workspace/reports/mega7/v2-1/after'));out.mkdir(parents=True,exist_ok=True)
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
  assert page.locator('main > section').count()==6
  assert page.locator('.affiliate').count()==3
  assert page.locator('#checklist img').count()==1
  for link in page.locator('.affiliate').all():
   assert link.bounding_box()['height']>=48
  assert page.evaluate('document.documentElement.scrollHeight>innerHeight*2')
  for section in page.locator('main > section').all():
   section.scroll_into_view_if_needed()
  for photo in page.locator('main img').all():
   photo.scroll_into_view_if_needed()
   photo.evaluate('(i)=>i.decode()')
  page.locator('.affiliate').last.scroll_into_view_if_needed()
  assert page.evaluate('scrollY>innerHeight')
  for link in page.locator('.affiliate').all():
   assert link.get_attribute('href')=='https://prodentim24.com/text.php?aff=Saulohenri4'
   assert 'sponsored' in link.get_attribute('rel')
  page.evaluate('window.scrollTo({top:0,behavior:"instant"})')
  page.screenshot(path=str(out/f'after-{w}x{h}.png'))
  page.screenshot(path=str(out/f'after-{w}x{h}-full.png'),full_page=True)
  assert not errors,errors
  checks.append({'viewport':[w,h],'image':img,'cta':cta,'console_errors':errors,'webp':True})
  c.close()
 b.close()
(out/'checks.json').write_text(json.dumps(checks,indent=2));print(json.dumps(checks,indent=2))
