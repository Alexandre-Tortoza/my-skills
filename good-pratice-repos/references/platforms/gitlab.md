# Adaptador GitLab

Use somente quando GitLab for a plataforma confirmada. Confira versão, tier e permissões antes de recomendar recursos; não gere configuração assumindo que toda instalação suporta as mesmas funcionalidades.

## GL-01 — Pipeline e merge

Inspecione `.gitlab-ci.yml`, includes, `workflow:rules`, regras de jobs e condições de merge. Verifique se o trabalho esperado roda em MR e na branch de integração, sem pipelines duplicadas ou gaps escondidos por filtros.

Confirme exigência de pipeline aprovado e regras de revisão/proteção disponíveis. Um job declarado no YAML não comprova que participou da pipeline relevante.

## GL-02 — Forks

Diferencie pipeline no fork de pipeline executada no projeto pai. Executar uma MR de fork no projeto pai pode combinar configuração da contribuição com recursos e variáveis do projeto pai; revise a origem antes de disparar.

Verifique condições de acesso a variáveis e runners protegidos na versão utilizada. Não presuma que marcar uma variável como masked autoriza usá-la com código externo. [S17]

## GL-03 — Runners e includes

Inspecione isolamento, persistência, tags, rede e uso de executores privilegiados. Não execute código não confiável em runner compartilhado com acesso ao host ou à infraestrutura interna. Restrinja execução privilegiada e evite reutilização de workspace entre fronteiras de confiança. [S18]

Fixe includes/componentes externos em referências imutáveis verificadas quando suportado. Proteja variáveis por escopo e ambiente; não copie secrets para o YAML para corrigir permissões.

## GL-04 — Segurança de deploy

Use serialização de deploy por ambiente, por exemplo `resource_group` quando apropriado, e proteção contra implantação de jobs antigos. Confira ordem, retries e dependências de migrations. Jobs de deploy destrutivos não devem ser tratados como livremente canceláveis. [S19]

Para identidade federada, consulte suporte da instalação e do provedor antes de gerar configuração. Não substitua um problema de identidade por token pessoal com escopo excessivo.

## Evidência

Separe conteúdo do YAML, resultado de pipeline e configuração da instância/projeto. Quando aprovações, ambientes ou recursos de segurança não estiverem disponíveis, proponha alternativa com limitações explícitas em vez de alegar controle inexistente.
