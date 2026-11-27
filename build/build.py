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

ARTICLES.append(article(
 "gta-6-rtx-4060",
 "Is the RTX 4060 Good for GTA 6 on PC? (Estimated Settings & FPS)",
 "Will an RTX 4060 run GTA 6 on PC? Our honest estimate of the settings to expect, how much its 8 GB of VRAM matters, and how DLSS and frame generation could help.",
 "Is the RTX 4060 good for GTA 6?",
 "The RTX 4060 is one of the most common graphics cards in budget gaming PCs and prebuilts from the last few years, so a lot of PC players will be wondering if it's enough for GTA 6. Our short answer: it should be playable at 1080p with DLSS, but its 8 GB of VRAM means you'll need to be sensible with textures.",
 [("Our estimate", "<p>We expect the RTX 4060 to run GTA 6 at <b>1080p on low to medium settings with DLSS upscaling on</b>, aiming for 30–60 FPS depending on the scene. Ray tracing will most likely need to stay off or very low. That puts it in the same \"Likely, low–medium\" tier as the RTX 3060 in our <a href=\"/will-it-run.html\">Will It Run checker</a>.</p><p>This is an estimate. Rockstar hasn't published PC requirements, and the real picture could be better or worse.</p>"),
  ("The 8 GB VRAM catch", "<p>The desktop RTX 4060 has <b>8 GB of GDDR6 video memory</b> on a 128-bit memory bus. In most games it's a bit faster than an RTX 3060, but the 12 GB version of the 3060 actually has more room for textures. Big modern open-world games increasingly want more than 8 GB on high texture settings, and running out of VRAM tends to cause stutter and blurry textures rather than just a lower frame rate.</p><p>Plan on <b>medium textures</b> to start, and only raise them if the game stays smooth. Our <a href=\"/guides/gta-6-rtx-3060.html\">RTX 3060 guide</a> and <a href=\"/guides/gta-6-rx-6600.html\">RX 6600 guide</a> cover the same VRAM trade-off from different angles.</p>"),
  ("DLSS and frame generation", "<p>This is where the RTX 4060 has an edge over older budget cards. It supports <b>DLSS upscaling</b>, and as an RTX 40-series card it also supports <b>DLSS Frame Generation</b>, if the PC version of GTA 6 includes it. (Multi Frame Generation is limited to RTX 50-series cards.)</p><p>Frame generation can make the game look much smoother, but it works best when your base frame rate is already decent, and it can add a little input lag. Think of it as a bonus on top of a playable setup, not a fix for a slow one. It also uses some extra VRAM, which matters on an 8 GB card.</p>"),
  ("Settings to try first", "<ul class=\"c\"><li>Resolution: 1080p</li><li>DLSS: Quality or Balanced</li><li>Textures: medium</li><li>Shadows and volumetrics/fog: low or medium</li><li>Ray tracing: off</li><li>Frame generation: try it once your base FPS is steady</li></ul><p>See our <a href=\"/settings.html\">settings page</a> for what to turn down first.</p>"),
  ("Older PC? Check the slot", "<p>The RTX 4060 uses <b>PCIe 4.0 x8</b>, so it only uses eight lanes. On an older PCIe 3.0 motherboard that halves the available bandwidth, which tends to hurt most when a game runs short on VRAM. Another reason to keep textures sensible.</p>")],
 [("Is the RTX 4060 better than the RTX 3060 for GTA 6?", "It's usually a bit faster and supports DLSS Frame Generation, but the 12 GB RTX 3060 has more VRAM for textures. We'd expect them to land in a similar tier."),
  ("Should I upgrade my RTX 4060 before GTA 6 comes to PC?", "Not yet. Wait for official specs. If you do upgrade later, a 16 GB card like the RTX 5060 Ti 16GB or RX 9060 XT 16GB is the meaningful step up. See our <a href=\"/builds.html\">budget builds</a>."),
  ("What about the RTX 4060 laptop GPU?", "Laptop versions also have 8 GB of VRAM but run at different power limits, so performance varies a lot between laptops. Our <a href=\"/guides/gta-6-gaming-laptop.html\">gaming laptop guide</a> explains what to check.")],
 updated="2026-11-23"))

ARTICLES.append(article(
 "gta-6-ryzen-5-3600",
 "Is a Ryzen 5 3600 Enough for GTA 6 on PC? (CPU Estimate)",
 "Can a Ryzen 5 3600 handle GTA 6 on PC, or will your CPU hold you back? Our honest estimate, why open-world games lean on the CPU, and the cheapest upgrade path on AM4.",
 "Is a Ryzen 5 3600 enough for GTA 6?",
 "The Ryzen 5 3600 was the go-to budget gaming CPU for years, and it's still in a huge number of PCs. With GTA 6 eventually heading to PC, it's fair to ask whether it can keep up. Our short answer: it will probably run the game, but it's likely to be the part that limits your frame rate, especially in busy city areas.",
 [("Our estimate", "<p>We expect a Ryzen 5 3600 to be <b>around the minimum you'd want</b> for GTA 6 on PC, likely fine for a 30–40 FPS-style experience but struggling to hold a steady 60 FPS in crowded areas. This is an estimate; Rockstar hasn't published PC requirements yet.</p>"),
  ("Why the CPU matters in GTA", "<p>Your graphics card draws the picture, but your CPU runs the world: traffic, pedestrians, physics and streaming in the map as you move. Dense open-world cities are some of the most CPU-heavy scenes in gaming. Lowering resolution or graphics settings helps your GPU, but it <b>doesn't do much for a CPU bottleneck</b>. If your FPS drops in busy streets no matter what settings you pick, the CPU is usually why.</p>"),
  ("How it compares to the consoles", "<p>GTA 6 was built for PS5 and Xbox Series X|S, which both use <b>8-core AMD Zen 2 CPUs</b>. The Ryzen 5 3600 is also Zen 2, but with <b>6 cores and 12 threads</b>. It runs at higher clock speeds than the console chips, but it has fewer cores, and PC versions often add extra overhead. That's why we think it lands at the edge rather than comfortably above.</p>"),
  ("The cheap upgrade path: stay on AM4", "<p>The good news is you probably don't need a new motherboard. The Ryzen 5 3600 uses the <b>AM4 socket</b>, and many AM4 boards also support Ryzen 5000-series CPUs like the Ryzen 5 5600, Ryzen 7 5700X or Ryzen 7 5700X3D, which are meaningfully faster for gaming. The Ryzen 5 5600 is the CPU in our Tier 1 <a href=\"/builds.html\">budget build</a>.</p><ul class=\"c\"><li>Check your motherboard's CPU support list on the manufacturer's website.</li><li><b>Update the BIOS before swapping the CPU.</b> Older boards often need it to recognize Ryzen 5000 chips.</li><li>Your existing DDR4 RAM and cooler will usually carry over.</li></ul>"),
  ("Help it out in the meantime", "<ul class=\"c\"><li>Make sure your RAM is in dual channel with XMP turned on (see <a href=\"/guides/gta-6-16gb-ram.html\">Is 16GB RAM enough?</a>).</li><li>Close browsers and other background apps while playing.</li><li>Install the game on an SSD to reduce streaming stutter (see <a href=\"/guides/gta-6-ssd-vs-hdd.html\">SSD vs HDD</a>).</li><li>Lower crowd/traffic density and draw distance settings if the PC version offers them.</li><li>Cap your frame rate for a steadier feel.</li></ul>")],
 [("Should I upgrade my Ryzen 5 3600 now?", "Not urgently. Wait for official specs. If you see a good deal on a Ryzen 5000 CPU that your board supports, it's one of the best-value upgrades for an AM4 PC."),
  ("Is the Ryzen 5 3600X much better?", "Only slightly. It's the same 6-core Zen 2 design with a bit higher clock speed, so expect a similar experience."),
  ("Will an upscaler like DLSS or FSR help a CPU bottleneck?", "Not much. Upscaling mainly reduces GPU load. It helps if your graphics card is the limit, not your CPU.")],
 updated="2026-11-23"))

ARTICLES.append(article(
 "gta-6-8gb-vram",
 "Is 8GB of VRAM Enough for GTA 6 on PC? (Honest Estimate)",
 "Will an 8 GB graphics card be enough for GTA 6 on PC? What VRAM does, what running out looks like, which settings use the most, and whether to buy 12 or 16 GB.",
 "Is 8GB of VRAM enough for GTA 6?",
 "A huge number of budget and mid-range graphics cards have 8 GB of video memory (VRAM): the RTX 4060, RTX 3060 Ti, RX 6600, RX 7600 and more. So whether 8 GB is enough is one of the most important questions for GTA 6 on PC. Our short answer: it should be playable at 1080p, but 8 GB is likely to be the thing that decides your texture setting.",
 [("Our estimate", "<p>We expect <b>8 GB of VRAM to be workable at 1080p with medium textures</b>, plus upscaling (DLSS, FSR or XeSS). High or ultra textures, 1440p and ray tracing are where 8 GB is most likely to run out. We'd treat <b>12 GB as comfortable for 1080p and 16 GB as the safe choice</b> if you're buying a card now.</p><p>This is an estimate. Rockstar hasn't published PC requirements, and the real number could be higher or lower.</p>"),
  ("What VRAM actually does", "<p>VRAM is the graphics card's own memory. It holds textures, models, shadows and other data the GPU needs right now. Open-world games like GTA keep streaming new areas in as you move, so they tend to need a lot of it. VRAM is separate from your system RAM (see <a href=\"/guides/gta-6-16gb-ram.html\">Is 16GB RAM enough?</a>), and adding more system RAM doesn't add VRAM.</p>"),
  ("What running out looks like", "<p>Running low on VRAM usually doesn't just lower your average FPS. Instead you tend to see:</p><ul class=\"c\"><li>Sudden stutters and hitches, especially when driving fast</li><li>Blurry textures that load in late or never sharpen</li><li>Performance that gets worse the longer you play</li></ul><p>If you see these, lower texture quality first. It's the setting with the biggest effect on VRAM, and it often makes the biggest difference on an 8 GB card.</p>"),
  ("Settings that use the most VRAM", "<ul class=\"c\"><li><b>Texture quality</b>: the biggest one. Start at medium.</li><li><b>Resolution</b>: 1440p and 4K use more than 1080p. Upscaling helps by rendering at a lower resolution.</li><li><b>Ray tracing</b>: adds extra data on top. Keep it off on 8 GB.</li><li><b>Frame generation</b>: also uses some VRAM, so leave a little headroom.</li><li><b>Shadow quality</b>: high settings can add up.</li></ul><p>Our <a href=\"/settings.html\">settings page</a> covers what to turn down first.</p>"),
  ("Check how much you have", "<p>Open Task Manager → Performance → GPU and look at <b>\"Dedicated GPU memory.\"</b> Some cards come in versions with different amounts, like the RTX 3060 (8 GB and 12 GB) or RTX 5060 Ti (8 GB and 16 GB), so check yours rather than going by the model name. Card-specific estimates are in our <a href=\"/guides/gta-6-rtx-4060.html\">RTX 4060</a>, <a href=\"/guides/gta-6-rx-6600.html\">RX 6600</a> and <a href=\"/guides/gta-6-rtx-3060.html\">RTX 3060</a> guides.</p>")],
 [("Should I upgrade my 8 GB card before GTA 6 comes to PC?", "Not yet. Wait for official specs. If you do upgrade, a 16 GB card like the RTX 5060 Ti 16GB or RX 9060 XT 16GB is the meaningful step. See our <a href=\"/builds.html\">budget builds</a>."),
  ("Is a 12 GB card worth it over 8 GB?", "For big open-world games, extra VRAM usually means you can run higher textures without stutter. Between two similar-speed cards, we'd pick the one with more VRAM."),
  ("Will upscaling fix an 8 GB limit?", "It helps, because the game renders at a lower resolution, but it doesn't remove the need to keep textures sensible.")],
 updated="2026-11-25"))

ARTICLES.append(article(
 "gta-6-intel-arc-b580",
 "Can the Intel Arc B580 Run GTA 6 on PC? (Estimated Settings)",
 "Will Intel's Arc B580 handle GTA 6 on PC? Our honest estimate, why its 12 GB of VRAM helps, XeSS 2 explained, and the Resizable BAR check you shouldn't skip.",
 "Can the Intel Arc B580 run GTA 6?",
 "Intel's Arc B580 became a popular budget pick thanks to its 12 GB of video memory, something rival cards in its class often lack. Our short answer: it should be a reasonable 1080p card for GTA 6 on PC, as long as your system is set up for it.",
 [("Our estimate", "<p>We expect the Arc B580 to run GTA 6 at <b>1080p on low to medium settings with upscaling on</b>, aiming for 30–60 FPS depending on the scene, with ray tracing off or very low. Launch reviews generally found it competitive with the RTX 4060, so we'd put it in the same \"Likely, low–medium\" tier as the RTX 3060 and RTX 4060 in our <a href=\"/will-it-run.html\">Will It Run checker</a>.</p><p>This is an estimate. Rockstar hasn't published PC requirements, and Intel driver support for any new game is something to check at launch.</p>"),
  ("12 GB of VRAM is the big plus", "<p>The B580 has <b>12 GB of GDDR6 on a 192-bit bus</b>. That's more than the 8 GB on cards like the RTX 4060 and RX 7600, and it gives you more room for texture quality in a big open-world game before stutter sets in. See <a href=\"/guides/gta-6-8gb-vram.html\">Is 8GB of VRAM enough?</a> for why that matters.</p>"),
  ("XeSS 2: upscaling and frame generation", "<p>The B580 can't use NVIDIA's DLSS. Instead it supports Intel's <b>XeSS 2</b>, which includes XeSS Super Resolution (upscaling), XeSS Frame Generation and Xe Low Latency. Whether GTA 6's PC version supports XeSS hasn't been announced. AMD's FSR also works on Intel cards if the game includes it, so you should have some upscaling option either way.</p>"),
  ("Don't skip: Resizable BAR", "<p>Intel recommends turning on <b>Resizable BAR</b> (AMD calls it Smart Access Memory) for good performance on Arc cards, and reviewers treat it as essential. Older PCs may have it off or not support it at all. Check before buying:</p><ul class=\"c\"><li>Look in your BIOS for \"Resizable BAR\" or \"Re-Size BAR Support\" and enable it (you may also need \"Above 4G Decoding\" on).</li><li>You may need a BIOS update on older boards.</li><li>Intel's Arc software can show whether it's active.</li></ul><p>The B580 also uses <b>PCIe 4.0 x8</b>, so on an older PCIe 3.0 board it gets half the bandwidth. If your PC is older, our <a href=\"/guides/gta-6-ryzen-5-3600.html\">Ryzen 5 3600 guide</a> covers CPU concerns too.</p>"),
  ("Settings to try first", "<ul class=\"c\"><li>Resolution: 1080p</li><li>Upscaling: XeSS (or FSR) on Quality or Balanced</li><li>Textures: medium to high (the 12 GB helps here)</li><li>Shadows and volumetrics/fog: low or medium</li><li>Ray tracing: off</li><li>Keep Intel graphics drivers up to date, especially around launch</li></ul>")],
 [("Is the Arc B580 better than the RTX 4060 for GTA 6?", "They should be in a similar tier. The B580 has more VRAM; the RTX 4060 has DLSS and NVIDIA's more established driver track record. Neither is a clear winner until we see the PC version."),
  ("Should I buy an Arc B580 for GTA 6 now?", "Wait for official specs if you can. If you do buy one, make sure your PC supports Resizable BAR first. Compare it against the options on our <a href=\"/builds.html\">builds page</a>."),
  ("What about the Arc B570?", "It's a cut-down version of the same chip with 10 GB of VRAM, so expect a similar setup with somewhat lower performance.")],
 updated="2026-11-25"))

ARTICLES.append(article(
 "gta-6-rtx-2060",
 "Can an RTX 2060 Run GTA 6 on PC? (Estimated Settings)",
 "Will an RTX 2060 handle GTA 6 on PC? Our honest estimate, why 6 GB of VRAM is the real limit, how DLSS helps, and when an upgrade makes sense.",
 "Can an RTX 2060 run GTA 6?",
 "The RTX 2060 was NVIDIA's entry ticket to ray tracing and DLSS back in 2019, and plenty of people are still gaming on one. With GTA 6 eventually coming to PC, it's a fair question whether it can keep up. Our short answer: maybe, at 1080p on low settings with DLSS on, but it will be tight, and its video memory is the main reason.",
 [("Our estimate", "<p>We put the RTX 2060 in the <b>\"Maybe, on low\"</b> tier of our <a href=\"/will-it-run.html\">Will It Run checker</a>, alongside the RTX 3050 and RX 6600. We'd expect it to be playable at <b>1080p, low settings, with DLSS on Performance or Balanced</b>, aiming for around 30 FPS-style play rather than a locked 60. Ray tracing should stay off.</p><p>This is an estimate. Rockstar hasn't published PC requirements, and the real picture could be better or worse.</p>"),
  ("6 GB of VRAM is the weak spot", "<p>The standard RTX 2060 has <b>6 GB of GDDR6</b>. That was fine in 2019, but large open-world games keep streaming new areas in as you move, and that eats video memory. When you run out, you usually get stutters and blurry textures rather than just a lower frame rate. On a 6 GB card, plan on <b>low or medium textures</b> and keep everything else that uses VRAM modest. Our <a href=\"/guides/gta-6-8gb-vram.html\">8GB VRAM guide</a> explains why memory matters so much, and 6 GB is a step below that.</p><p>Not every RTX 2060 is the same. NVIDIA also sold a <b>12 GB RTX 2060</b>, and the <b>RTX 2060 Super has 8 GB</b>. Check yours in Task Manager → Performance → GPU under \"Dedicated GPU memory.\"</p>"),
  ("DLSS is your best friend", "<p>Because it's an RTX card, the 2060 supports <b>DLSS Super Resolution</b>, which renders the game at a lower resolution and upscales it. That cuts GPU load and VRAM use, and it's the single biggest help for this card, assuming the PC version supports DLSS (not announced yet). What it <b>can't</b> use is NVIDIA's DLSS Frame Generation, which needs an RTX 40-series or newer card. If the game includes AMD's FSR frame generation, that can work on RTX 20-series cards, but frame generation feels best when you already have a decent base frame rate.</p>"),
  ("Settings to try first", "<ul class=\"c\"><li>Resolution: 1080p</li><li>DLSS: Balanced or Performance</li><li>Textures: low to medium (watch for stutter)</li><li>Shadows, volumetrics/fog and reflections: low</li><li>Ray tracing: off</li><li>Cap the frame rate at 30 or 40 for a steadier feel</li></ul><p>More on what to turn down first on our <a href=\"/settings.html\">settings page</a>. Installing the game on an SSD also helps with streaming hitches (see <a href=\"/guides/gta-6-ssd-vs-hdd.html\">SSD vs HDD</a>).</p>"),
  ("Upgrade or wait?", "<p>Wait for official specs before spending money. If you do end up upgrading, the jump that matters most for GTA 6 is to a card with <b>more VRAM</b>, ideally 12 or 16 GB. Our <a href=\"/builds.html\">budget builds page</a> lists options, and our <a href=\"/guides/gta-6-rtx-3060.html\">RTX 3060</a>, <a href=\"/guides/gta-6-rtx-4060.html\">RTX 4060</a> and <a href=\"/guides/gta-6-intel-arc-b580.html\">Arc B580</a> guides cover the cards one tier up.</p>")],
 [("Is the RTX 2060 better than a GTX 1660 for GTA 6?", "Yes, mainly because it supports DLSS and has dedicated ray tracing hardware the GTX 1660 lacks. See our <a href=\"/guides/gta-6-gtx-1660.html\">GTX 1660 guide</a>."),
  ("Will the RTX 2060 Super do better?", "Somewhat. It's faster and has 8 GB of VRAM instead of 6 GB, which gives more room for textures. Expect a similar low-to-medium experience with a bit more headroom."),
  ("Can I use ray tracing on an RTX 2060?", "It technically supports it, but in a game this demanding we'd leave it off and spend the performance on a steadier frame rate.")],
 updated="2026-11-27"))

ARTICLES.append(article(
 "gta-6-steam-deck",
 "Will GTA 6 Run on Steam Deck? (Honest Estimate)",
 "Can the Steam Deck run GTA 6 when it comes to PC? An honest look at the hardware, why anti-cheat may matter more than performance, and what about Windows handhelds.",
 "Will GTA 6 run on Steam Deck?",
 "Playing GTA 6 in bed or on a train is a tempting idea, and the Steam Deck is the handheld most people already own. Our short answer: we don't expect it to run well, and even whether it runs at all may depend on things that have nothing to do with performance.",
 [("Our estimate", "<p>We think the Steam Deck will be <b>well below what GTA 6 needs for a good experience</b>. Even if the game launches and runs, expect very low settings, heavy upscaling and frame rates that struggle in busy areas. We'd treat it as \"maybe, for curiosity\" rather than a way to actually play through the game.</p><p>This is an estimate. Rockstar hasn't published PC requirements or said anything about Steam Deck support.</p>"),
  ("Why the hardware is a stretch", "<p>The Steam Deck uses a custom AMD chip with a <b>4-core, 8-thread Zen 2 CPU</b> and an <b>RDNA 2 GPU with 8 compute units</b>, sharing <b>16 GB of LPDDR5</b> memory between the CPU and graphics. GTA 6 was built for PS5 and Xbox Series X|S, which have 8-core Zen 2 CPUs and much larger GPUs. Open-world cities lean hard on the CPU (see our <a href=\"/guides/gta-6-ryzen-5-3600.html\">Ryzen 5 3600 guide</a> for why), and half the cores of a console is a big gap. The Deck's low 1280×800 screen helps the GPU side, but it doesn't help the CPU.</p><p>The Steam Deck OLED has a more efficient chip and faster memory, but the same core counts, so we wouldn't expect a dramatically different result.</p>"),
  ("Anti-cheat may matter more than speed", "<p>The Steam Deck runs SteamOS, which is Linux-based and plays Windows games through Valve's Proton compatibility layer. That works well for many games, but not ones whose anti-cheat blocks Linux. There's a relevant precedent: when Rockstar added <b>BattlEye anti-cheat to GTA V in September 2024, GTA Online stopped working on Steam Deck and Linux</b>. Story mode remained playable. We don't know yet what GTA 6's PC version will use, so check Steam Deck compatibility reports at launch before buying for it.</p>"),
  ("What about Windows handhelds?", "<p>Handhelds that run Windows, like the ROG Ally or Legion Go, avoid the Linux question and some have stronger chips than the Steam Deck. They're still far smaller than a desktop graphics card, and they share memory between CPU and GPU, so we'd expect the same story: possible on minimum settings at best. If portability matters, a <a href=\"/guides/gta-6-gaming-laptop.html\">gaming laptop with a dedicated GPU</a> is a much safer bet.</p>"),
  ("A better option: stream from your PC", "<p>If you have a capable desktop, <b>Steam Remote Play</b> lets the PC do the work while the Steam Deck just displays the stream over your home network. Results depend on your Wi-Fi, but it sidesteps the hardware limits entirely. Not sure your desktop is up to it? Try our <a href=\"/will-it-run.html\">Will It Run checker</a> or see our <a href=\"/builds.html\">budget builds</a>.</p>")],
 [("Will Rockstar make GTA 6 Steam Deck Verified?", "Nothing has been announced. Valve's \"Verified\" ratings come from Valve's testing after a game is on Steam, so we'll know after the PC release."),
  ("Can I install Windows on my Steam Deck for GTA 6?", "You can install Windows on a Steam Deck, which can get around Linux anti-cheat blocks, but it won't make the hardware any faster."),
  ("Is the Steam Deck OLED better for GTA 6?", "A little, thanks to faster memory, but it has the same 4-core CPU and 8-CU GPU, so don't expect a big difference.")],
 updated="2026-11-27"))

# Guides index
gi = '<h1 class="ph">GTA 6 PC Guides</h1><p class="lead">Honest, budget-focused guides for running GTA 6 on PC. Everything is labeled as estimated until official specs are out.</p><div class="grid">'
for slug, h1, desc in ARTICLES:
    gi += f'<a class="card link" href="/guides/{slug}.html"><h3>{h1}</h3><p>{desc}</p></a>'
gi += "</div>"
page("guides/index.html", "GTA 6 PC Guides | LowSpecLeonida", "Budget-focused GTA 6 PC guides: release date, GPU and RAM questions, laptops and more.", gi, "/guides/")

# Home
latest = "".join(f'<a class="card link" href="/guides/{s}.html"><h3>{h}</h3><p>{d}</p></a>' for s, h, d in ARTICLES[::-1][:3])
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
<h2>Related guides</h2><ul class="c"><li><a href="/guides/gta-6-rtx-3060.html">Can an RTX 3060 run GTA 6?</a></li><li><a href="/guides/gta-6-gtx-1660.html">Will GTA 6 run on a GTX 1660?</a></li><li><a href="/guides/gta-6-16gb-ram.html">Is 16GB RAM enough?</a></li><li><a href="/guides/gta-6-rx-6600.html">Can an RX 6600 run GTA 6?</a></li><li><a href="/guides/gta-6-ssd-vs-hdd.html">Will GTA 6 need an SSD?</a></li><li><a href="/guides/gta-6-rtx-4060.html">Is the RTX 4060 good for GTA 6?</a></li><li><a href="/guides/gta-6-ryzen-5-3600.html">Is a Ryzen 5 3600 enough for GTA 6?</a></li><li><a href="/guides/gta-6-8gb-vram.html">Is 8GB of VRAM enough for GTA 6?</a></li><li><a href="/guides/gta-6-intel-arc-b580.html">Can the Intel Arc B580 run GTA 6?</a></li><li><a href="/guides/gta-6-rtx-2060.html">Can an RTX 2060 run GTA 6?</a></li><li><a href="/guides/gta-6-steam-deck.html">Will GTA 6 run on Steam Deck?</a></li></ul>'''
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
