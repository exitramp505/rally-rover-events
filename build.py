import os,json,urllib.request
import re,html
from PIL import Image
D=os.environ.get('DESIGN_DIR','/workspace/design-trial/')
ev=[
 dict(slug='georgetown',dir='georgetown',pre='georgetown_stroll',name='Georgetown Christmas Stroll Parade',short='Georgetown, TX',when='Saturday, December 5, 2026 · 10:00 AM',where='Historic Downtown Georgetown, TX',acc='#b3202a',bg='#10264a',fn='georgetown_FINAL.md',store='https://rally-rover.printful.me',off='https://dgagtx.org/Parade',offl='Parade route, times, and road closures',collection='Lone Star & courthouse designs'),
 dict(slug='flower-mound',dir='flowermound',pre='flowermound_holidays_on_the_mound',name='Flower Mound Christmas Parade & Tree Lighting',short='Flower Mound, TX',when='Saturday, December 5, 2026 · Festivities 5:30 PM, parade 6:00 PM',where='Gerault Park, 1200 Gerault Rd., Flower Mound, TX',acc='#b8902f',bg='#0f3b2a',fn='flowermound_FINAL.md',store='https://holidays-on-the-mound.printful.me',off='https://www.flowermound.gov/parade',offl='Schedule, parking, and shuttle info',collection='Holidays on the Mound designs'),
 dict(slug='richmond',dir='richmond',pre='richmond_christmas_on_broad_street',name='Richmond Christmas Parade',short='Richmond, VA',when='Saturday, December 5, 2026 · 10:15 AM',where='10th & Marshall Streets to Broad Street, Richmond, VA',acc='#b5472f',bg='#14284d',fn='richmond_FINAL.md',store='https://christmas-on-broad-street.printful.me',off='https://www.richmondparade.org/',offl='Route, viewing info, and lineup',collection='Christmas on Broad Street designs'),
]
# Form backend: FormSubmit (formsubmit.co) AJAX endpoint. Set FORM_ID to the activated random alias (or the inbox address).
import os
FORM_ID=os.environ.get('FORM_ID','38ad0f61698bde7da899feafa7e98b99')
FORM_URL='https://formsubmit.co/ajax/'+FORM_ID
CONSENT='Send me updates about this event and merch. Unsubscribe anytime.'
DISC="Independent fan guide and merchandise; not affiliated with or endorsed by the event organizers."
CSS="""*{box-sizing:border-box}body{margin:0;font:17px/1.6 Georgia,'Times New Roman',serif;color:#222;background:#faf7f2}
a{color:var(--a,#b3202a)}header.top{background:var(--bg,#10264a);color:#fff;padding:14px 20px}header.top a{color:#fff;text-decoration:none;font-weight:bold;font-family:system-ui,sans-serif}
main{max-width:860px;margin:0 auto;padding:20px}h1{font-size:2rem;line-height:1.2;margin:.3em 0}h2{margin-top:1.6em;font-size:1.4rem}
.when{font:600 1.05rem system-ui,sans-serif;color:var(--a)}.flyer{width:100%;height:auto;border-radius:6px;box-shadow:0 2px 12px #0003;margin:16px 0}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px}.grid img{width:100%;border-radius:6px;background:#fff}
.btn{display:inline-block;background:var(--a);color:#fff!important;text-decoration:none;padding:12px 22px;border-radius:6px;font:600 1rem system-ui,sans-serif;margin:6px 6px 6px 0}
.btn.alt{background:#fff;color:var(--a)!important;border:2px solid var(--a)}ul.p{padding-left:1.2em}
.rsvp{background:#fff;border:2px solid var(--a);border-radius:10px;padding:18px 20px;margin:28px 0}.rsvp h2{margin-top:0}.rsvp label{display:block;font:600 .95rem system-ui,sans-serif;margin:10px 0 4px}.rsvp input[type=email],.rsvp input[type=text],.rsvp select{width:100%;padding:10px;font:1rem system-ui,sans-serif;border:1px solid #bbb;border-radius:6px}
.rsvp .consent{display:flex;gap:8px;align-items:flex-start;font:.95rem system-ui,sans-serif;margin:14px 0}.rsvp .consent input{margin-top:4px}.rsvp button{background:var(--a);color:#fff;border:0;border-radius:6px;padding:12px 22px;font:600 1rem system-ui,sans-serif;cursor:pointer}.rsvp .note{font:.85rem system-ui,sans-serif;color:#555}.hp{position:absolute;left:-9999px;height:0;width:0;overflow:hidden}.msg{font:600 1rem system-ui,sans-serif}.err{color:#b00020}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px}.card{background:#fff;border-radius:8px;overflow:hidden;box-shadow:0 1px 8px #0002;text-decoration:none;color:#222}.card img{width:100%;display:block}.card div{padding:12px 14px}
.mgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px}.mc{position:relative;background:#fff;border-radius:8px;overflow:hidden;box-shadow:0 1px 8px #0002;display:flex;flex-direction:column}.mc img{width:100%;display:block;aspect-ratio:1;object-fit:cover}.mc>div{padding:10px 12px 12px;display:flex;flex-direction:column;flex:1}.mc strong{font:600 .95rem/1.3 system-ui,sans-serif}.mc p{margin:4px 0}.pr{font:600 1rem system-ui,sans-serif}.sz{font:.78rem/1.4 system-ui,sans-serif;color:#555}.mc .btn{margin:auto 0 0;text-align:center;padding:10px}.pv{position:absolute;top:8px;left:8px;background:#000a;color:#fff;font:600 .7rem system-ui,sans-serif;padding:2px 8px;border-radius:10px}.note2{font:.85rem system-ui,sans-serif;color:#555}
footer{max-width:860px;margin:30px auto;padding:20px;border-top:1px solid #ddd;font-size:.85rem;color:#555}"""

# ---- Fourthwall merch (build-time). Token from env FOURTHWALL_STOREFRONT_TOKEN or /workspace/fourthwall_api.txt; never written to output.
HANDLES={'georgetown':'georgetown-christmas-stroll','flower-mound':'flower-mound-christmas-parade','richmond':'richmond-christmas-parade'}
SHOP='https://rally-rover-shop.fourthwall.com'
PREVIEW_BADGE=os.environ.get('MERCH_PREVIEW_BADGE')=='1'  # set to 1 to show a small "Preview" badge on fallback cards
def _token():
    t=os.environ.get('FOURTHWALL_STOREFRONT_TOKEN')
    if t: return t.strip()
    try:
        for l in open('/workspace/fourthwall_api.txt'):
            if l.startswith('STOREFRONT_TOKEN='): return l.split('=',1)[1].strip()
    except OSError: pass
    return None
def _money(v): v=float(v); return f'${v:.0f}' if v==int(v) else f'${v:.2f}'
def api_products(handle):
    t=_token()
    if not t: return []
    try:
        u=f'https://storefront-api.fourthwall.com/v1/collections/{handle}/products?storefront_token={t}'
        j=json.load(urllib.request.urlopen(u,timeout=20))
    except Exception as ex:
        print('merch api: no products for',handle,'-',type(ex).__name__); return []
    out=[]
    for p in j.get('results',[]):
        vs=p.get('variants') or []
        prices=[v['unitPrice']['value'] for v in vs if v.get('unitPrice')]
        if not prices: continue
        sizes=[]
        if len(vs)>1:
            seen={}
            for v in vs:
                seen.setdefault(v.get('name','').split('/')[-1].strip(),v['unitPrice']['value'])
            sizes=[dict(label=k,price=x) for k,x in seen.items() if k]
        img=((p.get('images') or [{}])[0]).get('url','')
        out.append(dict(title=p.get('name',''),price=min(prices),slug=p.get('slug',''),url=f"{SHOP}/products/{p.get('slug','')}",image=img,sizes=sizes))
    return out
def merch_products(slug):
    """Returns (products, is_preview). Live API first, else data/merch_preview.json."""
    p=api_products(HANDLES[slug])
    if p: return p,False
    try: return json.load(open('data/merch_preview.json'))['collections'].get(slug,[]),True
    except OSError: return [],True
def merch_section(slug):
    ps,prev=merch_products(slug)
    if not ps: return ''
    c=''
    for p in ps:
        sz=''
        if p.get('sizes'):
            sz='<p class="sz">'+' · '.join(f"{html.escape(str(s['label']))} {_money(s['price'])}" for s in p['sizes'])+'</p>'
        badge='<span class="pv">Preview</span>' if (prev and PREVIEW_BADGE) else ''
        c+=f'<div class="mc">{badge}<a href="{html.escape(p["url"])}" rel="noopener"><img src="{html.escape(p["image"])}" alt="{html.escape(p["title"])}" loading="lazy"></a><div><strong>{html.escape(p["title"])}</strong><p class="pr">From {_money(p["price"])}</p>{sz}<a class="btn" href="{html.escape(p["url"])}" rel="noopener">Buy</a></div></div>'
    return f'<section id="merch"><h2>Merch</h2><div class="mgrid">{c}</div><p class="note2">Shipping is added at checkout.</p></section>'
def shell(title,body,a='#b3202a',bg='#10264a',desc=''):
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}"><style>:root{{--a:{a};--bg:{bg}}}{CSS}</style></head><body><header class="top"><a href="index.html">Rally Rover · Parade Guides</a></header><main>{body}</main>{JS}<footer>{DISC} · <a href="privacy.html">Privacy</a></footer></body></html>'

def rsvp(evname):
    en=html.escape(evname)
    return f'''<section class="rsvp" id="rsvp"><h2>Get updates for {en}</h2>
<form class="rsvp-form" action="{FORM_URL}" method="POST" novalidate>
<label for="rsvp-email">Email</label><input id="rsvp-email" type="email" name="email" required autocomplete="email">
<label for="rsvp-name">First name (optional)</label><input id="rsvp-name" type="text" name="first_name" autocomplete="given-name">
<input type="hidden" name="event" value="{en}">
<input type="hidden" name="_subject" value="Rally Rover RSVP signup: {en}"><input type="hidden" name="_captcha" value="false"><input type="hidden" name="_template" value="table">
<div class="hp" aria-hidden="true"><label>Leave this empty<input type="text" name="_honey" tabindex="-1" autocomplete="off"></label></div>
<label class="consent"><input type="checkbox" name="consent" value="yes" required><span>{CONSENT} <a href="privacy.html">Privacy</a></span></label>
<button type="submit">RSVP for updates</button><p class="note">Interest-only RSVP, not a ticket.</p><p class="msg" role="status" aria-live="polite"></p></form>
<div class="thanks" hidden><p class="msg">Thanks! You're on the list. We'll email you about this event and merch. You can unsubscribe anytime.</p></div></section>'''
JS="""<script>document.querySelectorAll('.rsvp-form').forEach(function(f){f.addEventListener('submit',function(ev){ev.preventDefault();var m=f.querySelector('.msg');m.className='msg';
if(f.querySelector('[name=_honey]').value){f.parentNode.querySelector('.thanks').hidden=false;f.hidden=true;return}
if(!f.email.value||!f.email.checkValidity()){m.className='msg err';m.textContent='Please enter a valid email.';return}
if(!f.consent.checked){m.className='msg err';m.textContent='Please tick the consent box to sign up.';return}
var d=new FormData(f);d.set('consent_text',"CONSENT_TEXT");var b=f.querySelector('button');b.disabled=true;m.textContent='Sending...';
fetch(f.action,{method:'POST',body:d,headers:{'Accept':'application/json'}}).then(function(r){return r.json()}).then(function(j){if(j.success===true||j.success==='true'){f.hidden=true;f.parentNode.querySelector('.thanks').hidden=false}else{throw 0}}).catch(function(){b.disabled=false;m.className='msg err';m.textContent='Sorry, that did not go through. Please try again later.'})})})</script>""".replace('CONSENT_TEXT',CONSENT)
cards=''
for e in ev:
    t=open('docs/copy/'+e['fn']).read()
    promo=t.split('## Promo post (social / event page)\n')[1].split('\n## ')[0].strip().split('\n')
    # split paragraphs before "Lead with" list
    paras=[];items=[]
    for l in promo:
        l=l.strip()
        if l.startswith('- '): items.append(l[2:])
        elif l and not l.startswith('Shop the store') and not l.startswith(('Parade route','Schedule,','Route,')) and not l.startswith('Lead with'): paras.append(l)
    # make images
    for k,s in ([] if not os.path.isdir(D) else [('flyer','flyer_8.5x11_2550x3300'),('hoodie','mockup_hoodie'),('mug','mockup_mug'),('tee','mockup_tee'),('ornament','mockup_ornament')]):
        im=Image.open(f"{D}{e['dir']}/{e['pre']}_{s}.png").convert('RGB')
        im.thumbnail((1000,1300) if k=='flyer' else (500,500))
        im.save(f"img/{e['slug']}-{k}.jpg",quality=82,optimize=True)
    Image.open(f"img/{e['slug']}-flyer.jpg")
    merch=''.join(f'<li>{html.escape(i)}</li>' for i in items)
    body=f'''<p class="when">{e['when']}</p><h1>{e['name']}</h1><p>{e['where']} · Free to attend</p>
<img class="flyer" src="img/{e['slug']}-flyer.jpg" alt="{e['name']} flyer" width="1000" height="1294">
<h2>About the day</h2>{''.join(f'<p>{html.escape(p)}</p>' for p in paras[:-1] if not p.startswith("Take that") and 'Our ' not in p[:4])}
<p><a class="btn alt" href="{e['off']}" rel="noopener">Official event page: {e['offl']}</a></p>
<h2>Take it home: {e['collection']}</h2><p>{html.escape([p for p in paras if p.startswith('Take that') or p.startswith('Our ')][0] if [p for p in paras if p.startswith('Take that') or p.startswith('Our ')] else '')}</p>
{merch_section(e['slug'])}
<p><a class="btn alt" href="{e['store']}" rel="noopener">More at our store</a></p>
{rsvp(e['name'])}'''
    open(f"{e['slug']}.html",'w').write(shell(e['name']+' 2026 | Rally Rover',body,e['acc'],e['bg'],f"{e['name']}, {e['when']}. Event info and holiday merch."))
    cards+=f'<a class="card" href="{e["slug"]}.html"><img src="img/{e["slug"]}-flyer.jpg" alt=""><div><strong>{e["name"]}</strong><br>{e["short"]} · Dec 5, 2026</div></a>'
home=f'<h1>Holiday Parade Guides, December 5, 2026</h1><p>Where to be, when to arrive, and cozy merch to wear while you watch. Pick your parade.</p><div class="cards">{cards}</div>'
priv=f'''<h1>Privacy</h1><p>Last updated October 18, 2026.</p>
<h2>Who we are</h2><p>Rally Rover publishes holiday parade guides and merchandise.</p>
<h2>What the RSVP form collects</h2><p>Your email address, an optional first name, which event you are interested in, and your consent. </p>
<h2>How we use it</h2><p>Only to email you updates about the event you chose and about our merchandise, as you agreed when you ticked the consent box ("{CONSENT}"). We do not sell or share your email.</p>
<h2>Where it is processed</h2><p>Form submissions are relayed by the form service FormSubmit (formsubmit.co) to our project inbox. This site has no analytics or tracking cookies. Links to the Printful stores and official event sites are governed by those sites' own policies.</p>
<h2>Unsubscribe or delete</h2><p>Every email will tell you how to unsubscribe. You can also email rallyrover@mail.grokbot.com at any time to ask us to remove or delete your information, and we will do so.</p>
<h2>Children</h2><p>This form is intended for adults; please do not submit information for a child.</p>'''
open('privacy.html','w').write(shell('Privacy | Rally Rover',priv,desc='Privacy note for Rally Rover RSVP updates.'))
open('index.html','w').write(shell('Rally Rover | Holiday Parade Guides 2026',home,desc='Holiday parade guides and merch for Georgetown, Flower Mound, and Richmond.'))
