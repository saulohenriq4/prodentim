# Auditoria antes das alterações — Mega7Products 2.1

Base: commit 93550d1, igual ao HEAD remoto main verificado nesta sessão. A página
pública não pôde ser lida: túnel HTTPS do ambiente retornou 403. As conclusões
abaixo se referem ao checkout publicado e à renderização local, não a observações
de tráfego real. Branch development/mega7products-2-1; backup completo anterior:
/workspace/backups/prodentim-v2-0-before-v2-1.tar.gz.

## Confirmado antes de alterar a aplicação

- Seis seções, página contínua: 4.069px em 1366px e 5.504px em mobile de 390px.
- Somente dois CTAs: hero e fechamento. Em 390px a seção final começa em y=4.383px.
  Existe uma longa leitura sem acesso direto à oferta. Não há dados que comprovem
  impacto disso em conversão; é uma hipótese de melhoria de distribuição.
- Foto na hero, apresentação e fechamento. Nenhuma fotografia em Product Details,
  Before You Buy ou FAQ. Highlights+Before You Buy somam cerca de 1.865px no mobile.
- A fórmula atual não foi verificada. Imagens de frutas e ervas como ingredientes
  seriam indevidas. A foto existente de hero contém elementos botânicos; não devem
  ser apresentados como uma composição verificada nem reutilizados como ingredientes.
- Imagem principal 815×621, WebP 48.748 bytes, com JPEG fallback e prioridade alta.
  Secundária JPEG 404×316, 51.159 bytes. Não ampliar detalhes além da resolução nativa.
- Disclaimer sobre não testar pessoalmente aparece na faixa de transparência,
  apresentação e FAQ. Limitações e termos de compra também se repetem. Há espaço
  para texto mais direto mantendo informação material em contexto adequado.
- Páginas institucionais finalizadas: Mega7Products e mega7products2@gmail.com.
  Não restam marcadores PENDING/DRAFT em HTML. Sem informações de empresa inventadas.
- en-US, um H1, canonical correto, metadados e OG existentes. Sitemap contém oito URLs;
  robots permite rastreamento. Não há estrelas nem avaliações estruturadas falsas.
- Navegação local, links internos e âncoras passam no smoke. Domínios externos e
  entrega de email não foram validados. Mailto não é prova de caixa postal ativa.
- Google Ads carrega apenas após aceite. A ação conversion enviada é clique de saída,
  sem valor/transação. Nenhuma integração confirma chegada ao vendedor ou venda.
- CSS acumulado usa três folhas, com regras históricas de layouts não utilizados.
  Não há necessidade de reescrever a base para esta melhoria incremental.

## Verificações iniciais executadas

32 combinações de página/largura aprovadas: carregamento, navegação, imagens, FAQ,
consentimento, retirada, payload original de clique e funcionamento sem JavaScript.
Cinco capturas de página completa geradas: 360×800, 390×844, 430×932, 1366×768,
1920×1080. Sem rolagem horizontal ou erros JavaScript detectados. Evidências em
/workspace/reports/mega7/v2-1/before (checks, smoke-results e audit-metrics).

O teste anterior de Lighthouse da 2.0 marcou 100 nas quatro categorias, LCP 1,6s,
CLS 0. Esse é um resultado histórico de laboratório; a 2.1 será medida novamente.
INP de campo não está disponível. Não foram alegados volumes, CPC ou resultados CRO.

## Melhorias propostas

1. Manter a hero e a estrutura; refinar seu enquadramento sem alterar pixels do rótulo.
2. Encurtar apresentação, cartões e FAQ; evitar avisos repetidos sem esconder limites.
3. Ter três CTAs exatos: hero, após Product Details e fechamento, todos no mesmo link.
4. Adicionar contexto visual de embalagem em Before You Buy com foto existente.
5. Otimizar a foto secundária em WebP e manter lazy loading abaixo da hero.
6. Preservar páginas institucionais, contato, CNAME e script de publicidade.
7. Documentar fotos futuras necessárias: frasco isolado atual e painel traseiro legível,
   com autorização. Não inventar um rótulo para preencher esse espaço agora.
8. Medir e entregar antes/depois sem publicar ou modificar campanhas.
