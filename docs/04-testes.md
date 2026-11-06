# Verificação da homologação — 5 de novembro de 2026

## Resultados executados

- Python 3.12.14, Node 24.22.1, Chromium do ambiente, Playwright local.
- Servidor HTTP estático iniciado na raiz do checkout; requisições funcionais locais.
- Smoke: 8 páginas × 4 larguras (360, 390, 768 e 1440px) = 32 combinações aprovadas.
- Em cada combinação: HTTP 200, lang=en-US, um H1, canonical correto, ausência de
  rolagem horizontal, navegação local e âncoras válidas; sem erros JavaScript de página.
- FAQ nativo abre; âncora de checklist navega. Testado também sem JavaScript.
- Os dois CTAs do guia preservam exatamente URL/parâmetros e rel=sponsored.
- Sem consentimento: nenhuma solicitação de tag. Aceite: uma tag com ID original.
  Clique: um evento local com destino original, placement e rótulo de saída, sem valor
  monetário ou transaction_id. Persistência e retirada de consentimento verificadas.
- Rede externa interceptada nos testes de eventos. Não houve conversão real enviada,
  compra, abertura do checkout de afiliado ou verificação de atribuição de comissão.
- Axe-core: 8 páginas × 2 larguras (390/1440), zero violações nos critérios automatizados
  WCAG 2 A/AA e 2.1 A/AA examinados. Inclui painel de privacidade aberto.
- HTML Validate: oito documentos aprovados após corrigir nomes de landmarks e elementos
  decorativos. JavaScript passou no node --check.
- Lighthouse mobile no guia: Performance 100, Accessibility 100, Best Practices 100,
  SEO 100. FCP 0,8s; LCP 0,9s; CLS 0; TBT 0ms. Uma medição de laboratório local,
  sem consentimento de publicidade; não representa experiência de produção ou campo.
- Assets carregados na página: CSS/JS locais e desenho HTML/CSS original. Nenhum img
  de avaliação/antes-depois está referenciado. Imagem social PNG original preparada.
- Check de publicação falha intencionalmente em seis páginas com dados pendentes.
- Leitura GitHub pelo proxy existente passou: HEAD remoto igual ao commit original.
  Nenhum token solicitado. Primeiras tentativas dentro do sandbox falharam por acesso
  ao socket; com execução autorizada o Git e a instalação de ferramentas funcionaram.

## Evidências

JSON e capturas reais em `/workspace/reports/mega7/`:
`smoke-results.json`, `axe-results.json`, `lighthouse-mobile.json`,
`home-360.png`, `home-390.png`, `home-768.png`, `home-1440.png`,
`prodentim-360.png`, `prodentim-390.png`, `prodentim-768.png`, `prodentim-1440.png`.
Capturas geradas após recusar medição, com primeira resposta do FAQ aberta no guia.

## Limitações e verificações pendentes

- Firefox e Safari/WebKit não executados; apenas Chromium real do ambiente.
- Não houve teste com leitor de tela nem inspeção em aparelhos físicos.
- Axe e Lighthouse não certificam acessibilidade integral nem conformidade legal.
- Não houve consulta a CrUX/Search Console, teste de indexação pública ou validação
  do domínio em produção; nenhuma alteração foi publicada.
- NIH, Google Ads policies e página pública do vendedor responderam bloqueio de túnel
  403 no proxy. Isso é bloqueio de acesso do ambiente, não diagnóstico dos sites.
  Novos domínios foram adicionados somente ao rascunho; aplicação em runtime não comprovada.
- Termos de afiliado, rótulo, condições de compra, direitos de imagens originais,
  legitimidade de avaliações e compra/conversão real continuam não verificados.
- Nenhum teste de segurança independente ou auditoria jurídica foi realizado.
- Ferramentas de auditoria são dependências de desenvolvimento externas ao site;
  avisos de depreciação npm não foram ocultados. Aplicação não exige dependências npm.

## Atualização — imagens e identidade do produto

As duas fotos existentes do ProDentim agora aparecem na home e no guia: destaque do
frasco com folhas/morangos e detalhe das embalagens. Arquivos copiados sem alterar a
imagem ou seu rótulo; originais preservados. Layout com verde botânico e tipografia
que acompanha a embalagem, mantendo Mega7Products como identidade do site.
Dimensões explícitas, alt descritivo, prioridade no hero e lazy loading na imagem secundária.
Backup antes desta revisão: /workspace/backups/prodentim-before-product-visuals.tar.gz.
Reexecutados: 32 verificações de página/tela aprovadas; fotos carregadas; HTML válido;
16 auditorias axe sem violações. Capturas atualizadas nos mesmos caminhos de evidência.
Nova medição de desempenho em lighthouse-product-images.json; a medição anterior
lighthouse-mobile.json corresponde à versão sem fotografias. Direitos de uso e atualidade
da embalagem permanecem itens da revisão antes da publicação.

Lighthouse local após as fotos: performance 100, accessibility 100, best-practices 100, seo 100.

## Ajuste de destaque no desktop

A foto da home foi movida da seção secundária para o hero, ao lado do título.
A apresentação do guia também foi compactada para dar prioridade ao frasco.
32 verificações de página/tela e validação HTML aprovadas novamente.
Checagem específica em 1366×768, 1440×900 e 1920×1080 confirmou a foto carregada,
inteiramente dentro da primeira tela nas duas URLs e com pelo menos 400px de largura.
Capturas: home-desktop-1366-first-screen.png e prodentim-desktop-1366-first-screen.png,
com variantes 1440 e 1920 em /workspace/reports/mega7.
Backup: /workspace/backups/prodentim-before-desktop-hero.tar.gz.
A alteração continua local, sem publicação no domínio de produção.
