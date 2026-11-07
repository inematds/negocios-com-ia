# AI Businesses: 13 from Worst to Best — and Where to Start

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

[![AI Businesses](guia/assets/banner-en.jpg)](https://inematds.github.io/negocios-com-ia/guia/en/)

## What it is

Every day, a new business idea built around artificial intelligence appears, and choosing has become harder than building. This page rates thirteen of them on three 1-to-5 scales: how much technical knowledge you need to deliver something people will pay for, how much room there is in the market (more buyers than sellers), and how long the business can last and grow without being swallowed by a platform. The list ranks them from worst to best for building over the long term. That is not the same as the best one to start with: the top spot requires experience no one has on day one, and some businesses near the bottom are great first steps. The simple rule at the end is this: at the bottom, you sell what you build, which gets cheaper every month; at the top, you sell your judgment, which becomes more valuable. That is why the second part is a four-step ladder, with a 6-question assessment to find your step, a ready-to-use offer for each business, industry examples, and a 90-day plan. Prices in reais are reference ranges for what businesses charge, not a promise of earnings.

## 📖 Page

- Ranking of the 13 businesses: **https://inematds.github.io/negocios-com-ia/guia/en/**
- Video (16:9 and short, in Portuguese): **https://inematds.github.io/negocios-com-ia/videos/**
- Ladder, quiz and 90-day plan: **https://inematds.github.io/negocios-com-ia/guia/en/escada/**

(Technical demands / Market opportunity / Durability and growth)

13. 📱 **AI subscription app (SaaS)** — 4/1/3
12. 🎬 **Faceless channel made with AI** — 2/2/1
11. 🌐 **AI-built websites for businesses** — 1/2/1
10. 🧩 **Company AI hub** — 3/4/2
9. 🔎 **Show up in AI answers (GEO)** — 2/3/2
8. ⚙️ **Automation and integration** — 2/3/2
7. 🎓 **AI workshops for teams** — 3/3/3
6. 📞 **AI customer service and receptionist** — 3/4/2
5. 🎨 **AI creative studio** — 3/4/3
4. 🎯 **AI-powered lead generation** — 4/3/5
3. 🎙️ **Education and personal brand** — 3/3/5
2. 🩺 **AI consulting and diagnosis** — 3/4/4
1. 🧭 **AI director (in-house or fractional)** — 4/5/5

## How it is organized

- `conteudo/pt.json` (+ `en.json`, `es.json`) — negócios, notas, degraus, teste, setores, plano.
- `conteudo/imagens.json` + `scripts/gerar-imagens.sh` — imagens (Codex image_gen).
- `scripts/traduzir.sh` — EN/ES pelo tradutor central `inema-traduz`.
- `scripts/build.py` — gera `guia/`, `guia/escada/` e `en/`, `es/`.

## The process, start to finish

1. 🧠 Sessão com o Nei: escolher os negócios, as notas e escrever `conteudo/pt.json`.
2. 🧠 Descrever as cenas em `conteudo/imagens.json`.
3. ⚙️ `scripts/gerar-imagens.sh` — Codex gera as 13 imagens (4 em paralelo).
4. ⚙️ `scripts/traduzir.sh` — `inema-traduz` traduz para EN e ES e confere a estrutura.
5. ⚙️ `gerar-banner.sh` (skill projetos-landing-guia) — banners live e grade PT/EN/ES.
6. ⚙️ `python3 scripts/build.py` — monta ranking e escada nos 3 idiomas.
7. 🧠 Conferir no navegador (360 px a 1920 px, teste e abas) e `git push` (GitHub Pages).
8. 🤖 Explicavideo 16:9 + 9:16 (`roda_ev.sh`, avatar no estúdio HeyGen) → lives1 + Metricool inematds.
9. 🧠 Portal (inema.club), área no eventos e tópico no Telegram INEMA.IA.
