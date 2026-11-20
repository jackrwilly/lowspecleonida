import os, re, shutil, datetime
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "site")
shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(OUT + "/guides")
DOMAIN = "https://lowspecleonida.com"
TODAY = "2026-11-19"

CSS = open(os.path.join(ROOT, "build", "style.css")).read()
open(OUT + "/style.css", "w").write(CSS)

NAV = [("/will-it-run.html", "Will It Run?"), ("/builds.html", "Budget Builds"), ("/settings.html", "Best Settings"), ("/guides/", "Guides"), ("/mods.html", "Mods")]

def page(path, title, desc, body, active="", script=""):
    nav = "".join(f'<a class="l{" on" if h==active else ""}" href="{h}">{t}</a>' for h, t in NAV)
    canon = DOMAIN + "/" + path.replace("index.html", "")
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@400;600;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css">
</head>
<body>
<header><div class="nav"><a class="logo" href="/">LowSpec<span>Leonida</span></a>{nav}</div></header>
<main>
{body}
</main>
<footer>© 2026 LowSpecLeonida · Unofficial fan site · Not affiliated with Rockstar Games or Take-Two Interactive · <a href="/about.html">About</a> · <a href="/privacy.html">Privacy Policy</a></footer>
{script}
</body>
</html>"""
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w").write(html)
    return path

AFF = '<div class="note"><i>Some links on this page may be affiliate links. If you buy through them we may earn a small commission at no extra cost to you.</i></div>'
EST = '<div class="note"><b>Heads up:</b> Rockstar has not released official GTA 6 PC system requirements yet. Everything below is an estimate based on how demanding current open-world games are. We will update this page the day official specs drop.</div>'

LASTMOD = {}

def article(slug, title, desc, h1, intro, sections, faq, updated=TODAY):
    body = f'<article class="post"><p class="crumbs"><a href="/guides/">Guides</a> / {h1}</p><span class="tag s">Updated {updated}</span><h1 class="ph">{h1}</h1><p class="lead">{intro}</p>{EST}'
    for h, txt in sections:
        body += f"<h2>{h}</h2>{txt}"
    body += "<h2>FAQ</h2>"
    for q, a in faq:
        body += f'<div class="card faq"><h3>{q}</h3><p>{a}</p></div>'
    body += '<div class="cta card"><h3>Not sure about your PC?</h3><p>Try our quick checker. Pick your graphics card and get an instant estimate.</p><a class="btn" href="/will-it-run.html">Will my PC run GTA 6? →</a></div></article>'
    page(f"guides/{slug}.html", title, desc, body, "/guides/")
    LASTMOD[f"guides/{slug}.html"] = updated
    return (slug, h1, desc)

ARTICLES = []

ARTICLES.append(article(
 "gta-6-pc-release-date",
 "When Is GTA 6 Coming to PC? Release Date Status (Nov 2026)",
 "GTA 6 is out on PS5 and Xbox, but not PC. Here is what Rockstar has actually said, what the rumors claim, and what past Rockstar ports suggest.",
 "When is GTA 6 coming to PC?",
 "GTA 6 launched on PS5 and Xbox Series X|S on November 19, 2026. PC players are still waiting. Here's what's confirmed, what's rumored, and what history tells us.",
 [("What's confirmed", "<p>Rockstar has said a PC version is planned, but it has <b>not</b> announced a date or even a release window. The official GTA 6 site lists only PlayStation 5 and Xbox Series X|S.</p>"),
  ("What the rumors say", "<p>Some reports claim the PC version is aimed at early 2027. Others expect late 2027 or even 2028. None of these come from Rockstar, so treat them as guesses until there's an announcement.</p>"),
  ("What past Rockstar games suggest", "<p>Rockstar has always released on console first:</p><table><tr><th>Game</th><th>Console</th><th>PC</th><th>Gap</th></tr><tr><td>GTA IV</td><td>Apr 2008</td><td>Dec 2008</td><td>~8 months</td></tr><tr><td>GTA V</td><td>Sep 2013</td><td>Apr 2015</td><td>~19 months</td></tr><tr><td>Red Dead Redemption 2</td><td>Oct 2018</td><td>Nov 2019</td><td>~13 months</td></tr></table><p>If GTA 6 follows that pattern, a realistic window is <b>somewhere between mid-2027 and mid-2028</b>.</p>"),
  ("What to do while you wait", "<p>This is the best time to plan an upgrade. Prices on current parts tend to drop over the next year, and you'll have time to watch for deals. Start with our <a href=\"/builds.html\">budget build tiers</a> and the <a href=\"/will-it-run.html\">Will It Run checker</a>.</p>")],
 [("Is GTA 6 on PC at launch?", "No. It launched on PS5 and Xbox Series X|S only."),
  ("Has Rockstar confirmed a PC version?", "Rockstar has said a PC version is planned but has not given a date."),
  ("Can I play GTA 6 on PC with cloud gaming?", "Only if a cloud service officially adds it. As of now, nothing has been announced for PC.")]))

ARTICLES.append(article(
 "gta-6-rtx-3060",
 "Can an RTX 3060 Run GTA 6 on PC? (Estimated Settings & FPS)",
 "Will the RTX 3060 handle GTA 6 on PC? Our estimate of the settings, resolution and frame rate to expect, plus how to squeeze out more FPS.",
 "Can an RTX 3060 run GTA 6?",
 "The RTX 3060 is one of the most popular graphics cards on Steam, so this is one of the biggest questions for PC players. Short answer: probably yes, at 1080p with sensible settings.",
 [("Our estimate", "<p>We expect the RTX 3060 to run GTA 6 at <b>1080p on low to medium settings</b>, likely with DLSS upscaling turned on, targeting 30–60 FPS. Expect to keep ray tracing off.</p>"),
  ("Why it should hold up", "<p>The <b>12 GB version</b> of the RTX 3060 has more video memory (VRAM) than many newer budget cards. Big open-world games eat VRAM for textures, so that 12 GB is a real advantage. It also supports DLSS, which can add a lot of FPS.</p>"),
  ("Watch out: the 8 GB version", "<p>There's also an RTX 3060 with only 8 GB of VRAM. If that's yours, expect to drop texture quality further. Check your card in Windows: open Task Manager → Performance → GPU and look at \"Dedicated GPU memory.\"</p>"),
  ("Settings to try first", "<ul class=\"c\"><li>DLSS on Quality or Balanced</li><li>Shadows: medium or low</li><li>Volumetrics / fog: low</li><li>Ray tracing: off</li><li>Textures: high on 12 GB, medium on 8 GB</li></ul>"),
  ("Should you upgrade?", "<p>Not yet. Wait for official specs. If you do need more, the next real step up is a 16 GB card like the RTX 5060 Ti 16GB or RX 9060 XT 16GB. See our <a href=\"/builds.html\">builds page</a>.</p>")],
 [("Will the RTX 3060 run GTA 6 at 1440p?", "Probably only on low settings with aggressive upscaling. 1080p is the realistic target."),
  ("Is the RTX 3060 still worth buying for GTA 6?", "A used 12 GB model can be good value for a budget build. New, a current 16 GB card is usually the smarter buy.")]))

ARTICLES.append(article(
 "gta-6-16gb-ram",
 "Is 16GB RAM Enough for GTA 6 on PC?",
 "Will 16GB of RAM be enough for GTA 6 on PC, or do you need 32GB? Our estimate and what we'd buy today.",
 "Is 16GB of RAM enough for GTA 6?",
 "RAM is one of the cheapest upgrades you can make, so it's worth getting right. Here's our take on 8, 16 and 32 GB for GTA 6.",
 [("Our estimate", "<p><b>16 GB should be the realistic minimum, and 32 GB is the comfortable choice.</b> Many recent open-world games already list 16 GB as their minimum and recommend more for high settings.</p>"),
  ("8 GB", "<p>We'd expect 8 GB to struggle badly, with stuttering and long load times. If you're on 8 GB, upgrading RAM is one of the best-value moves you can make.</p>"),
  ("16 GB", "<p>Should be playable, especially if you close background apps like browsers and Discord while playing. Make sure it's running in <b>dual channel</b> (two sticks, not one).</p>"),
  ("32 GB", "<p>Gives you headroom for streaming, mods and background apps. If you're buying RAM now, 32 GB (2×16 GB) is the sweet spot.</p>"),
  ("Quick checks", "<ul class=\"c\"><li>See your RAM: Task Manager → Performance → Memory</li><li>Make sure XMP/EXPO is turned on in your BIOS so RAM runs at its rated speed</li><li>Match your type: DDR4 boards need DDR4, DDR5 boards need DDR5</li></ul>")],
 [("Does faster RAM matter?", "A bit, especially on AMD Ryzen CPUs. But having enough RAM matters much more than speed."),
  ("DDR4 or DDR5?", "Whatever your motherboard supports. You can't mix them.")]))

ARTICLES.append(article(
 "gta-6-gtx-1660",
 "Will GTA 6 Run on a GTX 1660? (Honest Answer)",
 "Can a GTX 1660, 1660 Super or 1660 Ti run GTA 6 on PC? Our honest estimate and the cheapest upgrade paths.",
 "Will GTA 6 run on a GTX 1660?",
 "The GTX 1660 family was a budget hero for years. For GTA 6, though, we think it's going to fall short.",
 [("Our estimate", "<p>We expect the GTX 1660, 1660 Super and 1660 Ti to be <b>below what GTA 6 needs</b> for a good experience. It may launch on the lowest settings, but we wouldn't count on smooth gameplay.</p>"),
  ("Why", "<ul class=\"c\"><li>Only <b>6 GB of VRAM</b>. Big modern open-world games want more.</li><li>No DLSS support (it's not an RTX card), though AMD's FSR may still help.</li><li>No hardware ray tracing.</li></ul>"),
  ("Cheapest upgrade paths", "<p>If you only upgrade your graphics card, look at a used RTX 3060 12GB or a new RX 7600 for the tightest budget, or a 16 GB card like the RTX 5060 Ti 16GB / RX 9060 XT 16GB for more headroom. Check that your power supply can handle the new card. See <a href=\"/builds.html\">our build tiers</a>.</p>")],
 [("Should I upgrade now or wait?", "Wait until official specs are out unless you find a great deal. Prices generally drop over time."),
  ("Will FSR save my 1660?", "Upscaling helps, but it can't fix the VRAM limit.")]))

ARTICLES.append(article(
 "gta-6-gaming-laptop",
 "Can You Play GTA 6 on a Gaming Laptop? What You'll Need",
 "Planning to play GTA 6 on a laptop? What specs to look for, what to avoid, and how to get the most performance out of a gaming laptop.",
 "Can you play GTA 6 on a gaming laptop?",
 "Yes, if it's the right laptop. Gaming laptops can run demanding games, but the same GPU name can perform very differently from one laptop to the next.",
 [("What to look for (estimated)", "<ul class=\"c\"><li><b>GPU:</b> RTX 4060 laptop or better. An RTX 5060 or 5070 laptop GPU is a safer bet.</li><li><b>RAM:</b> 16 GB minimum, 32 GB preferred</li><li><b>Storage:</b> 1 TB SSD (big games take a lot of space)</li><li><b>Cooling:</b> check reviews. A hot laptop throttles and loses FPS.</li></ul>"),
  ("The laptop GPU catch", "<p>Laptop GPUs run at different power limits (called TGP). A high-wattage RTX 4060 laptop can beat a low-wattage RTX 4070 laptop. Always check the TGP in reviews before buying.</p>"),
  ("Avoid", "<ul class=\"c\"><li>Laptops with only integrated graphics</li><li>Thin-and-light models with low-power GPUs</li><li>8 GB of RAM that can't be upgraded</li></ul>"),
  ("Get more FPS from a laptop", "<ul class=\"c\"><li>Always play plugged in</li><li>Use the laptop's performance mode</li><li>Use a cooling pad and keep vents clear</li><li>Turn on DLSS or FSR</li></ul>")],
 [("Is a laptop or desktop better for GTA 6?", "For the same money, a desktop is usually faster and easier to upgrade. A laptop wins if you need portability."),
  ("Will GTA 6 run on a MacBook?", "Rockstar hasn't announced a Mac version.")]))

ARTICLES.append(article(
 "gta-6-rx-6600",
 "Can an RX 6600 Run GTA 6 on PC? (Estimated Settings & FPS)",
 "Will AMD's Radeon RX 6600 handle GTA 6 on PC? Our honest estimate of the settings to expect, how much its 8 GB of VRAM matters, and when to upgrade.",
 "Can an RX 6600 run GTA 6?",
 "The Radeon RX 6600 has been one of the best-value budget cards for years, so plenty of PC players are wondering if it will be enough for GTA 6. Our short answer: it should be playable at 1080p on low settings with upscaling, but it will be tight.",
 [("Our estimate", "<p>We expect the RX 6600 to run GTA 6 at <b>1080p on low settings, with upscaling (FSR) turned on</b>, likely aiming for around 30 FPS rather than a locked 60. Ray tracing should stay off. That puts it in the \"Maybe, on low\" tier of our <a href=\"/will-it-run.html\">Will It Run checker</a>, alongside the RTX 2060 and RTX 3050.</p><p>This is an estimate. Rockstar hasn't published PC requirements, and the real numbers could land higher or lower.</p>"),
  ("The 8 GB VRAM question", "<p>The RX 6600 has <b>8 GB of GDDR6 video memory</b>. That's enough for most games at 1080p, but large modern open-world games increasingly push past it on high texture settings. When a game runs out of VRAM you usually see stutter and blurry textures popping in, not just a lower frame rate.</p><p>Plan on <b>medium (or lower) textures</b>. If you want to check how much VRAM your card has, open Task Manager → Performance → GPU and look at \"Dedicated GPU memory.\" For more on this, compare with our <a href=\"/guides/gta-6-rtx-3060.html\">RTX 3060 guide</a>: the 12 GB version of that card has more room for textures.</p>"),
  ("Upscaling: FSR, not DLSS", "<p>As an AMD card, the RX 6600 can't use NVIDIA's DLSS. It can use AMD's <b>FSR</b>, and Intel's <b>XeSS</b> also runs on non-Intel cards, if the PC version supports them. AMD has also said it is bringing FSR 4 to older Radeon cards, so check AMD's driver release notes for the current status. Upscaling will likely be the single biggest FPS boost available to RX 6600 owners.</p>"),
  ("Settings to try first", "<ul class=\"c\"><li>Resolution: 1080p</li><li>Upscaling: FSR on Quality or Balanced</li><li>Textures: medium</li><li>Shadows and volumetrics/fog: low</li><li>Ray tracing: off</li><li>Cap the frame rate (for example 30 or 45) for smoother, more consistent gameplay</li></ul><p>Our <a href=\"/settings.html\">settings page</a> covers what to turn down first in more detail.</p>"),
  ("Older motherboard? One more thing", "<p>The RX 6600 connects using <b>PCIe 4.0 x8</b> (eight lanes instead of the usual sixteen). On older PCIe 3.0 motherboards that halves the available bandwidth, which can hurt a little more when a game runs short on VRAM. It's not a reason to panic, but it's another reason to keep texture settings sensible.</p>")],
 [("Should I upgrade my RX 6600 before GTA 6 comes to PC?", "Not yet. Wait for official specs. If you do upgrade, a 16 GB card like the RX 9060 XT 16GB or RTX 5060 Ti 16GB is a meaningful step up. See our <a href=\"/builds.html\">budget builds</a>."),
  ("Is the RX 6600 XT much better for GTA 6?", "It's faster, but it also has 8 GB of VRAM, so the same texture limits apply. Expect similar settings with a bit more FPS."),
  ("Will the RX 6600 run GTA 6 at 1440p?", "We wouldn't count on it. 1080p with upscaling is the realistic target.")],
 updated="2026-11-20"))

ARTICLES.append(article(
 "gta-6-ssd-vs-hdd",
 "Will GTA 6 Need an SSD on PC? SSD vs HDD Explained",
 "Can you play GTA 6 on PC from a hard drive, or will you need an SSD? Our estimate, why it matters for open-world games, and SATA vs NVMe explained.",
 "Will GTA 6 need an SSD on PC?",
 "Storage is easy to forget when you're planning a GTA 6 upgrade, but it could matter more than you'd think. Our take: plan on installing GTA 6 on an SSD. A hard drive (HDD) may not cut it.",
 [("Our estimate", "<p>We expect an <b>SSD to be strongly recommended, and possibly required</b>, for GTA 6 on PC. Rockstar hasn't confirmed this, but there are good reasons to expect it:</p><ul class=\"c\"><li>GTA 6 was built for PS5 and Xbox Series X|S, which both have fast SSDs built in.</li><li>A number of recent big PC releases already list an SSD in their minimum or recommended requirements.</li><li>Open-world games stream the map off your drive constantly as you move through it.</li></ul>"),
  ("Why a hard drive struggles", "<p>A hard drive reads data from a spinning disk, which is much slower than an SSD, especially when a game needs lots of small pieces of data quickly. In open-world games that can mean long loading screens, textures and buildings popping in late, and stutters when you drive or fly fast. Even if the game launches from an HDD, it's likely to be the worst version of the experience.</p>"),
  ("SATA SSD vs NVMe SSD", "<p>There are two common types of SSD:</p><table><tr><th>Type</th><th>Connects via</th><th>Typical max speed</th></tr><tr><td>SATA SSD</td><td>SATA cable (2.5\" drive)</td><td>~550 MB/s</td></tr><tr><td>NVMe SSD (PCIe 3.0)</td><td>M.2 slot</td><td>~3,500 MB/s</td></tr><tr><td>NVMe SSD (PCIe 4.0)</td><td>M.2 slot</td><td>up to ~7,000 MB/s</td></tr></table><p>Any SSD is a huge jump from a hard drive. A <b>SATA SSD is a fine budget option</b>, especially for older PCs without an M.2 slot. If your motherboard has a free M.2 slot, an NVMe drive is usually the better buy and leaves room for faster loading in future games.</p>"),
  ("How much space to plan for", "<p>Rockstar hasn't said how big the PC install will be. Modern open-world games regularly take 100 GB or more, so we'd plan on a <b>1 TB SSD</b> if you're buying one, rather than trying to squeeze GTA 6 onto a nearly full 500 GB drive. A big hard drive is still fine for storing videos, screenshots and older games.</p>"),
  ("Quick checks", "<ul class=\"c\"><li>See what drives you have: Task Manager → Performance. Each disk is labeled SSD or HDD.</li><li>Check your motherboard manual for free M.2 slots and whether they're PCIe 3.0 or 4.0.</li><li>Install the game on the SSD, not just Windows.</li></ul><p>An SSD fits well into any of our <a href=\"/builds.html\">budget build tiers</a>, and it pairs nicely with a RAM upgrade (see <a href=\"/guides/gta-6-16gb-ram.html\">Is 16GB RAM enough?</a>).</p>")],
 [("Will GTA 6 run on a hard drive at all?", "We don't know yet. Rockstar hasn't released PC requirements. Even if it does run, expect longer loads and more stutter."),
  ("Do I need a PCIe 4.0 NVMe drive?", "Probably not for a good experience. Any SSD should be a big improvement over a hard drive; faster NVMe drives mostly help with load times."),
  ("Can I use an external SSD?", "A fast external SSD over USB can work for many games, but an internal SSD is the safer bet for performance and reliability.")],
 updated="2026-11-20"))

# Guides index
gi = '<h1 class="ph">GTA 6 PC Guides</h1><p class="lead">Honest, budget-focused guides for running GTA 6 on PC. Everything is labeled as estimated until official specs are out.</p><div class="grid">'
for slug, h1, desc in ARTICLES:
    gi += f'<a class="card link" href="/guides/{slug}.html"><h3>{h1}</h3><p>{desc}</p></a>'
gi += "</div>"
page("guides/index.html", "GTA 6 PC Guides | LowSpecLeonida", "Budget-focused GTA 6 PC guides: release date, GPU and RAM questions, laptops and more.", gi, "/guides/")

# Home
latest = "".join(f'<a class="card link" href="/guides/{s}.html"><h3>{h}</h3><p>{d}</p></a>' for s, h, d in ARTICLES[:3])
home = f'''<div class="hero"><span class="tag p">PC version: date not announced yet</span>
<h1>Play GTA 6 on PC<br><em>without going broke.</em></h1>
<p class="lead">Budget builds, upgrade paths and settings guides for anyone who wants Vice City on a normal-person budget. We'll update everything the minute official PC specs drop.</p>
<a class="btn" href="/will-it-run.html">Will my PC run it?</a><a class="btn alt" href="/builds.html">See budget builds</a></div>
<h2>Where things stand</h2><div class="grid">
<div class="card"><span class="tag">Out now</span><h3>Consoles</h3><p>GTA 6 launched on PS5 and Xbox Series X|S on November 19, 2026.</p></div>
<div class="card"><span class="tag s">Waiting</span><h3>PC release</h3><p>Rockstar has said a PC version is planned but hasn't given a date. <a href="/guides/gta-6-pc-release-date.html">Full breakdown →</a></p></div>
<div class="card"><span class="tag p">Unknown</span><h3>Official specs</h3><p>No official PC requirements yet. Our tiers are estimates and clearly labeled.</p></div></div>
<h2>Latest guides</h2><div class="grid">{latest}</div>
<p style="margin-top:16px"><a href="/guides/">All guides →</a></p>'''
page("index.html", "LowSpecLeonida — Run GTA 6 on a Budget PC", "Budget PC builds, performance settings and (after launch) the best mods for running GTA 6 on PC without spending a fortune.", home)

# Will it run
wir = '''<h1 class="ph">Will my PC run GTA 6?</h1>''' + EST + '''
<div class="tool"><label>Your graphics card (GPU)</label><select id="gpu">
<option value="0">GTX 1060 / RX 580 or older</option><option value="1">GTX 1660 / RX 5600 XT</option>
<option value="2">RTX 2060 / RTX 3050 / RX 6600</option><option value="3" selected>RTX 3060 / RTX 4060 / RX 7600</option>
<option value="4">RTX 3070 / RTX 4060 Ti / RTX 5060 / RX 9060 XT</option><option value="5">RTX 4070 / RTX 5070 / RX 7800 XT / RX 9070</option>
<option value="6">RTX 4080 / 5080 / 4090 / 5090 / RX 7900 XTX</option></select>
<label>Your system memory (RAM)</label><select id="ram"><option value="0">8 GB</option><option value="1" selected>16 GB</option><option value="2">32 GB or more</option></select>
<button onclick="check()">Check my PC</button></div><div id="verdict"></div>
<h2>Related guides</h2><ul class="c"><li><a href="/guides/gta-6-rtx-3060.html">Can an RTX 3060 run GTA 6?</a></li><li><a href="/guides/gta-6-gtx-1660.html">Will GTA 6 run on a GTX 1660?</a></li><li><a href="/guides/gta-6-16gb-ram.html">Is 16GB RAM enough?</a></li><li><a href="/guides/gta-6-rx-6600.html">Can an RX 6600 run GTA 6?</a></li><li><a href="/guides/gta-6-ssd-vs-hdd.html">Will GTA 6 need an SSD?</a></li></ul>'''
script = '''<script>
function check(){const g=+document.getElementById('gpu').value,r=+document.getElementById('ram').value;let t,c,m;
if(g<=1){t='Probably not';c='p';m='Your GPU is likely below what GTA 6 will need. A GPU upgrade is the move.'}
else if(g===2){t='Maybe, on low';c='s';m='Possible at 1080p low with upscaling, but it will be tight.'}
else if(g===3){t='Likely, low–medium';c='s';m='Should be playable at 1080p low–medium with upscaling (estimate).'}
else if(g===4){t='Likely, medium–high';c='';m='Good shape for 1080p high / 1440p medium (estimate).'}
else if(g===5){t='Yes, high';c='';m='Should handle 1440p high comfortably (estimate).'}
else{t='Yes, maxed-ish';c='';m='Top-tier card. Expect high to ultra settings (estimate).'}
if(r===0)m+=' <b>Note:</b> 8 GB RAM will likely be a bottleneck. Upgrade to 16 GB+.';
document.getElementById('verdict').innerHTML='<div class="card"><span class="tag '+c+'">Estimate</span><h3>'+t+'</h3><p>'+m+'</p><p style="margin-top:10px"><a href="/builds.html">See upgrade options →</a></p></div>'}
</script>'''
page("will-it-run.html", "Will My PC Run GTA 6? Free Checker (Estimate) | LowSpecLeonida", "Pick your graphics card and RAM to get an instant estimate of how GTA 6 will run on your PC.", wir, "/will-it-run.html", script)

# Builds
src = open(os.path.join(ROOT, "build", "source-v1.html")).read()
def grab(id_):
    m = re.search(r'<section class="page" id="p-%s">(.*?)</section>' % id_, src, re.S)
    return m.group(1)
b = grab("builds").replace("<h2>Budget builds for GTA 6</h2>", '<h1 class="ph">Budget PC builds for GTA 6</h1>')
page("builds.html", "Best Budget PC Builds for GTA 6 (3 Tiers) | LowSpecLeonida", "Three budget PC build tiers for GTA 6 on PC, plus the single upgrade that matters most.", b, "/builds.html")
s = grab("settings").replace("<h2>Best settings for FPS</h2>", '<h1 class="ph">Best GTA 6 PC settings for FPS</h1>')
page("settings.html", "Best GTA 6 PC Settings for FPS | LowSpecLeonida", "What to turn down first for more FPS in GTA 6 on PC. Full tested guide goes live at PC launch.", s, "/settings.html")
mo = grab("mods").replace("<h2>GTA 6 PC mods</h2>", '<h1 class="ph">GTA 6 PC mods</h1>')
page("mods.html", "GTA 6 PC Mods (Coming at PC Launch) | LowSpecLeonida", "Our GTA 6 PC mods list goes live when the PC version launches: performance, graphics and install guides.", mo, "/mods.html")
ab = grab("about").replace("<h2>About LowSpecLeonida</h2>", '<h1 class="ph">About LowSpecLeonida</h1>')
page("about.html", "About | LowSpecLeonida", "About LowSpecLeonida, an unofficial fan site for running GTA 6 on budget PCs.", ab)
pr = grab("privacy").replace("<h2>Privacy Policy</h2>", '<h1 class="ph">Privacy Policy</h1>')
page("privacy.html", "Privacy Policy | LowSpecLeonida", "Privacy policy for LowSpecLeonida.", pr)

# sitemap + robots + 404
urls = ["", "will-it-run.html", "builds.html", "settings.html", "mods.html", "guides/", "about.html", "privacy.html"] + [f"guides/{a[0]}.html" for a in ARTICLES]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{DOMAIN}/{u}</loc><lastmod>{LASTMOD.get(u, TODAY)}</lastmod></url>\n" for u in urls) + "</urlset>\n"
open(OUT + "/sitemap.xml", "w").write(sm)
open(OUT + "/robots.txt", "w").write(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
page("404.html", "Page not found | LowSpecLeonida", "Page not found.", '<h1 class="ph">Page not found</h1><p class="lead">That page took a wrong turn in Vice City.</p><a class="btn" href="/">Back home</a>')
print("built", len(urls), "urls")
