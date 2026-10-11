# Adaptador GitHub

Use somente quando GitHub for a plataforma confirmada. Consulte documentação oficial e configuração atual antes de escolher sintaxe, versão de action, SHA ou disponibilidade por plano. Este módulo não pressupõe acesso administrativo.

## GH-01 — Merge com controle efetivo

Inspecione rulesets/proteções da branch, checks exigidos, bypasses e política de revisão. `CODEOWNERS` sem a exigência de aprovação correspondente não é prova de bloqueio. Se houver merge queue, confirme execução dos gates para `merge_group` e validação da revisão que será integrada. [S14] [S29]

Não assuma que `main` é a branch padrão. Registre configuração inacessível como UNKNOWN. Não a altere para “facilitar” a auditoria.

## GH-02 — Workflows e código externo

Prefira `pull_request` para testar contribuições com confiança restrita. Não faça checkout/build/teste de código não confiável em `pull_request_target` ou em outro contexto privilegiado com segredos/token de escrita. Separe triagem de execução.

Trate artefatos recebidos por `workflow_run` como dados não confiáveis; não os execute só porque o workflow consumidor tem mais privilégios. Políticas e defaults da plataforma mudam: confirme as vigentes, sem depender deles como única defesa. [S13]

## GH-03 — Dependências do workflow

Fixe actions/workflows reutilizados por SHA completo verificado na origem, com atualização controlada. Não invente SHA nem entregue placeholder executável como configuração pronta. Use permissões mínimas por job e evite interpolar título/body de PR em comandos shell. [S12]

Restrinja OIDC ao job de publicação/deploy e à identidade esperada. A permissão para obter ID token não dispensa a política restritiva no provedor. [S27]

## GH-04 — Entrega

Verifique ambientes protegidos, segredos por ambiente, concorrência e retenção de artefatos anteriores. Não cancele indiscriminadamente uma migration em andamento para permitir outro deploy.

Não presuma que um evento criado por automação desencadeará outro workflow: confira regras do token/evento e prefira dependências explícitas. Releases devem validar origem e gates antes de publicar. [S28]

## Evidência

Relate paths dos workflows, branch/revisão, nomes dos checks e configurações remotas confirmadas. A existência de `.github/workflows/ci.yml` prova somente configuração no checkout, não uma execução aprovada ou proteção ativa.
