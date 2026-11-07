#!/usr/bin/env python3
"""Monta o guia Negócios com IA a partir de conteudo/<lang>.json.
Saída: guia/index.html (ranking) e guia/escada/index.html (escada + teste), mais en/ e es/.
Uso: python3 scripts/build.py [pt en es]"""
import json, html, pathlib, sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
SLUG = "negocios-com-ia"
REPO = f"https://github.com/inematds/{SLUG}"
BASE = f"https://inematds.github.io/{SLUG}/guia/"
LANGS = {"pt": ("pt-BR", ""), "en": ("en", "en"), "es": ("es", "es")}
E = html.escape
CSS = (RAIZ / "scripts/base.css").read_text() + r"""
.q .lbl,.facts .f small,.ofr small,.q .curta small,.diag .dt{font-size:.8rem!important}
ul.rel .tp{font-size:.75rem!important}
.rk li a{display:block;padding:.35em 0;min-height:40px}
.esc .dg li a{display:block;padding:.45em 0}
/* notas */
.nt{display:grid;gap:9px}
.nt .r{display:grid;grid-template-columns:118px minmax(0,1fr) 30px;gap:10px;align-items:center;font-family:Sora;font-size:.8rem;font-weight:600}
.nt .r .tr{height:12px;background:var(--bg2);border-radius:999px;overflow:hidden}
.nt .r .fl{height:100%;width:0;border-radius:999px;background:#FACC15;transition:width 1.1s cubic-bezier(.2,.7,.2,1);transition-delay:calc(var(--i)*220ms)}
.nt .r.tec .fl{background:var(--bad)}.nt .r.dur .fl{background:var(--ok)}
.nt .r b{text-align:right;color:var(--amb)}
.diag.vis .nt .fl{width:var(--w)}
@media(prefers-reduced-motion:reduce){.nt .fl{width:var(--w)!important;transition:none}}
.pos{display:inline-flex;align-items:center;gap:8px}
.pos .num{font-family:Sora;font-weight:800;font-size:2.1rem;line-height:1;color:var(--amb)}
.facts{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:1.2em}
@media(max-width:600px){.facts{grid-template-columns:1fr}}
.facts .f{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 14px;min-width:0}
.facts .f small{display:block;font-family:Sora;font-size:.7rem;letter-spacing:.12em;text-transform:uppercase;color:var(--mut);font-weight:600;margin-bottom:.3em}
.facts .f.bad{border-left:4px solid var(--bad)}.facts .f.ok{border-left:4px solid var(--ok)}
.ofr{margin-top:1em;background:var(--card);border:1px dashed var(--amb);border-radius:12px;padding:12px 14px;font-style:italic}
.ofr small{display:block;font-style:normal;font-family:Sora;font-size:.7rem;letter-spacing:.12em;text-transform:uppercase;color:var(--amb);font-weight:600;margin-bottom:.3em}
.rk ol{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:1fr 1fr;gap:6px 22px}
@media(max-width:760px){.rk ol{grid-template-columns:1fr}}
.rk li{display:grid;grid-template-columns:44px minmax(0,1fr) auto;gap:12px;align-items:center;padding:11px 0;border-bottom:1px solid var(--line)}
.rk li .p{font-family:Sora;font-weight:800;color:var(--amb);font-size:1.05rem}
.rk li a{color:var(--txt);font-weight:600;font-family:Sora;font-size:.95rem;line-height:1.3}.rk li a:hover{color:var(--amb)}
.rk li span.c{display:block;color:var(--mut);font-size:.86rem;margin-top:.2em;font-family:Inter;font-weight:400}
.rk li .mini{display:flex;gap:3px}.rk li .mini i{width:8px;height:22px;border-radius:3px;background:var(--bg2);display:block;position:relative;overflow:hidden}
.rk li .mini i:after{content:"";position:absolute;left:0;right:0;bottom:0;height:var(--h);background:#FACC15}
.rk li .mini i.tec:after{background:var(--bad)}.rk li .mini i.dur:after{background:var(--ok)}
.regra{background:linear-gradient(135deg,rgba(250,204,21,.10),transparent 60%)}
.regra p{font-size:1.1rem;max-width:70ch}
/* escada */
.esc{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;align-items:end}
@media(max-width:820px){.esc{grid-template-columns:1fr 1fr}}
@media(max-width:480px){.esc{grid-template-columns:1fr}}
.esc .dg{background:var(--card);border:1px solid var(--line);border-top:4px solid #FACC15;border-radius:14px;padding:16px;min-width:0}
@media(min-width:821px){.esc .dg:nth-child(1){margin-top:180px}.esc .dg:nth-child(2){margin-top:120px}.esc .dg:nth-child(3){margin-top:60px}}
.esc .dg .k{font-family:Sora;font-size:.72rem;letter-spacing:.12em;text-transform:uppercase;color:var(--amb);font-weight:700}
.esc .dg h3{font-size:1.1rem;margin:.3em 0}.esc .dg .v{font-family:Sora;font-weight:600;font-size:.88rem}
.esc .dg p{color:var(--mut);font-size:.88rem;margin:.5em 0}
.esc .dg ul{list-style:none;margin:.4em 0 0;padding:0;font-size:.86rem}.esc .dg li{padding:.2em 0}
.esc .dg li a{color:var(--txt)}.esc .dg li a:hover{color:var(--amb)}
.esc .dg{opacity:0;transform:translateY(16px);transition:opacity .6s,transform .6s;transition-delay:calc(var(--i)*200ms)}
.diag.vis .esc .dg,.esc.vis .dg{opacity:1;transform:none}
.teste .qq{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px 18px;margin-bottom:12px}
.teste .qq h3{font-size:1rem;margin-bottom:.7em}.teste .qq h3 b{color:var(--amb)}
.teste .ops{display:flex;flex-wrap:wrap;gap:8px}
.teste .ops label{cursor:pointer;border:1px solid var(--line);border-radius:10px;padding:.5em .85em;font-size:.92rem;background:var(--bg2);user-select:none}
.teste .ops input{position:absolute;opacity:0;pointer-events:none}
.teste .ops input:checked+span{color:#1a1206}
.teste .ops label:has(input:checked){background:#FACC15;border-color:#FACC15;color:#1a1206;font-weight:600}
.teste .ops input:focus-visible+span{outline:2px solid var(--amb);outline-offset:3px}
.teste button.btn{border:0;cursor:pointer;font-size:1rem;margin-top:8px}
#res{margin-top:22px}
#res .box{background:var(--card);border:1px solid #FACC15;border-radius:16px;padding:20px;display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:20px}
@media(max-width:760px){#res .box{grid-template-columns:1fr}}
#res img{width:100%;border-radius:12px;display:block}
#res h3{font-size:1.4rem;margin:.2em 0 .5em}
#res .alt{color:var(--mut);font-size:.92rem;margin-top:.8em}
#res .msg{color:var(--bad)}
.fichas .grid{grid-template-columns:repeat(3,1fr)}
@media(max-width:900px){.fichas .grid{grid-template-columns:1fr 1fr}}@media(max-width:560px){.fichas .grid{grid-template-columns:1fr}}
.fichas .card{display:flex;flex-direction:column;gap:6px;scroll-margin-top:80px}
.fichas .card .of{font-style:italic;color:var(--txt);font-size:.92rem}
.fichas .card .kp{font-size:.84rem;color:var(--mut)}.fichas .card .kp b{color:var(--ok);font-weight:600}
.fichas .card .lk{margin-top:auto;font-size:.86rem}
.fichas h3.dgh{grid-column:1/-1;font-size:1rem;margin-top:12px;color:var(--amb)}
.tabs{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:16px}
.tabs button{cursor:pointer;border:1px solid var(--line);background:var(--bg2);color:var(--txt);border-radius:999px;padding:.45em .95em;font:600 .9rem Sora}
.tabs button[aria-selected=true]{background:#FACC15;border-color:#FACC15;color:#1a1206}
.setor{display:none}.setor.on{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}
@media(max-width:820px){.setor.on{grid-template-columns:1fr 1fr}}@media(max-width:480px){.setor.on{grid-template-columns:1fr}}
.setor .card .k{font-family:Sora;font-size:.7rem;letter-spacing:.12em;text-transform:uppercase;color:var(--amb);font-weight:700}
.setor .card p{color:var(--txt);margin-top:.4em}
"""

JS = r"""
(function(){var K='%s-theme',b=document.body,t=document.getElementById('themeToggle');
try{if(localStorage.getItem(K)==='light'){b.classList.add('light');t.textContent='☀️';}}catch(e){}
t.addEventListener('click',function(){var l=b.classList.toggle('light');t.textContent=l?'☀️':'🌙';try{localStorage.setItem(K,l?'light':'dark')}catch(e){}});
var ds=document.querySelectorAll('.diag,.esc');
if(!('IntersectionObserver' in window)){ds.forEach(function(d){d.classList.add('vis')});}else{
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('vis');io.unobserve(e.target);}})},{threshold:.2});
ds.forEach(function(d){io.observe(d)});}
})();
""" % SLUG

FONTES = '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;600;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">'
TIPO = {"projeto": "rel_projeto", "curso": "rel_curso"}


def cabeca(ui, hl, title, desc, og, pagina, sub):
    rel_path = (sub + "/" if sub else "") + pagina
    alts = "".join(f'<link rel="alternate" hreflang="{h}" href="{BASE}{p}{pagina}">' for h, p in (("pt-BR", ""), ("en", "en/"), ("es", "es/")))
    return f"""<!DOCTYPE html>
<html lang="{hl}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:image" content="{og}">
<link rel="canonical" href="{BASE}{rel_path}">
{alts}
{FONTES}
<style>{CSS}</style>
</head>
<body>"""


def barra(ui, sel, inicio, links):
    return f"""<nav><div class="wrap">
  <a class="brand" href="{inicio}"><span class="emoji">🪜</span> {E(ui["brand"])}</a>
  <span class="sep">|</span>
  <span class="clubpro"><a class="inema" href="https://inema.club" target="_blank" rel="noopener">INEMA.CLUB</a><span class="sep">-</span><a class="pro" href="https://inema.pro" target="_blank" rel="noopener">PRO</a></span>
  <div class="links">
    {links}
    <span class="lang">{sel}</span>
    <button class="tgl" id="themeToggle" aria-label="{E(ui["toggle"])}" title="{E(ui["toggle"])}">🌙</button>
    <a class="btn" href="{REPO}" target="_blank" rel="noopener">GitHub</a>
  </div>
</div></nav>"""


def rodape(ui, extra_js=""):
    return f"""<footer><div class="wrap">
  <span class="pill">HTML + CSS</span><span class="pill">PT · EN · ES</span>
  <p style="margin-top:18px">{E(ui["brand"])} · {E(ui["rodape"])} · <a href="{REPO}">inematds/{SLUG}</a> · <a href="https://inema.club">INEMA.CLUB</a></p>
</div></footer>
<script>{JS}{extra_js}</script>
</body>
</html>
"""


def seletor(sub, pagina):
    """links para a mesma página nos 3 idiomas; pagina = '' ou 'escada/'"""
    sobe = ("../" if sub else "") + ("../" if pagina else "")
    return "".join(f'<a{" class=\"on\"" if l == sub else ""} href="{sobe}{(l + "/") if l else ""}{pagina}">{l.upper() if l else "PT"}</a>' for l in ("", "en", "es"))


def notas(n, ui, i0=0):
    return '<div class="nt">' + "".join(
        f'<div class="r {k}"><span>{E(ui["n_" + k])}</span><div class="tr"><div class="fl" style="--i:{i0+j};--w:{n[k]*20}%"></div></div><b>{n[k]}/5</b></div>'
        for j, k in enumerate(("tec", "mer", "dur"))) + "</div>"


def rel_lista(itens, ui, lang):
    if lang != "pt":
        itens = [dict(x, url=x["url"] + lang + "/") if x.get("i18n") else x for x in itens]
    lis = "".join(f'<li><a href="{E(x["url"])}" target="_blank" rel="noopener"><span class="tp {x["t"]}">{E(ui[TIPO[x["t"]]])}</span><span><span class="nm">{E(x["nome"])}</span><span class="ds">{E(x["d"])}</span></span></a></li>' for x in itens)
    nota = f'<p class="rel-nota">{E(ui["rel_nota"])}</p>' if lang != "pt" and any(not x.get("i18n") for x in itens) else ""
    return f'<ul class="rel">{lis}</ul>{nota}'


def fluxo(passos, ui):
    parts = []
    for i, p in enumerate(passos):
        if i:
            parts.append(f'<div class="ar" data-i style="--i:{i}" aria-hidden="true"></div>')
        parts.append(f'<div class="st" data-i style="--i:{i}"><b>{i+1}</b>{E(p)}</div>')
    return f'<div class="diag"><div class="dt">{E(ui["comecar"])}</div><div class="df">' + "".join(parts) + "</div></div>"


def ranking(c, lang):
    ui = c["ui"]; hl, sub = LANGS[lang]
    pre = "../" if sub else ""; a = f"{pre}assets"; suf = f"-{sub}" if sub else ""
    ns = c["negocios"]
    rk = "".join(
        f'<li><span class="p">{x["pos"]}º</span><div><a href="#{x["id"]}">{x["emoji"]} {E(x["nome"])}</a><span class="c">{E(x["curta"])}</span></div>'
        f'<span class="mini" aria-label="{x["notas"]["tec"]}/{x["notas"]["mer"]}/{x["notas"]["dur"]}">' + "".join(f'<i class="{k}" style="--h:{x["notas"][k]*20}%"></i>' for k in ("tec", "mer", "dur")) + "</span></li>"
        for x in ns)
    cards = ""
    for x in ns:
        tx = "".join(f"<p>{E(p)}</p>" for p in x["texto"])
        cards += (f'<article class="q" id="{x["id"]}"><div class="side">'
                  f'<figure><img src="{a}/img/{x["id"]}.jpg" alt="{E(ui["img_alt"])}: {E(x["nome"])}" loading="lazy" width="1280" height="720"></figure>'
                  f'<div class="diag"><div class="dt">{x["emoji"]} {E(ui["notas_titulo"])}</div>{notas(x["notas"], ui)}</div>'
                  f'{fluxo(x["comecar"], ui)}</div><div>'
                  f'<span class="pos"><span class="num">{x["pos"]}º</span><span class="chip">{E(ui["degrau"])} {x["degrau"]}</span></span><h3>{E(x["nome"])}</h3>'
                  f'<div class="curta"><small>{E(ui["curta"])}</small>{E(x["curta"])}</div>'
                  f'<div class="lbl">{E(ui["explica"])}</div><div class="texto">{tx}</div>'
                  f'<div class="facts"><div class="f"><small>{E(ui["preco"])}</small>{E(x["preco"])}</div><div class="f ok"><small>{E(ui["para_quem"])}</small>{E(x["para_quem"])}</div>'
                  f'<div class="f bad" style="grid-column:1/-1"><small>{E(ui["armadilha"])}</small>{E(x["armadilha"])}</div></div>'
                  f'<div class="ofr"><small>{E(ui["oferta"])}</small>“{E(x["oferta"])}”</div>'
                  f'<div class="lbl">{E(ui["rel_titulo"])}</div>{rel_lista(x["rel"], ui, lang)}'
                  f'<a class="topo" href="#lista">↑ {E(ui["topo"])}</a></div></article>')
    leg = "".join(f'<div class="card"><h3>{E(ui["n_" + k])}</h3><p>{E(ui["n_" + k + "_d"])}</p></div>' for k in ("tec", "mer", "dur"))
    doc = cabeca(ui, hl, ui["title"], ui["description"], f"{BASE}assets/banner{suf}.jpg", "", sub)
    doc += barra(ui, seletor(sub, ""), "#top", f'<a class="sec" href="#lista">{E(ui["nav_ranking"])}</a><a class="sec" href="escada/">{E(ui["nav_escada"])}</a><a class="sec" href="escada/#teste">{E(ui["nav_teste"])}</a>')
    doc += f"""
<header class="hero" id="top"><div class="glow"></div><div class="wrap">
  <div>
    <span class="chip">{E(ui["hero_chip"])}</span>
    <h1>{ui["hero_titulo"]}</h1>
    <p class="lead">{E(ui["hero_lead"])}</p>
    <div class="cta"><a class="btn" href="#lista">{E(ui["cta1"])}</a><a class="btn ghost" href="escada/#teste">{E(ui["cta2"])}</a></div>
  </div>
  <figure><img src="{a}/banner{suf}.jpg" alt="{E(ui["hero_alt"])}" width="1400" height="788"></figure>
</div></header>
<section class="resumo"><div class="wrap">
  <span class="chip">{E(ui["resumo_chip"])}</span>
  <p>{E(ui["resumo"])}</p>
</div></section>
<section id="notas"><div class="wrap">
  <span class="chip">{E(ui["notas_chip"])}</span><h2>{E(ui["notas_titulo"])}</h2><p class="sub">{E(ui["notas_sub"])}</p>
  <figure class="big"><img src="{a}/banner-grade{suf}.jpg" alt="{E(ui["hero_alt"])}" loading="lazy" width="1400" height="788"></figure>
  <div class="grid g4" style="grid-template-columns:repeat(auto-fit,minmax(220px,1fr))">{leg}</div>
  <p class="sub" style="margin-top:1.4em">🪜 {E(ui["degrau_nota"])} <a href="escada/#degraus">{E(ui["nav_escada"])} →</a></p>
</div></section>
<section id="lista" class="rk"><div class="wrap">
  <span class="chip">{E(ui["rapido_chip"])}</span><h2>{E(ui["rapido_titulo"])}</h2><p class="sub">{E(ui["rapido_sub"])}</p>
  <ol>{rk}</ol>
</div></section>
<section id="negocios"><div class="wrap">{cards}</div></section>
<section class="regra"><div class="wrap">
  <span class="chip">{E(ui["regra_chip"])}</span><h2>{E(ui["regra_titulo"])}</h2>
  <p>{E(ui["regra_texto"])}</p>
  <p><a class="btn" href="escada/#teste">{E(ui["regra_cta"])} →</a></p>
  <div class="aviso">{E(ui["aviso"])}</div>
</div></section>
"""
    doc += rodape(ui)
    out = RAIZ / "guia" / (f"{sub}/" if sub else "") / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True); out.write_text(doc)
    return out


TESTE_JS = r"""
(function(){var D=JSON.parse(document.getElementById('dados').textContent);
var f=document.getElementById('fteste'),r=document.getElementById('res');
function ficha(id){return D.n.filter(function(x){return x.id===id})[0]}
f.addEventListener('submit',function(ev){ev.preventDefault();var s={},ok=true;
for(var i=0;i<D.q;i++){var m=f.querySelector('input[name=q'+i+']:checked');if(!m){ok=false;continue;}
var o=JSON.parse(m.value);for(var k in o){s[k]=(s[k]||0)+o[k];}}
if(!ok){r.innerHTML='<p class="msg">'+D.ui.falta+'</p>';return;}
var ord=Object.keys(s).sort(function(a,b){return s[b]-s[a]||ficha(a).pos-ficha(b).pos});
var a=ficha(ord[0]),b=ficha(ord[1]),c=ficha(ord[2]);
var up=D.dg.filter(function(d){return d.n===a.degrau+1})[0];
r.innerHTML='<div class="box"><img src="'+D.img+a.id+'.jpg" alt=""><div><span class="chip">'+D.ui.res+'</span><h3>'+a.emoji+' '+a.nome+'</h3>'+
'<div class="curta">'+a.curta+'</div><div class="ofr"><small>'+D.ui.oferta+'</small>“'+a.oferta+'”</div>'+
'<p class="alt"><b>'+D.ui.seg+':</b> '+b.emoji+' '+b.nome+' · '+c.emoji+' '+c.nome+'</p>'+
'<p class="alt"><b>'+D.ui.prox+':</b> '+(up?up.emoji+' '+up.nome+' — '+up.vende:D.ui.topo)+'</p>'+
'<p style="margin-top:14px"><a class="btn" href="'+D.rank+'#'+a.id+'">'+D.ui.ficha+' →</a> <a class="btn ghost" href="#teste" id="refaz">'+D.ui.refaz+'</a></p></div></div>';
document.getElementById('refaz').addEventListener('click',function(){f.reset();r.innerHTML='';});
r.scrollIntoView({behavior:'smooth',block:'start'});});
var tb=document.querySelectorAll('.tabs button');tb.forEach(function(x){x.addEventListener('click',function(){
tb.forEach(function(y){y.setAttribute('aria-selected',y===x?'true':'false')});
document.querySelectorAll('.setor').forEach(function(p){p.classList.toggle('on',p.id==='s-'+x.dataset.s)});});});
})();
"""


def escada(c, lang):
    ui = c["ui"]; hl, sub = LANGS[lang]
    pre = ("../" if sub else "") + "../"; a = f"{pre}assets"
    ns = {x["id"]: x for x in c["negocios"]}
    dgs = ""
    for i, d in enumerate(c["degraus"]):
        lis = "".join(f'<li><a href="#f-{k}">{ns[k]["emoji"]} {E(ns[k]["nome"])}</a></li>' for k in d["ids"])
        dgs += f'<div class="dg" style="--i:{i}"><span class="k">{E(ui["degrau"])} {d["n"]} {d["emoji"]}</span><h3>{E(d["nome"])}</h3><div class="v">{E(d["vende"])}</div><p>{E(d["d"])}</p><ul>{lis}</ul></div>'
    qs = ""
    for i, q in enumerate(c["teste"]):
        ops = "".join(f'<label><input type="radio" name="q{i}" value="{E(json.dumps(o["s"]))}"><span>{E(o["t"])}</span></label>' for o in q["op"])
        qs += f'<fieldset class="qq" style="border:1px solid var(--line)"><h3><b>{i+1}.</b> {E(q["p"])}</h3><div class="ops">{ops}</div></fieldset>'
    fich = ""
    for d in c["degraus"]:
        fich += f'<h3 class="dgh">{d["emoji"]} {E(ui["degrau"])} {d["n"]} · {E(d["nome"])}</h3>'
        for k in d["ids"]:
            x = ns[k]; r0 = x["rel"][0]
            url = r0["url"] + (lang + "/" if lang != "pt" and r0.get("i18n") else "")
            fich += (f'<div class="card" id="f-{k}"><span class="n">{x["pos"]}º · {x["emoji"]}</span><h3>{E(x["nome"])}</h3>'
                     f'<p class="of">“{E(x["oferta"])}”</p><p class="kp"><b>{E(ui["kpi"])}:</b> {E(x["kpi"])}</p>'
                     f'<p class="kp">{E(x["preco"])}</p>'
                     f'<a class="lk" href="{E(url)}" target="_blank" rel="noopener">{E(ui[TIPO[r0["t"]]])}: {E(r0["nome"])} →</a></div>')
    tabs = "".join(f'<button type="button" role="tab" data-s="{s["id"]}" aria-selected="{"true" if i == 0 else "false"}">{s["emoji"]} {E(s["nome"])}</button>' for i, s in enumerate(c["setores"]))
    dmap = {d["n"]: d for d in c["degraus"]}
    sets = "".join(f'<div class="setor{" on" if i == 0 else ""}" id="s-{s["id"]}" role="tabpanel">' + "".join(
        f'<div class="card"><span class="k">{E(ui["degrau"])} {o["d"]} · {E(dmap[o["d"]]["nome"])}</span><p>{E(o["t"])}</p></div>' for o in s["ofertas"]) + "</div>"
        for i, s in enumerate(c["setores"]))
    plano = '<div class="diag"><div class="dtm">' + "".join(f'<div class="mk" data-i style="--i:{i}"><i></i><div><strong>{E(m["t"])}</strong><span>{E(m["d"])}</span></div></div>' for i, m in enumerate(c["plano"])) + "</div></div>"
    dados = {"q": len(c["teste"]), "img": f"{a}/img/", "rank": "../",
             "n": [{k: x[k] for k in ("id", "pos", "emoji", "nome", "curta", "oferta", "degrau")} for x in c["negocios"]],
             "dg": [{k: d[k] for k in ("n", "emoji", "nome", "vende")} for d in c["degraus"]],
             "ui": {"falta": ui["teste_falta"], "res": ui["teste_res"], "seg": ui["teste_seg"], "prox": ui["teste_prox"], "refaz": ui["teste_refaz"], "ficha": ui["teste_ficha"], "oferta": ui["oferta"], "topo": ui["teste_topo"]}}
    dados_txt = json.dumps(dados, ensure_ascii=False).replace("</", "<\\/")
    doc = cabeca(ui, hl, ui["escada_titulo"], ui["escada_desc"], f"{BASE}assets/banner-grade{'-' + sub if sub else ''}.jpg", "escada/", sub)
    doc += barra(ui, seletor(sub, "escada/"), "../", f'<a class="sec" href="../#lista">{E(ui["nav_ranking"])}</a><a class="sec" href="#degraus">{E(ui["nav_escada"])}</a><a class="sec" href="#teste">{E(ui["nav_teste"])}</a>')
    doc += f"""
<header class="hero" id="top"><div class="glow"></div><div class="wrap" style="grid-template-columns:1fr">
  <div>
    <span class="chip">{E(ui["escada_chip"])}</span>
    <h1>{ui["escada_h1"]}</h1>
    <p class="lead" style="max-width:60ch">{E(ui["escada_lead"])}</p>
    <div class="cta"><a class="btn" href="#teste">{E(ui["escada_cta"])}</a><a class="btn ghost" href="../">{E(ui["escada_volta"])}</a></div>
  </div>
</div></header>
<section id="degraus"><div class="wrap">
  <span class="chip">{E(ui["degraus_chip"])}</span><h2>{E(ui["degraus_titulo"])}</h2><p class="sub">{E(ui["degraus_sub"])}</p>
  <div class="esc">{dgs}</div>
</div></section>
<section id="teste" class="teste"><div class="wrap">
  <span class="chip">{E(ui["teste_chip"])}</span><h2>{E(ui["teste_titulo"])}</h2><p class="sub">{E(ui["teste_sub"])}</p>
  <form id="fteste">{qs}<button class="btn" type="submit">{E(ui["teste_ver"])}</button></form>
  <div id="res" aria-live="polite"></div>
</div></section>
<section id="fichas" class="fichas"><div class="wrap">
  <span class="chip">{E(ui["fichas_chip"])}</span><h2>{E(ui["fichas_titulo"])}</h2><p class="sub">{E(ui["fichas_sub"])}</p>
  <div class="grid">{fich}</div>
</div></section>
<section id="setores"><div class="wrap">
  <span class="chip">{E(ui["setores_chip"])}</span><h2>{E(ui["setores_titulo"])}</h2><p class="sub">{E(ui["setores_sub"])}</p>
  <div class="tabs" role="tablist">{tabs}</div>{sets}
</div></section>
<section id="plano"><div class="wrap">
  <span class="chip">{E(ui["plano_chip"])}</span><h2>{E(ui["plano_titulo"])}</h2><p class="sub">{E(ui["plano_sub"])}</p>
  {plano}
</div></section>
<section class="regra"><div class="wrap">
  <span class="chip">{E(ui["foco_chip"])}</span><h2>{E(ui["foco_titulo"])}</h2><p>{E(ui["foco_texto"])}</p>
  <div class="aviso">{E(ui["aviso"])}</div>
</div></section>
<script type="application/json" id="dados">{dados_txt}</script>
"""
    doc += rodape(ui, TESTE_JS)
    out = RAIZ / "guia" / (f"{sub}/" if sub else "") / "escada/index.html"
    out.parent.mkdir(parents=True, exist_ok=True); out.write_text(doc)
    return out


if __name__ == "__main__":
    for l in (sys.argv[1:] or LANGS):
        src = RAIZ / f"conteudo/{l}.json"
        if not src.exists():
            print(f"--  {l} (sem conteudo/{l}.json)"); continue
        c = json.loads(src.read_text())
        for f in (ranking, escada):
            print("ok ", f(c, l).relative_to(RAIZ))
