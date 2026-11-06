# Auditoria inicial — 5 de novembro de 2026

Inspeção anterior ao redesign, commit bfd6066b2bb836585b3ad74f7dd81d805510e77e.
Branch de trabalho: development/mega7products-2. Backup completo (inclui Git):
/workspace/backups/prodentim-before-mega7-20261105.tar.gz, arquivo listado com sucesso.

## Confirmado no código original
- Site estático sem gerenciador de pacotes, build, CI ou suíte de testes.
- index.html e prodentim/index.html são idênticos: conteúdo e metadados duplicados.
- lang=en, sem canonical, Open Graph, robots.txt ou sitemap.xml.
- Marca do produto ocupa a identidade principal; Mega7Products não é apresentada.
- Estrelas sem fonte, depoimento “Customer review example”, milhares de consumidores,
  urgência, descontos, garantia de 60 dias e alegações de saúde sem comprovação anexada.
- Imagens de antes/depois e avaliações sem documentação de autorização.
- review.jpg pesa aproximadamente 1,8 MB; imagens sem dimensões explícitas.
- Divulgação de afiliado somente no rodapé. Sem páginas institucionais.
- CTAs usam o link exato solicitado; não têm rel=sponsored.
- Google Ads AW-17961565555 carrega automaticamente. Cada clique .btn-prod envia
  conversion para AW-17961565555/98brCNTlyZ4cEPP63vRC. Isso mede saída, não venda.
- CSS contém breakpoint de 760px, mas faltam foco explícito e reduced-motion.
- Nenhuma dependência de aplicação; código de publicidade é uma dependência externa.

## Ainda não comprovado
- Resultados médicos, ingredientes atuais, preço, garantia, estoque e direitos das imagens.
- Indexação real, Search Console, Core Web Vitals de usuários reais, configuração da
  ação no Google Ads e confirmação de vendas na Digistore24 exigem acesso externo.
- Não é possível afirmar conformidade com Google Ads ou regras do afiliado apenas
  lendo HTML. Termos oficiais atuais precisam ser conferidos antes de campanhas.
- Responsividade, acessibilidade e desempenho serão medidos na versão local; a
  presença de media queries no original não comprova uma boa experiência.

## Alterações propostas
1. Home editorial distinta e guia /prodentim/, preservando URLs.
2. Identidade petróleo/verde, tipografia local, navegação sem JavaScript e FAQ nativo.
3. Retirar afirmações não sustentadas e provas sociais fictícias, preservar arquivos originais.
4. Divulgação antes dos CTAs, checklist, limites de evidência e avisos de saúde.
5. Preservar link e IDs; publicidade opcional com escolha explícita, documentando saída.
6. Páginas institucionais em rascunho noindex até dados do responsável serem fornecidos.
7. SEO técnico, testes reais locais e plano de publicação/Ads sem ativação.
