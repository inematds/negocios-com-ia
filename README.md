# Negócios com IA: os 13 do pior ao melhor para começar — e a escada para subir

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

[![Negócios com IA](guia/assets/banner.jpg)](https://inematds.github.io/negocios-com-ia/guia/)

## O que é

Todo dia aparece um negócio novo para abrir com inteligência artificial, e escolher ficou mais difícil do que construir. Esta página avalia treze deles com três notas de 1 a 5: quanto conhecimento técnico você precisa para entregar algo que alguém pague, quanto espaço existe no mercado (mais compradores do que vendedores) e quanto o negócio dura e cresce sem ser engolido por uma plataforma. A lista vai do pior para o melhor para quem está começando. A regra que aparece no fim é simples: embaixo você vende o que constrói, que fica mais barato a cada mês; em cima você vende o seu julgamento, que fica mais valioso. Por isso a segunda parte é uma escada de quatro degraus, com um teste de 6 perguntas para achar o seu, a oferta pronta de cada negócio, exemplos por setor e um plano de 90 dias. Os valores em reais são faixas de referência do que se cobra, não promessa de ganho.

## 📖 Página

- Ranking dos 13 negócios: **https://inematds.github.io/negocios-com-ia/guia/**
- Escada, teste e plano de 90 dias: **https://inematds.github.io/negocios-com-ia/guia/escada/**

(Exige técnica / Espaço no mercado / Dura e cresce)

13. 📱 **Aplicativo por assinatura com IA (SaaS)** — 4/1/3
12. 🎬 **Canal sem rosto feito com IA** — 2/2/1
11. 🌐 **Sites para empresas feitos com IA** — 1/2/1
10. 🧩 **Central de IA da empresa** — 3/4/2
9. 🔎 **Aparecer nas respostas da IA (GEO)** — 2/3/2
8. ⚙️ **Automação e integração** — 2/3/2
7. 🎓 **Workshops de IA para equipes** — 3/3/3
6. 📞 **Atendente e recepcionista com IA** — 3/4/2
5. 🎨 **Estúdio criativo com IA** — 3/4/3
4. 🎯 **Geração de clientes (leads) com IA** — 4/3/5
3. 🎙️ **Educação e marca pessoal** — 3/3/5
2. 🩺 **Consultoria e diagnóstico de IA** — 3/4/4
1. 🧭 **Diretor de IA (na empresa ou fracionado)** — 4/5/5

## Como está organizado

- `conteudo/pt.json` (+ `en.json`, `es.json`) — negócios, notas, degraus, teste, setores, plano.
- `conteudo/imagens.json` + `scripts/gerar-imagens.sh` — imagens (Codex image_gen).
- `scripts/traduzir.sh` — EN/ES pelo tradutor central `inema-traduz`.
- `scripts/build.py` — gera `guia/`, `guia/escada/` e `en/`, `es/`.

## O processo, do início ao fim

1. 🧠 Sessão com o Nei: escolher os negócios, as notas e escrever `conteudo/pt.json`.
2. 🧠 Descrever as cenas em `conteudo/imagens.json`.
3. ⚙️ `scripts/gerar-imagens.sh` — Codex gera as 13 imagens (4 em paralelo).
4. ⚙️ `scripts/traduzir.sh` — `inema-traduz` traduz para EN e ES e confere a estrutura.
5. ⚙️ `gerar-banner.sh` (skill projetos-landing-guia) — banners live e grade PT/EN/ES.
6. ⚙️ `python3 scripts/build.py` — monta ranking e escada nos 3 idiomas.
7. 🧠 Conferir no navegador (360 px a 1920 px, teste e abas) e `git push` (GitHub Pages).
8. 🤖 Explicavideo 16:9 + 9:16 (`roda_ev.sh`, avatar no estúdio HeyGen) → lives1 + Metricool inematds.
9. 🧠 Portal (inema.club), área no eventos e tópico no Telegram INEMA.IA.
