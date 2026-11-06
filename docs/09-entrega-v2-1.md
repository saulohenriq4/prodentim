# Mega7Products 2.1 — entrega para revisão

Implementação incremental na branch `development/mega7products-2-1`, baseada no commit
93550d1 da versão publicada. Nenhum push, deploy, anúncio, DNS ou configuração crítica
foi alterado nesta tarefa. Backup: `/workspace/backups/prodentim-v2-0-before-v2-1.tar.gz`.
Auditoria inicial feita antes das alterações em `docs/08-auditoria-v2-1.md`.

## Resultado

Mantidas as seis seções, identidade editorial, tipografia e paleta. A hero mantém a
composição aprovada, com fotografia ligeiramente maior no desktop (599→617px em 1366px)
e proporção original. Nenhum detalhe do rótulo foi redesenhado. O mobile preserva a
ordem título/produto/CTA e o primeiro botão visível na primeira tela após fechar a escolha
publicitária nas resoluções testadas.

A apresentação agora tem título direto e texto mais curto, com três informações de
formato/posicionamento. Product Details usa textos mais objetivos e não afirma fórmula
não verificada. Removidos avisos repetidos na apresentação e FAQ; permanecem divulgação
clara antes da hero, informação sobre fórmula e adequação, aviso de saúde e documentos
institucionais. A FAQ passou de seis para cinco perguntas.

Os CTAs são exatamente três, com textos distintos e comportamento consistente:

| Local | Texto | Placement |
| --- | --- | --- |
| Hero | View Current Product Details | hero |
| Após Product Details | Explore the Current Offer | details |
| Fechamento | Check the Seller’s Current Offer | final |

Todos usam `https://prodentim24.com/text.php?aff=Saulohenri4`, sem novos parâmetros,
com `rel="sponsored noopener"`, mesma aba e altura mínima de 58px. Não há botão fixo,
pop-up comercial, escassez ou desconto inventado. A nova distribuição é uma hipótese
CRO; não existem dados de A/B ou evidência de aumento de vendas.

## Comparação mensurada

| Aspecto | 2.0 | 2.1 |
| --- | --- | --- |
| CTAs comerciais | 2 | 3 |
| Imagens nas seis seções | 3 | 4 |
| Before You Buy | Apenas texto | Referência visual da embalagem + checklist |
| FAQ | 6 perguntas | 5 perguntas, respostas mais curtas |
| Altura desktop 1366 | 4.069px | 4.295px |
| Altura mobile 390 | 5.504px | 5.747px |

Os textos foram encurtados, mas a página ficou cerca de 4–6% mais alta por incorporar
a nova foto e o CTA intermediário. Não se alega redução da altura total. O benefício
proposto é intercalar informação, produto e decisão, não remover conteúdo essencial.

## Capturas completas e comparação

- [Comparação visual antes/depois](/workspace/reports/mega7/v2-1/comparison.html).
- [Desktop 1366×768 completo](/workspace/reports/mega7/v2-1/after/after-1366x768-full.png).
- [Desktop 1920×1080 completo](/workspace/reports/mega7/v2-1/after/after-1920x1080-full.png).
- [Mobile 360×800 completo](/workspace/reports/mega7/v2-1/after/after-360x800-full.png).
- [Mobile 390×844 completo](/workspace/reports/mega7/v2-1/after/after-390x844-full.png).
- [Mobile 430×932 completo](/workspace/reports/mega7/v2-1/after/after-430x932-full.png).

Capturas reais de Chromium local, com FAQ fechado e escolha de publicidade recusada.
Referências anteriores preservadas na pasta `before`, novas na pasta `after`. A comparação
não usa imagens geradas ou simulações do site.

## Relatório das imagens

Imagem pública usada: `assets/prodentim-product.webp`, 815×621, 48.748 bytes, derivada
da fotografia JPEG de 56.613 bytes já usada na 2.0. Hero, apresentação e referência de
compra usam picture com fallback JPEG; a imagem final mantém o WebP da versão anterior.
O navegador reutiliza o mesmo arquivo: quatro posições não exigem quatro downloads.
Hero usa prioridade alta; abaixo dela as imagens têm lazy loading, dimensões e alt.

A foto antiga de três frascos permanece preservada no repositório, mas saiu da landing
para não misturar apresentações de embalagem. Sua conversão WebP foi avaliada e depois
descartada por não ser usada. Não foram criados frascos, pessoas, resultados ou selos.
Não há imagens de ingredientes em Product Details. As folhas/frutas que já fazem parte
da fotografia original não são declaradas ingredientes; a legenda da apresentação
explicita que a imagem não constitui uma lista de composição verificada.

### Arquivos futuros desejáveis

- `assets/prodentim-front-current.webp`: foto atual autorizada do frasco isolado, sem
  elementos botânicos adicionados, ao menos 1200px de largura. Substituição nos pictures
  existentes da hero/apresentação/fechamento, com dimensões reais atualizadas.
- `assets/prodentim-label-current.webp`: foto autorizada do painel atual e legível,
  ao menos 1600px de largura. A figura `.lp-label-reference` em Before You Buy já é
  o espaço de substituição; não foi criado um rótulo fictício ou campo vazio público.
- Documento do fabricante com composição, data/versão e permissão de uso das fotos.
  Só depois criar fotografias específicas de ingredientes ou citar a composição.

Os arquivos acima não existem ainda e não são referenciados por URLs quebradas.
A origem/autorização e atualidade da foto preexistente ainda precisam ser confirmadas
pelo responsável. A presença no repositório não comprova licença.

## SEO e performance

Title, H1 e canonical preservados; description e OG description ajustadas ao fluxo
mais direto. en-US, um H1, H2/H3, alt, sitemap com oito URLs e robots existentes
validados. Nenhuma estrela, avaliação ou dado estruturado fictício. Home, páginas
institucionais, contato, sitemap, robots, CNAME e script de publicidade permanecem
byte a byte iguais à base. Uma folha pequena e específica isola os ajustes 2.1;
nenhuma biblioteca ou JavaScript de aplicação foi adicionado.

Lighthouse mobile local final: Performance 100, Accessibility 100, Best Practices 100,
SEO 100. LCP 1,5s; CLS 0; TBT 0ms. Resultados de uma execução de laboratório local,
sem tag publicitária carregada. **INP de campo não foi medido**: não há dados RUM/CrUX
nem acesso a tráfego real. TBT não é um substituto que comprove INP.

## Testes

- Antes: 32 combinações de página/largura e capturas em cinco resoluções.
- Depois: mesmas 32 combinações, seis seções contínuas, três CTAs e fotografia em
  Before You Buy; todas as imagens decodificadas e navegação local aprovada.
- Cinco resoluções exigidas: 360×800, 390×844, 430×932, 1366×768 e 1920×1080.
- Sem rolagem horizontal ou erros JavaScript de página; botões ≥48px; produto não
  recortado no desktop. Inspeção visual das capturas completas desktop e mobile.
- HTML Validate das oito páginas, check_release.py e git diff --check aprovados.
- Axe: 16 auditorias em oito páginas (390/1440), zero violações automatizadas nos
  critérios WCAG examinados. Isso não é uma certificação integral de acessibilidade.
- Teste de cada um dos três placements: um evento por clique com ação e ID exatos,
  sem valor monetário ou transaction_id. Aceite/recusa/retirada e navegação sem JS
  verificados. Tráfego Google/vendedor interceptado; não enviadas conversões reais.
- Comparação binária de 11 arquivos confirma preservação de home, seis páginas
  institucionais, CNAME, sitemap, robots e assets/site.js.

Evidências em `/workspace/reports/mega7/v2-1/after`: smoke-results.json, checks.json,
audit-metrics.json, axe-results.json e lighthouse.json.

## O que cada sinal permite concluir

| Sinal | Significado | Limite |
| --- | --- | --- |
| Visita ao site | Documento local pode ser aberto; com consentimento a tag é inicializada | Não equivale a clique ou compra |
| Clique de afiliado | Evento `conversion`, rótulo `outbound_affiliate_click` e placement | O nome histórico conversion não o torna venda |
| Acesso ao vendedor | O link inicia navegação para o destino original | Não há confirmação de chegada/checkout no nosso domínio |
| Venda atribuída | Transação confirmada pela plataforma de afiliados | Não existe integração de venda nesta página |

IDs preservados: AW-17961565555 e AW-17961565555/98brCNTlyZ4cEPP63vRC. O script
não foi alterado; o CTA novo é atendido pelo mesmo listener genérico e acrescenta
apenas placement=details ao evento já existente. Nenhum objetivo de campanha, lance,
orçamento ou tag foi modificado. Cliques não devem ser usados como compras confirmadas.

## Limitações e próximos passos

- Consulta ao domínio público bloqueada pelo proxy 403; main remoto coincidiu com a
  base da auditoria. Não afirmamos teste de produção nesta tarefa.
- Autorização e atualidade de fotos, fórmula, preços, garantia e restrições oficiais do
  afiliado permanecem sem verificação externa. Não foram anunciados como confirmados.
- Regras de marca/PPC e políticas Google precisam ser verificadas antes de anúncios.
  Não foi ativada campanha nem prometida aprovação. R$20/dia é planejamento futuro,
  não gasto, projeção de CPC ou promessa de comissão.
- Firefox/Safari, aparelhos físicos, leitores de tela, INP real e entrega do email não
  testados. Não houve venda real, validação de atribuição ou teste A/B.
- Revisar esta versão e autorizar separadamente sua publicação. A 2.1 não foi enviada
  para main, e a versão 2.0 publicada foi preservada.
