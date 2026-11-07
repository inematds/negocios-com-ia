#!/usr/bin/env bash
# Traduz conteudo/pt.json para en/es pelo tradutor central (inema-traduz). Uso: scripts/traduzir.sh [en es]
set -u; cd "$(dirname "$0")/.."
for L in "${@:-en es}"; do for l in $L; do
  case $l in en) nome="inglês (público global)"; moeda="mantenha os valores em reais (R\$) como estão, porque são do Brasil, e acrescente '(Brazil)' só na primeira menção no campo ui.aviso";; es) nome="espanhol neutro da América Latina"; moeda="mantenha os valores em reais (R\$) como estão, porque são do Brasil, e acrescente '(Brasil)' só na primeira menção no campo ui.aviso";; esac
  { echo "Traduza este JSON para $nome. Regras: devolva SOMENTE o JSON válido, sem comentário e sem cercas de código; mesma estrutura, mesmas chaves, mesma ordem; não traduza chaves, ids, emojis, URLs, números, os campos \"t\":\"projeto\"/\"curso\" nem nomes de projeto em minúsculas com hífen (ex.: site-inspirado); mantenha tags HTML como <span class=\"amb\">; troque \"lang\" para \"$l\"; $moeda. Nomes de cursos podem ser traduzidos. WhatsApp, ChatGPT, Gemini, Claude e Perplexity ficam iguais."; echo; cat conteudo/pt.json; } | inema-traduz > conteudo/$l.raw
  python3 - "$l" <<'PY'
import json,sys,re
l=sys.argv[1]; s=open(f'conteudo/{l}.raw').read()
s=s[s.index('{'):s.rindex('}')+1]; d=json.loads(s); p=json.load(open('conteudo/pt.json'))
assert len(d['negocios'])==len(p['negocios']) and len(d['teste'])==len(p['teste']) and set(d['ui'])==set(p['ui']), 'estrutura diferente'
for a,b in zip(d['negocios'],p['negocios']): assert a['id']==b['id'] and a['notas']==b['notas'] and [r['url'] for r in a['rel']]==[r['url'] for r in b['rel']]
for a,b in zip(d['teste'],p['teste']):
  for x,y in zip(a['op'],b['op']): assert x['s']==y['s']
json.dump(d,open(f'conteudo/{l}.json','w'),ensure_ascii=False,indent=1); print('ok',l)
PY
done; done
