# Preparação da publicação autorizada

O proprietário autorizou explicitamente a publicação nesta conversa. Nome público:
Mega7Products. Contato público final: mega7products2@gmail.com (substitui o endereço
contact@mega7products.com informado inicialmente).

As seis páginas institucionais foram finalizadas com as informações fornecidas,
sem inventar empresa registrada, endereço físico ou jurisdição. Removidos avisos de
rascunho e noindex; sitemap inclui as oito URLs. Privacidade descreve GitHub Pages,
Google Ads existente, preferência local, correspondência, direitos e provedores.
A caixa postal foi fornecida pelo proprietário; entrega de email não foi testada.
Nenhuma mensagem foi enviada e nenhum contato externo foi realizado.

O check de rascunhos e a validação HTML passaram. Link de afiliado, IDs e código
JavaScript de rastreamento foram preservados. Nenhuma campanha ou alteração DNS.
Backup antes da finalização em /workspace/backups/prodentim-before-public-contact-release.tar.gz.

## Bloqueio externo

A leitura Git via proxy funciona; a consulta `gh api repos/saulohenriq4/prodentim/pages`
retornou Forbidden antes de confirmar source/build_type do GitHub Pages. A liberação de
api.github.com e mega7products.com está salva no rascunho do ambiente, mas sua aplicação
no runtime não foi comprovada. Credencial GitHub já está presente; não foi solicitado
outro token. Não tentar acessar o destino por rotas que contornem a política de rede.

Após liberar o acesso em configurações do ambiente: consultar Pages, confirmar branch
e pasta, reler HEAD remoto, preservar backup da produção, publicar o commit autorizado
pelo fluxo configurado e verificar build e HTTPS no domínio real. A autorização permanece
válida. Não é preciso pedir novamente permissão para publicar esta versão.
