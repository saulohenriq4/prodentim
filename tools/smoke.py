"""Local-only browser checks. External traffic is blocked, including Ads and affiliate URLs."""
import json, os
from pathlib import Path
from playwright.sync_api import sync_playwright
BASE=os.environ.get('MEGA7_TEST_URL','http://127.0.0.1:8000')
OUT=Path(os.environ.get('MEGA7_REPORT_DIR','/workspace/reports/mega7')); OUT.mkdir(parents=True,exist_ok=True)
AFF='https://prodentim24.com/text.php?aff=Saulohenri4'
results=[]
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 for width,height in [(360,800),(390,844),(768,1024),(1440,1000)]:
  context=browser.new_context(viewport={'width':width,'height':height},reduced_motion='reduce')
  context.route('**/*',lambda r:r.continue_() if r.request.url.startswith(BASE) else r.abort())
  page=context.new_page(); errors=[]; page.on('pageerror',lambda e:errors.append(str(e)))
  for path in ['/','/prodentim/','/about/','/contact/','/privacy/','/terms/','/affiliate-disclosure/','/medical-disclaimer/']:
   response=page.goto(BASE+path); assert response.status==200
   assert page.locator('h1').count()==1
   assert page.locator('html').get_attribute('lang')=='en-US'
   assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'),(width,path,'overflow')
   page.locator('#decline-ads').click() if page.locator('#consent').is_visible() else None
   assert page.locator('script[src*="googletagmanager"]').count()==0
   assert page.locator('link[rel=canonical]').get_attribute('href')=='https://mega7products.com'+path
   # Scroll to lazy images before checking their load state.
   for photo in page.locator('img').all():
    photo.scroll_into_view_if_needed()
    photo.evaluate('(i)=>i.decode()')
   page.evaluate('window.scrollTo({top:0,behavior:"instant"})')
   images=page.locator('img').evaluate_all('(xs)=>xs.every(x=>x.complete&&x.naturalWidth>0)'); assert images
   if path=='/prodentim/':
    links=page.locator('.affiliate'); assert links.count()==2
    for link in links.all():
     assert link.get_attribute('href')==AFF
     assert 'sponsored' in link.get_attribute('rel')
    page.locator('summary').first.click(); assert page.locator('details').first.get_attribute('open') is not None
    page.locator('a[href="#checklist"]').first.click(); assert page.url.endswith('#checklist')
    page.screenshot(path=str(OUT/f'prodentim-{width}.png'),full_page=True)
   if path=='/': page.screenshot(path=str(OUT/f'home-{width}.png'),full_page=True)
   # Resolve all same-site resources and anchors without following seller links.
   for href in page.locator('a[href]').evaluate_all('(xs)=>xs.map(x=>x.getAttribute("href"))'):
    if href.startswith('#'): assert page.locator('[id="'+href[1:]+'"]').count()>0
    elif href.startswith('/'):
     target,_,anchor=href.partition('#'); assert page.request.get(BASE+target).status==200
   results.append({'width':width,'path':path,'passed':True})
  assert not errors,errors
  context.close()
 # Event tests with a network stub: no visit or click is transmitted to Google or seller.
 context=browser.new_context(); requests=[]
 def route(r):
  if r.request.url.startswith(BASE): r.continue_()
  else: requests.append(r.request.url); r.fulfill(status=200,body='',content_type='application/javascript')
 context.route('**/*',route); page=context.new_page();page.goto(BASE+'/prodentim/')
 assert not requests
 page.locator('#accept-ads').click()
 page.wait_for_function('window.dataLayer && window.dataLayer.length >= 2')
 assert page.locator('script[src*="AW-17961565555"]').count()==1
 page.evaluate('document.querySelector(".affiliate").addEventListener("click",e=>e.preventDefault())')
 page.locator('.affiliate').first.click()
 events=page.evaluate('window.dataLayer.map(x=>Array.from(x))')
 clicks=[x for x in events if x[0]=='event'];assert len(clicks)==1
 assert clicks[0][1]=='conversion'
 assert clicks[0][2]['send_to']=='AW-17961565555/98brCNTlyZ4cEPP63vRC'
 assert clicks[0][2]['event_label']=='outbound_affiliate_click'
 assert clicks[0][2]['placement']=='hero'
 assert 'value' not in clicks[0][2] and 'transaction_id' not in clicks[0][2]
 page.reload();assert page.evaluate('localStorage.getItem("mega7-ads-choice-v1")')=='granted'
 page.locator('#privacy-settings').click();page.locator('#decline-ads').click();page.wait_for_load_state()
 assert page.locator('script[src*="googletagmanager"]').count()==0
 context.close()
 # Native links and FAQ work without JavaScript.
 context=browser.new_context(java_script_enabled=False);page=context.new_page();page.goto(BASE+'/prodentim/')
 assert page.locator('.affiliate').first.get_attribute('href')==AFF
 page.locator('summary').first.click();assert page.locator('details').first.get_attribute('open') is not None
 context.close(); browser.close()
(OUT/'smoke-results.json').write_text(json.dumps({'pages':results,'events':'passed with external requests stubbed','no_js':'passed','console_errors':0},indent=2))
print(f'PASS: {len(results)} page/viewport checks; consent, exact affiliate links, event payload, withdrawal, no-JS, local navigation, console.')
