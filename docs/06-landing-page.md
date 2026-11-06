# Landing page ProDentim — nova estrutura para aprovação

A versão de desenvolvimento em `/prodentim/` agora possui uma sequência comercial
contínua, sem sidebar editorial ou seções longas de artigo. A home e os documentos
institucionais não foram reconstruídos nesta revisão. A hero existente foi integrada
a um novo corpo com seis seções principais, como solicitado no novo briefing.

## Estrutura e mudanças

1. **Hero:** frasco grande, título informativo, subtítulo curto e CTA original.
2. **What is ProDentim:** apresentação objetiva atribuída ao posicionamento do vendedor,
   fotografia das embalagens e limite claro sobre teste pessoal e benefícios.
3. **Product details:** três cards visuais para ingredientes, direções e adequação pessoal.
   Não foi inventada uma fórmula: a composição atual ainda não foi verificada.
4. **Before You Buy ProDentim:** vendedor, custo total e condições de reembolso;
   bloco de transparência com contraste e identidade própria Mega7Products.
5. **FAQ:** seis respostas curtas em acordeões nativos, inclusive preço e garantia.
6. **Fechamento:** foto do produto, frase de decisão, CTA final e divulgação de afiliado.

Paleta petróleo/verde, imagens reais já existentes no checkout, ícones SVG locais,
fundos alternados e cartões com profundidade suave. Nenhum antes/depois, avaliação,
cliente ou profissional fictício. Layout mobile em coluna com fotos dimensionadas,
card de fechamento reorganizado e botões com área de toque confortável.

Os dois CTAs comerciais preservam **exatamente**:
https://prodentim24.com/text.php?aff=Saulohenri4

Menu e links informativos servem à navegação; não são botões de compra. Os CTAs usam
`rel="sponsored noopener"` e `data-placement` existentes (`hero`/`final`). O script
`assets/site.js` permanece byte a byte igual ao backup, incluindo escolha publicitária,
AW-17961565555 e AW-17961565555/98brCNTlyZ4cEPP63vRC. Clique continua sendo saída,
sem confirmação de compra. Nenhuma alteração de rastreamento ou de CNAME.

## Código

- [Landing page](/workspace/prodentim/prodentim/index.html).
- [Estilos das novas seções](/workspace/prodentim/assets/landing.css).
- [Teste de rolagem e seis seções](/workspace/prodentim/tools/landing_page.py).
- Smoke ajustado para aguardar imagens lazy fora da primeira tela antes de verificar
  seu carregamento; não foram removidas as verificações de links ou de eventos.

## Capturas reais completas

- [Desktop 1366 × 768 — página inteira](/workspace/reports/mega7/landing-v2/after-1366x768-full.png).
- [Desktop 1920 × 1080 — página inteira](/workspace/reports/mega7/landing-v2/after-1920x1080-full.png).
- [Mobile 390 × 844 — página inteira](/workspace/reports/mega7/landing-v2/after-390x844-full.png).
- [Mobile 430 × 932 — página inteira](/workspace/reports/mega7/landing-v2/after-430x932-full.png).
- Extra: largura 360 em `after-360x800-full.png` na mesma pasta.

As capturas foram renderizadas por Chromium, após recusar medição publicitária,
com FAQ fechado. A página permite rolar normalmente; não há trava de viewport.

## Testes executados

- Cinco resoluções; exatamente seis seções principais; conteúdo maior que duas telas.
- Rolagem até cada seção e até o CTA final, inclusive carregamento das imagens lazy.
- Fotos decodificadas, proporções preservadas por object-fit, WebP na hero.
- Sem rolagem horizontal nem erros JavaScript de página nas capturas.
- CTA original e final com URL exata; dimensões de toque verificadas.
- Smoke completo: 32 combinações de página/largura aprovadas, com navegação, FAQ,
  âncoras, consentimento, retirada de consentimento e payload de evento existente.
- Primeira execução do smoke identificou seletor de âncora incompatível com o menu
  antigo; o menu foi ajustado para `#checklist` e a suíte completa passou em seguida.
- Axe: 16 auditorias em oito páginas (390/1440), sem violações automatizadas encontradas.
- HTML Validate das oito páginas e git diff --check aprovados.
- Lighthouse mobile local: Performance 100, Accessibility 100, Best Practices 100,
  SEO 100; LCP 1,6s, CLS 0, TBT 0ms. É laboratório local, não métrica de campo.
- Comparação binária: script de rastreamento e CNAME intactos em relação ao backup.

Evidências: `/workspace/reports/mega7/landing-v2/checks.json`, `lighthouse.json`,
`/workspace/reports/mega7/smoke-results.json` e `axe-results.json`.
Os testes interceptam tráfego externo: não enviam conversões reais nem compram produtos.

## Pendências preservadas

Verificar direitos das imagens existentes e atualidade das embalagens; composição,
preço, garantia e termos do programa não estão confirmados. Por isso não são anunciados
como fatos. Não declaramos autorização de uso só por encontrar fotos no repositório.
Documentos institucionais seguem em rascunho até identificação e contato do operador.
Firefox/Safari, aparelhos reais, entrega de eventos ao Google e comissões não testados.
Sem certificação de acessibilidade integral ou promessa de aprovação Google Ads.

Backup anterior: `/workspace/backups/prodentim-before-six-section-landing.tar.gz`.
Nenhum arquivo importante foi excluído. Nenhuma publicação, push, DNS, campanha,
contratação ou despesa foi realizada. Versão de desenvolvimento para aprovação.
