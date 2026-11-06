# Entrega, rastreamento e publicação segura

## Implementação

- Branch local `development/mega7products-2`; nenhuma publicação, push, compra ou anúncio.
- Backup anterior a todas as alterações em `/workspace/backups/prodentim-before-mega7-20261105.tar.gz`,
  com checkout e metadados Git. Não restaurar sobre trabalho posterior sem preservar esse trabalho.
- Home original substituída por home Mega7Products; /prodentim/ mantém a URL do guia.
- Paleta petróleo/verde suave, fontes do sistema, desenho editorial feito com HTML/CSS,
  sem atribuir aparência oficial ao produto. Sem assets externos novos ou imagens de terceiros novas.
- CTAs limitados ao hero e conclusão; FAQ com details/summary; navegação funciona sem JS.
- Sem afirmações de eficácia, prova social fictícia, escassez ou preços não comprovados.
- Canonicals distintos, en-US, descrição/title únicos, Open Graph e imagem social própria,
  favicon, robots e sitemap (apenas duas URLs editoriais). Nenhuma avaliação estruturada.
- Foco visível e suporte a movimento reduzido. Sem novas integrações de publicidade.
- Seis páginas institucionais preparadas em inglês, com [PENDING], banner e noindex/nofollow.
  Elas não são documentos finais nem devem ser publicadas. Noindex não controla acesso público.

## Rastreamento

Preservados, sem mudar parâmetros:
- Link: https://prodentim24.com/text.php?aff=Saulohenri4
- Google Ads: AW-17961565555
- Ação: AW-17961565555/98brCNTlyZ4cEPP63vRC

Antes: tag carregada automaticamente; todos os botões disparavam `conversion`.
Agora: a tag existente só carrega após “Allow ads measurement”. Recusar permite navegar
sem carregá-la. Não há GA4, CMP externa ou nova tag. A preferência é guardada em localStorage
(`mega7-ads-choice-v1`); se indisponível, a escolha vale só na página corrente.
Sem JS não há medição, mas links continuam funcionando.

Ao clicar em `.affiliate`, com consentimento, o evento continua chamado `conversion`,
com `send_to` original, `event_label=outbound_affiliate_click` e `placement=hero|final`.
Não há valor monetário, moeda ou transaction_id. Não se impede a navegação nativa.
Por isso, bloqueadores ou navegação rápida podem impedir entrega: contagem não garantida.
Reabrir escolhas fica no rodapé. Retirar consentimento recarrega a página para interromper
a tag; não apaga cookies de terceiros nem dados já enviados. A solução precisa de revisão
jurídica e das configurações de privacidade do Google antes de produção.

**Clique de saída não é compra, receita ou comissão.** Configurar essa ação como secundária
(observação), excluí-la dos objetivos de compra/lances e nomeá-la claramente na conta Google
Ads requer acesso à conta e decisão do responsável. Nenhuma configuração da conta foi alterada.
Compra somente poderá ser medida após validação de integração autorizada, consentimento,
atribuição e deduplicação de transações na Digistore24. Não adicionar postback ou novas tags
sem aprovação. Os testes atuais interceptam rede e comprovam o payload local, não entrega real.

## Pendências antes de publicação

1. Preencher nome real do operador e canal público de contato; revisar privacidade/termos
   e práticas de hospedagem, retenção, direitos e transferências com o responsável.
2. Verificar regras oficiais atuais do afiliado, permissão de anúncios, uso da marca e
   conteúdo da oferta. Validar checkout, rótulo, ingredientes e termos se forem citados.
3. Revisar fonte NIH e políticas Google: consultas atuais negadas pelo proxy (403).
4. Revisar rascunhos, retirar marcadores somente depois da resolução; ajustar noindex e sitemap
   para documentos finalizados. Executar `python3 tools/check_release.py` até passar.
5. Validar Safari/WebKit e Firefox, leitores de tela e dispositivos reais. Medir campo após
   produção: dados de laboratório não comprovam Core Web Vitals de usuários reais.
6. Validar a ação Google Ads como clique secundário, nunca venda presumida.
7. Obter aprovação explícita do proprietário para a versão concreta antes de publicar.

## Publicação após aprovação

- Confirmar no GitHub Settings/Pages qual branch/diretório publica o domínio; não presumir
  que a branch de desenvolvimento será publicada. Rever diff e conferir CNAME preservado.
- Criar backup da versão que estiver em produção nesse momento.
- Executar smoke, axe, HTML e check_release. Revisar a versão final dos textos institucionais.
- Só então fazer revisão/merge e deploy pelo fluxo aprovado. Não alterar DNS nem CNAME.
- Depois verificar HTTPS, /, /prodentim/, links, canonical, robots e sitemap no domínio real;
  testar publicidade sem gerar conversões falsas. Solicitar indexação somente quando adequado.
- Se houver defeito, reverter pelo histórico Git no fluxo de publicação aprovado, preservando
  o backup e sem excluir branches. Não aplicar comandos destrutivos de restauração.

## Experimentos futuros

Usar atributos `data-placement` para distinguir CTAs em observação. Experimento futuro
pode variar um título ou texto de CTA por vez, com hipótese e janela previamente definidas.
Avaliar cliques como métrica intermediária e comissões verificadas como resultado. Não há
plataforma de testes instalada nem resultados A/B alegados.

## Escolha visual final do proprietário

O proprietário escolheu o primeiro redesign como base, mantendo a foto do último layout.
Restaurados o HTML editorial do guia, as cores azul-petróleo, a tipografia e os componentes
originais do redesign. A foto do frasco com folhas/morangos substitui o cartão ilustrado.
Na home, a mesma foto permanece ao lado do título para aparecer na primeira tela do desktop.
A seção adicional com três frascos foi retirada para respeitar a composição inicial escolhida.
Os arquivos de imagem e todo o trabalho anterior permanecem preservados nos backups.
Backup desta revisão: /workspace/backups/prodentim-before-editorial-return.tar.gz.
As capturas de revisão foram atualizadas. Nenhuma alteração foi publicada.
