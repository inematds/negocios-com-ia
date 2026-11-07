# Negocios con IA: los 13 del peor al mejor, y por dónde empezar

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

[![Negocios con IA](guia/assets/banner-es.jpg)](https://inematds.github.io/negocios-com-ia/guia/es/)

## Qué es

Cada día aparece un nuevo negocio que puedes iniciar con inteligencia artificial, y elegir se ha vuelto más difícil que construir. Esta página evalúa trece de ellos con tres calificaciones del 1 al 5: cuánto conocimiento técnico necesitas para entregar algo por lo que alguien pague, cuánto espacio hay en el mercado (más compradores que vendedores) y cuánto dura y crece el negocio sin que una plataforma se lo lleve por delante. La lista va del peor al mejor negocio para construir a largo plazo. Eso no es lo mismo que el mejor para empezar: el primer lugar exige una experiencia que nadie tiene el primer día, y algunos negocios del final de la lista son excelentes para dar el primer paso. La regla que aparece al final es sencilla: abajo vendes lo que construyes, que cada mes cuesta menos; arriba vendes tu criterio, que cada vez vale más. Por eso, la segunda parte es una escalera de cuatro peldaños, con un test de 6 preguntas para encontrar el tuyo, la oferta lista de cada negocio, ejemplos por sector y un plan de 90 días. Los valores en reales son rangos de referencia de lo que se cobra, no una promesa de ingresos.

## 📖 Página

- Ranking de los 13 negocios: **https://inematds.github.io/negocios-com-ia/guia/es/**
- Video (16:9 y short, en portugués): **https://inematds.github.io/negocios-com-ia/videos/**
- Escalera, test y plan de 90 días: **https://inematds.github.io/negocios-com-ia/guia/es/escada/**

(Exigencia técnica / Espacio en el mercado / Durabilidad y crecimiento)

13. 📱 **Aplicación por suscripción con IA (SaaS)** — 4/1/3
12. 🎬 **Canal sin rostro creado con IA** — 2/2/1
11. 🌐 **Sitios web para empresas creados con IA** — 1/2/1
10. 🧩 **Centro de IA de la empresa** — 3/4/2
9. 🔎 **Aparecer en las respuestas de la IA (GEO)** — 2/3/2
8. ⚙️ **Automatización e integración** — 2/3/2
7. 🎓 **Talleres de IA para equipos** — 3/3/3
6. 📞 **Recepcionista y atención al cliente con IA** — 3/4/2
5. 🎨 **Estudio creativo con IA** — 3/4/3
4. 🎯 **Generación de clientes potenciales (leads) con IA** — 4/3/5
3. 🎙️ **Educación y marca personal** — 3/3/5
2. 🩺 **Consultoría y diagnóstico de IA** — 3/4/4
1. 🧭 **Director de IA (en una empresa o fraccionado)** — 4/5/5

## Cómo está organizado

- `conteudo/pt.json` (+ `en.json`, `es.json`) — negócios, notas, degraus, teste, setores, plano.
- `conteudo/imagens.json` + `scripts/gerar-imagens.sh` — imagens (Codex image_gen).
- `scripts/traduzir.sh` — EN/ES pelo tradutor central `inema-traduz`.
- `scripts/build.py` — gera `guia/`, `guia/escada/` e `en/`, `es/`.

## El proceso, de principio a fin

1. 🧠 Sessão com o Nei: escolher os negócios, as notas e escrever `conteudo/pt.json`.
2. 🧠 Descrever as cenas em `conteudo/imagens.json`.
3. ⚙️ `scripts/gerar-imagens.sh` — Codex gera as 13 imagens (4 em paralelo).
4. ⚙️ `scripts/traduzir.sh` — `inema-traduz` traduz para EN e ES e confere a estrutura.
5. ⚙️ `gerar-banner.sh` (skill projetos-landing-guia) — banners live e grade PT/EN/ES.
6. ⚙️ `python3 scripts/build.py` — monta ranking e escada nos 3 idiomas.
7. 🧠 Conferir no navegador (360 px a 1920 px, teste e abas) e `git push` (GitHub Pages).
8. 🤖 Explicavideo 16:9 + 9:16 (`roda_ev.sh`, avatar no estúdio HeyGen) → lives1 + Metricool inematds.
9. 🧠 Portal (inema.club), área no eventos e tópico no Telegram INEMA.IA.
