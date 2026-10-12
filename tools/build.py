#!/usr/bin/env python3
"""Genera il sito statico in docs/ a partire da project/. Uso: python3 tools/build.py"""
import json, re, html, shutil, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "project"
OUT = ROOT / "docs"
tokens = json.loads((SRC / "tokens.json").read_text(encoding="utf-8"))
index = json.loads((SRC / "design-system.json").read_text(encoding="utf-8"))
esc = html.escape

def alias(v):
    m = re.fullmatch(r"\{([\w.-]+)\}", v.strip())
    return f"var(--{m.group(1)})" if m else v

# ---------- variabili CSS (chiaro e scuro) ----------
light, dark = [], []
for t in tokens["color"]["tokens"]:
    light.append(f"--{t['name']}:{alias(t['value']['light'])}")
    dark.append(f"--{t['name']}:{alias(t['value']['dark'])}")
for k, v in tokens["type"]["families"].items():
    light.append(f"--font-{k}:{v}")
for grp in ("spacing", "radius"):
    for t in tokens[grp]["tokens"]:
        light.append(f"--{t['name']}:{t['value']}")
for t in tokens["shadow"]["tokens"]:
    light.append(f"--{t['name']}:{t['value']['light']}")
    dark.append(f"--{t['name']}:{t['value']['dark']}")
VARS = (":root{" + ";".join(light) + "}\n"
        ":root[data-theme=dark]{color-scheme:dark;" + ";".join(dark) + "}")

# font locali: dichiarati in tokens.json (type.fonts), copiati in docs/fonts
def font_face(prefix):
    css = ""
    for f in tokens["type"].get("fonts", []):
        css += ("@font-face{font-family:\"%s\";src:url(\"%s%s\") format(\"truetype\");font-weight:%s;"
                "font-style:%s;font-display:swap}" % (f["family"], prefix, f["file"], f.get("weight", "400"), f.get("style", "normal")))
    return css

(OUT / "fonts").mkdir(parents=True, exist_ok=True)
for old in (OUT / "fonts").glob("*"):
    old.unlink()
for f in (SRC / "fonts").glob("*.ttf"):
    shutil.copy(f, OUT / "fonts" / f.name)

# loghi: copia i PNG nella pagina (esclude le misure 512 e 2048)
(OUT / "logos").mkdir(parents=True, exist_ok=True)
for old in (OUT / "logos").glob("*"):
    old.unlink()
logo_files = sorted(p for p in (SRC / "assets" / "Logos").glob("*.png")
                    if not re.search(r"-(512|2048)\.png$", p.name))
for p in logo_files:
    shutil.copy(p, OUT / "logos" / p.name)

THEME_JS = """<script>(function(){var d=document.documentElement;
function set(t){d.setAttribute('data-theme',t)}
var s=null;try{s=localStorage.getItem('ds-theme')}catch(e){}
set(s||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'));
addEventListener('message',function(e){if(e.data&&e.data.theme)set(e.data.theme)});})();</script>"""

# ---------- anteprime ----------
(OUT / "previews").mkdir(parents=True, exist_ok=True)
for old in (OUT / "previews").glob("*.html"):
    old.unlink()
components = []
for d in sorted((SRC / "components").iterdir()):
    pv = d / "preview.html"
    if not pv.exists():
        continue
    text = pv.read_text(encoding="utf-8")
    m = re.match(r"<!--\s*@dsCard\s*(.*?)-->", text)
    meta = dict(re.findall(r'(\w+)=(?:"([^"]*)"|(\d+))', m.group(1)) and
                [(a, b or c) for a, b, c in re.findall(r'(\w+)=(?:"([^"]*)"|(\d+))', m.group(1))]) if m else {}
    inject = f"<style id=\"ds-vars\">{font_face('../fonts/')}{VARS}</style>{THEME_JS}"
    text = re.sub(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com[^>]*>\n?', "", text)
    out = text.replace("</head>", inject + "</head>", 1)
    (OUT / "previews" / f"{d.name}.html").write_text(out, encoding="utf-8")
    readme = (d / "README.md").read_text(encoding="utf-8") if (d / "README.md").exists() else ""
    components.append({"name": d.name, "group": meta.get("group", "Copertina"),
                       "height": int(meta.get("height", 300)), "subtitle": meta.get("subtitle", ""),
                       "readme": readme})

order = ["Copertina", "Fondamenta", "Marchio", "Base", "Social", "Video", "Slide e pagine"]
groups = {}
for c in components:
    groups.setdefault(c["group"], []).append(c)
group_names = [g for g in order if g in groups] + [g for g in groups if g not in order]

# ---------- sezioni di testo ----------
docs = [("README", "Panoramica", (SRC / "README.md").read_text(encoding="utf-8"))]
for f in sorted(SRC.glob("0*.md")):
    first = f.read_text(encoding="utf-8").splitlines()[0].lstrip("# ").strip()
    docs.append((f.stem, first or f.stem, f.read_text(encoding="utf-8")))

# ---------- HTML dei token ----------
def usage(u):
    return esc(re.sub(r"`([^`]+)`", r"\1", u))

colors = ""
for t in tokens["color"]["tokens"]:
    lv, dv = t["value"]["light"], t["value"]["dark"]
    colors += (f'<div class="sw"><div class="chips"><i style="background:{alias(lv)}"></i>'
               f'<i class="d" style="background:{alias(dv)}"></i></div>'
               f'<b>{esc(t["name"])}</b><code>{esc(lv)}</code><code>{esc(dv)}</code>'
               f'<p>{usage(t["usage"])}</p></div>')

fams = tokens["type"]["families"]
fam_label = {k: v.split(",")[0].strip('"\' ') for k, v in fams.items()}
fam_role = {"display": "Titoli", "editorial": "Titoli grandi", "sans": "Testo", "mono": "Dati"}
type_html = '<div class="fams">'
for k, v in fams.items():
    nm = fam_label[k]
    type_html += (f'<div class="fam" style="font-family:var(--font-{k})"><small>{esc(fam_role.get(k,k))} · --font-{k}</small>'
                  f'<span class="big">{esc(nm)}</span>'
                  f'<span>Aa Bb Cc 0123 — Le email non aspettano.</span></div>')
type_html += "</div>"
for g in tokens["type"]["groups"]:
    type_html += f'<h3>{esc(g["name"])}</h3>'
    for s in g["styles"]:
        fam = s.get("family", g["family"])
        css = (f'font-family:var(--font-{fam});font-size:{s["fontSize"]};line-height:{s.get("lineHeight","1.2")};'
               f'font-weight:{s["fontWeight"]};letter-spacing:{s.get("letterSpacing","0")}')
        size = int(re.sub(r"\D", "", s["fontSize"]))
        scale = min(1, 56 / size) if size > 56 else 1
        type_html += (f'<div class="ts"><div class="meta"><b>{esc(s["name"])}</b>'
                      f'<code>{esc(fam_label[fam])} {s["fontWeight"]} · {esc(s["fontSize"])}/{esc(s.get("lineHeight","auto"))}</code>'
                      f'<p>{usage(s["usage"])}</p></div>'
                      f'<div class="sample" style="{css};font-size:{round(size*scale)}px;line-height:{round(size*scale*1.1)}px">{esc(s["sample"])}</div></div>')

space_html = ""
for t in tokens["spacing"]["tokens"]:
    space_html += (f'<div class="row"><code>{esc(t["name"])}</code><span class="bar" style="width:{t["value"]}"></span>'
                   f'<em>{esc(t["value"])}</em><p>{usage(t["usage"])}</p></div>')
radius_html = ""
for t in tokens["radius"]["tokens"]:
    radius_html += (f'<div class="rd"><span style="border-radius:{t["value"]}"></span><code>{esc(t["name"])}</code>'
                    f'<em>{esc(t["value"])}</em><p>{usage(t["usage"])}</p></div>')
shadow_html = ""
for t in tokens["shadow"]["tokens"]:
    shadow_html += (f'<div class="sh"><span style="box-shadow:var(--{t["name"]})"></span><code>{esc(t["name"])}</code>'
                    f'<p>{usage(t["usage"])}</p></div>')
if tokens["shadow"].get("note"):
    shadow_html += f'<p class="note">{esc(tokens["shadow"]["note"])}</p>'

# ---------- componenti ----------
def comp_block(c):
    return (f'<article class="comp" id="c-{c["name"]}"><header><h3>{esc(c["name"])}</h3>'
            f'<span>{esc(c["subtitle"])}</span></header>'
            f'<iframe class="pv" src="previews/{c["name"]}.html" title="{esc(c["name"])}" '
            f'style="height:{c["height"]}px" loading="lazy"></iframe>'
            f'<details><summary>Regole d\'uso</summary><div class="md" data-md="{esc(c["readme"])}"></div></details></article>')

comp_html = ""
nav_comp = ""
for g in group_names:
    comp_html += f'<h3 class="grp">{esc(g)}</h3>' + "".join(comp_block(c) for c in groups[g])
    nav_comp += "".join(f'<a href="#c-{c["name"]}">{esc(c["name"])}</a>' for c in groups[g])

doc_html = "".join(f'<section id="d-{i}"><h2>{esc(t)}</h2><div class="md" data-md="{esc(md)}"></div></section>' for i, t, md in docs)
nav_docs = "".join(f'<a href="#d-{i}">{esc(t)}</a>' for i, t, _ in docs)

def logo_block(p):
    n = p.name
    bg = "var(--ink)" if "fondo-scuro" in n else "var(--brand)" if "fondo-petrolio" in n else "var(--surface-raised)"
    return (f'<figure class="lg"><div style="background:{bg}"><img src="logos/{esc(n)}" alt="{esc(n)}" loading="lazy"></div>'
            f'<figcaption><code>{esc(n)}</code></figcaption></figure>')
logos_html = "".join(logo_block(p) for p in logo_files)

title = esc(index.get("title", tokens["name"]))
note = esc(index.get("lastChange", {}).get("note", ""))
PAGE = f"""<!doctype html>
<html lang="it" data-theme="light"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} — Design System</title>
<style>{font_face('fonts/')}{VARS}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--surface);color:var(--ink);font:400 16px/24px var(--font-sans)}}
code{{font:400 12px/18px var(--font-mono);color:var(--ink-muted)}}
a{{color:var(--brand-text)}}
.top{{position:sticky;top:0;z-index:5;display:flex;gap:16px;align-items:center;padding:12px 24px;background:var(--surface-raised);border-bottom:1px solid var(--line)}}
.top h1{{margin:0;font:700 18px/24px var(--font-display)}}
.top small{{color:var(--ink-muted);flex:1}}
.tg{{border:1px solid var(--line-strong);background:transparent;color:var(--ink);border-radius:999px;padding:6px 14px;font:600 12px var(--font-sans);cursor:pointer}}
.wrap{{display:grid;grid-template-columns:220px 1fr}}
nav{{position:sticky;top:49px;align-self:start;height:calc(100vh - 49px);overflow:auto;padding:16px;border-right:1px solid var(--line);font-size:14px}}
nav a{{display:block;padding:4px 0;text-decoration:none;color:var(--ink)}} nav a:hover{{color:var(--brand-text)}}
nav h4{{margin:16px 0 4px;font:700 11px/16px var(--font-sans);letter-spacing:.08em;text-transform:uppercase;color:var(--ink-muted)}}
main{{padding:24px 32px 96px;max-width:1100px}}
h2{{font:700 32px/36px var(--font-display);margin:64px 0 16px;letter-spacing:-.01em}} h2:first-child{{margin-top:0}}
h3{{font:600 20px/28px var(--font-display);margin:32px 0 8px}} h3.grp{{margin-top:40px;color:var(--brand-text)}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:16px}}
.sw{{background:var(--surface-raised);border:1px solid var(--line);border-radius:12px;padding:12px}}
.sw .chips{{display:flex;height:56px;border-radius:8px;overflow:hidden;border:1px solid var(--line)}} .sw .chips i{{flex:1}}
.sw b{{display:block;margin-top:8px}} .sw code{{display:inline-block;margin-right:8px}} .sw p,.ts p,.row p,.rd p,.sh p{{margin:4px 0 0;font-size:13px;line-height:18px;color:var(--ink-muted)}}
.fams{{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px}}
.fam{{display:flex;flex-direction:column;gap:6px;background:var(--surface-raised);border:1px solid var(--line);border-radius:12px;padding:16px}}
.fam small{{font:400 11px/16px var(--font-mono);color:var(--ink-muted)}} .fam .big{{font-size:32px;line-height:36px;color:var(--brand-text)}}
.ts{{display:grid;grid-template-columns:240px 1fr;gap:24px;align-items:center;padding:16px 0;border-bottom:1px solid var(--line)}}
.sample{{overflow-wrap:anywhere}}
.row{{display:grid;grid-template-columns:90px 160px 50px 1fr;gap:12px;align-items:center;padding:6px 0}} .row .bar{{height:16px;background:var(--brand);border-radius:4px;display:block}} .row p{{margin:0}}
.shapes{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:24px}}
.rd span{{display:block;width:96px;height:64px;background:var(--brand-soft);border:2px solid var(--brand)}}
.sh span{{display:block;width:140px;height:80px;background:var(--surface-raised);border-radius:12px;margin:8px 0 16px}}
.comp{{margin:16px 0 32px}} .comp header{{display:flex;gap:12px;align-items:baseline}} .comp header h3{{margin:0}} .comp header span{{color:var(--ink-muted);font-size:14px}}
.pv{{width:100%;border:1px solid var(--line);border-radius:12px;background:var(--surface);margin-top:8px;display:block}}
details{{margin-top:8px}} summary{{cursor:pointer;color:var(--brand-text);font-weight:600;font-size:14px}}
.md table{{border-collapse:collapse;margin:12px 0}} .md td,.md th{{border:1px solid var(--line);padding:6px 10px;text-align:left;vertical-align:top}}
.md blockquote{{margin:12px 0;padding-left:16px;border-left:3px solid var(--brand)}} .md pre{{white-space:pre-wrap}}
.md code{{background:var(--brand-soft);padding:1px 5px;border-radius:4px;color:var(--ink)}}
.note{{color:var(--ink-muted)}}
.logos{{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:16px}}
.lg{{margin:0}} .lg div{{display:flex;align-items:center;justify-content:center;height:160px;border:1px solid var(--line);border-radius:12px;padding:12px}}
.lg img{{max-width:100%;max-height:100%;object-fit:contain}} .lg figcaption{{margin-top:6px;word-break:break-all}}
@media(max-width:800px){{.wrap{{grid-template-columns:1fr}}nav{{display:none}}main{{padding:16px}}.ts{{grid-template-columns:1fr}}.row{{grid-template-columns:70px 1fr 50px}}.row p{{grid-column:1/-1}}}}
</style></head><body>
<div class="top"><h1>{title}</h1><small>Design system · {note}</small><button class="tg" id="tg" type="button">Chiaro / Scuro</button></div>
<div class="wrap"><nav>
<h4>Fondamenta</h4><a href="#colori">Colori</a><a href="#tipografia">Tipografia</a><a href="#spazi">Spaziature</a><a href="#forme">Raggi e ombre</a><a href="#loghi">Loghi</a>
<h4>Componenti</h4>{nav_comp}
<h4>Sezioni</h4>{nav_docs}
</nav><main>
<h2 id="colori">Colori</h2><p class="note">Ogni campione mostra il tema chiaro (sinistra) e scuro (destra).</p><div class="grid">{colors}</div>
<h2 id="tipografia">Tipografia</h2>{type_html}
<h2 id="spazi">Spaziature</h2>{space_html}
<h2 id="forme">Raggi e ombre</h2><div class="shapes">{radius_html}</div><h3>Ombre</h3><div class="shapes">{shadow_html}</div>
<h2 id="loghi">Loghi</h2><p class="note">Sono mostrati i PNG a 1024 px. Gli SVG e le misure 512 e 2048 sono in project/assets/Logos/. Regole d'uso nella sezione Loghi più in basso.</p><div class="logos">{logos_html}</div>
<h2 id="componenti">Componenti</h2>{comp_html}
{doc_html}
</main></div>
{THEME_JS}
<script src="https://cdnjs.cloudflare.com/ajax/libs/marked/12.0.2/marked.min.js"></script>
<script>
document.querySelectorAll('.md').forEach(function(el){{var t=el.getAttribute('data-md')||'';
 if(window.marked){{el.innerHTML=marked.parse(t)}}else{{var p=document.createElement('pre');p.textContent=t;el.appendChild(p)}}}});
function push(){{var t=document.documentElement.getAttribute('data-theme');
 document.querySelectorAll('iframe.pv').forEach(function(f){{try{{f.contentWindow.postMessage({{theme:t}},'*')}}catch(e){{}}}})}}
document.querySelectorAll('iframe.pv').forEach(function(f){{f.addEventListener('load',push)}});
document.getElementById('tg').onclick=function(){{var d=document.documentElement;var t=d.getAttribute('data-theme')==='dark'?'light':'dark';
 d.setAttribute('data-theme',t);try{{localStorage.setItem('ds-theme',t)}}catch(e){{}}push()}};
</script></body></html>"""
(OUT / "index.html").write_text(PAGE, encoding="utf-8")
(OUT / ".nojekyll").write_text("", encoding="utf-8")
print("Generati", len(components), "componenti e", len(docs), "sezioni in", OUT)
