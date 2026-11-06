# Mega7Products 2.0

Homologação editorial estática, em inglês americano. Sem framework, build de aplicação,
fontes remotas ou dependências de produção. Hospedagem de destino: GitHub Pages no
**domínio próprio mega7products.com**, com a raiz deste checkout publicada na raiz do domínio.
Caminhos absolutos intencionais; um preview em /nome-do-repo/ precisa de adaptação de base.

## Desenvolvimento local

```sh
cd /workspace/prodentim
python3 -m http.server 8000 --bind 127.0.0.1
```

Abra o site no navegador local do ambiente. O onboarding usa requisições internas;
não existe preview público publicado. Processos devem ser reiniciados em novas sessões.
Nenhum segredo, banco de dados ou serviço de backend é necessário.

## Validação

Ferramentas de auditoria instaladas fora do checkout em `/workspace/tooling/mega7`;
`package.json` e `package-lock.json` nesse diretório fixam as versões.

```sh
npm ci --prefix /workspace/tooling/mega7 --no-fund
node --check assets/site.js
python3 tools/smoke.py
node tools/accessibility.cjs
/workspace/tooling/mega7/node_modules/.bin/html-validate index.html */index.html
CHROME_PATH=/usr/bin/chromium /workspace/tooling/mega7/node_modules/.bin/lighthouse http://127.0.0.1:8000/prodentim/ --chrome-flags='--headless --no-sandbox' --only-categories=performance,accessibility,seo,best-practices --output=json --output-path=/workspace/reports/mega7/lighthouse-mobile.json --quiet
python3 tools/check_release.py
```

O smoke usa Python Playwright fornecido pelo ambiente e Chromium em `/usr/bin/chromium`.
Os testes de eventos interceptam tráfego externo: não enviam conversões reais.
O último comando impede a liberação enquanto houver marcadores de rascunho nas páginas.
Ele é um check manual; não impede sozinho um push ou publicação no GitHub Pages.

## Arquivos e entrega

- `index.html`: home editorial distinta.
- `prodentim/index.html`: guia com link de afiliado preservado.
- `assets/`: CSS, JavaScript, favicon e imagem social original.
- Seis diretórios institucionais finalizados com contato público e incluídos no sitemap.
- `docs/01-auditoria-original.md`: diagnóstico antes da reformulação.
- `docs/02-entrega-e-publicacao.md`: alterações, rastreamento e publicação segura.
- `docs/03-google-ads.md`: plano sem campanhas ativas.
- `docs/04-testes.md`: resultados e limitações reais.

**A publicação anterior foi autorizada para a versão 2.0. A versão 2.1 está em desenvolvimento e exige nova autorização antes de publicar.**
O CNAME e os arquivos originais de imagens foram preservados. As duas imagens existentes do produto são usadas na nova apresentação; imagens de antes/depois e avaliações continuam fora da página. Confirmar direitos de uso e atualidade da embalagem antes de publicar.

## Versão atual da landing ProDentim

A versão atual possui seis seções contínuas, fotos do produto e rolagem vertical.
Consulte `docs/06-landing-page.md` para a entrega mais recente e capturas completas.
Com o servidor local iniciado, `python3 tools/landing_page.py` verifica as seis seções
em cinco resoluções e gera evidências em `/workspace/reports/mega7/landing-v2`.
Relatórios anteriores descrevem versões históricas preservadas nos backups.

## Mega7Products 2.1 — versão para revisão

Branch `development/mega7products-2-1`. Auditoria anterior às alterações em
`docs/08-auditoria-v2-1.md`; entrega, imagens, rastreamento e testes em
`docs/09-entrega-v2-1.md`. Capturas antes/depois em `/workspace/reports/mega7/v2-1`.
Três CTAs e a mesma ação de clique; isso não mede vendas.
Com o servidor da aplicação ativo, execute:

```sh
python3 tools/smoke.py
python3 tools/landing_page.py
```

Os relatórios desses dois testes vão para `/workspace/reports/mega7/v2-1/after`.
Use `MEGA7_TEST_URL` ou `MEGA7_REPORT_DIR` para alterar endereço/pasta de evidências.
A versão 2.1 não foi publicada e a branch main permanece na versão anterior.
