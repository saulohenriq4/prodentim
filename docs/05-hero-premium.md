# Refinamento premium da hero — versão para aprovação

A implementação editorial existente foi refinada, sem reconstruir o site. Alterações
principais no guia /prodentim/; a home compartilha a melhoria de marca e a fonte WebP.

## Antes e depois

| Aspecto | Antes | Agora |
| --- | --- | --- |
| Foto no desktop 1366 | 484 × 369 px | 599 × 457 px, cerca de 24% mais larga |
| Composição desktop | Foto em cartão com título duplicado | Foto protagonista, menos moldura, profundidade sutil |
| Mobile | Texto, CTA e depois fotografia | Título, produto, CTA e informação complementar |
| Botão principal | 54 px de altura | 60 px no desktop e 58 px no mobile |
| Marca no cabeçalho | 18 px, peso misto | 21 px no desktop e 20 px no mobile, com mais contraste |
| Arquivo da foto | JPEG, 56.613 bytes | WebP, 48.748 bytes (13,9% menor), com fallback JPEG |

Mantidos título informativo, CTA solicitado, transparência, identidade petróleo/verde,
embalagem e rótulo da foto existente. Não foram gerados frascos, ingredientes ou selos.
A conversão WebP altera somente a codificação; dimensões 815 × 621 e proporção mantidas.
A foto é exibida abaixo de sua resolução nativa. Não existe detalhe que ultrapasse a
qualidade do arquivo original; não foi usado upscaling generativo.

## Capturas reais

Arquivos em `/workspace/reports/mega7/premium-hero/`, gerados com Chromium local.
As capturas finais mostram a página após recusar medição publicitária, sem banner aberto.

- Antes desktop: [1366 × 768](/workspace/reports/mega7/premium-hero/before-desktop-1366.png).
- Antes mobile: [captura completa em largura 390](/workspace/reports/mega7/premium-hero/before-mobile-390.png).
- Depois: [1366 × 768](/workspace/reports/mega7/premium-hero/after-1366x768.png).
- Depois: [1920 × 1080](/workspace/reports/mega7/premium-hero/after-1920x1080.png).
- Depois: [390 × 844](/workspace/reports/mega7/premium-hero/after-390x844.png).
- Depois: [430 × 932](/workspace/reports/mega7/premium-hero/after-430x932.png).
- Extra: [360 × 800](/workspace/reports/mega7/premium-hero/after-360x800.png).

## Arquivos modificados nesta revisão

- `prodentim/index.html`: classe de refinamento, título e picture com fallback.
- `index.html`: inclusão da folha visual compartilhada e WebP com fallback.
- `assets/hero.css`: refinamento visual isolado, responsivo e sem animações novas.
- `assets/prodentim-product.webp`: versão otimizada da imagem existente.
- `tools/premium_hero.py`: verificações e capturas específicas.
- Este relatório. `assets/site.css` e `assets/site.js` não foram modificados nesta revisão.

## Testes executados

- Cinco resoluções: 1366×768, 1920×1080, 360×800, 390×844 e 430×932.
- Imagem carregada e WebP selecionado; dimensões nativas confirmadas.
- Foto inteiramente visível na primeira tela desktop; sem rolagem horizontal.
- Mobile: separação entre título, foto e botão, CTA ≥48px e dentro da primeira tela
  nas três resoluções após fechar a escolha publicitária.
- Inspeção visual das capturas de desktop e mobile: rótulo sem distorção, textos
  legíveis e ausência de cortes nas áreas principais.
- 32 combinações de página/tela do smoke aprovadas; links, âncoras e FAQ funcionais.
- URL de afiliado preservada exatamente. Payloads de evento existentes aprovados
  com tráfego externo interceptado; não enviadas conversões reais.
- Nenhum erro JavaScript de página nas verificações. HTML Validate aprovado nas oito páginas.
- Axe: 16 auditorias, zero violações automatizadas nos critérios WCAG examinados.
- Lighthouse mobile local: 100 em performance, acessibilidade, boas práticas e SEO.
  LCP 1,5s; CLS 0; TBT 0ms. Resultado de laboratório, não Core Web Vitals de campo.
- Comparação binária com backup: JavaScript de rastreamento e CNAME intactos.
- `git diff --check` aprovado. Nenhuma instalação de nova integração ou tag.

Evidência técnica: `checks.json` e `lighthouse.json` na pasta das capturas.

## Pendências e limites

Confirmar direitos de uso e atualidade da imagem original com o responsável; o fato
de estar no repositório não prova autorização do fabricante. Documentos institucionais,
termos do programa de afiliado e verificações externas seguem pendentes conforme os
relatórios anteriores. Firefox, Safari e aparelhos físicos não foram testados. Auditoria
automatizada não comprova conformidade integral de acessibilidade ou de publicidade.

Backup antes da revisão: `/workspace/backups/prodentim-before-premium-hero.tar.gz`.
Nenhuma publicação, alteração de DNS, campanha ou despesa foi realizada.
