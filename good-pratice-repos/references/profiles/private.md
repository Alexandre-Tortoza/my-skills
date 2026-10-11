# Perfil privado ou interno

Carregue quando o acesso ao código, a operação ou os dados exigirem confidencialidade. Este perfil pode coexistir com o open source: distribuição e acesso não são a mesma decisão.

## PRV-01 — Acesso e propriedade

Identifique responsáveis reais pelo serviço e pelos componentes sensíveis, além do processo de concessão e remoção de acesso. Verifique permissões de humanos, bots, runners e registries com evidência da plataforma; checkout local não comprova essas configurações.

Use controles de merge e entrega compatíveis com o risco. Não exija um segundo mantenedor fictício em projeto solo; não declare revisão independente quando o próprio autor aprovou. Controles compensatórios precisam ser explícitos, não um bypass silencioso. [S14]

## PRV-02 — Confidencialidade no desenvolvimento

Não inclua dados de clientes, dumps reais ou credenciais em fixtures, snapshots, exemplos, issues e artefatos de CI. Use dados sintéticos ou preparação autorizada. Redija achados sem repetir valores sensíveis.

Antes de usar LLM remoto, bot de review, scanner SaaS ou preview público, confira a política aplicável e o escopo autorizado. Repositório privado não significa que todo serviço externo está autorizado a recebê-lo. `.gitignore` não é controle de acesso de ferramentas de IA. [S20]

## PRV-03 — Onboarding interno

Documente como pedir acesso, preparar ambiente e obter credenciais pelos canais aprovados. O README pode apontar para documentação interna restrita, mas quem tem o perfil correto deve conseguir acessá-la. Falha de permissão do auditor é UNKNOWN, não link quebrado confirmado.

Não exija landing page pública, marketplace, Homebrew ou pacote público. Avalie o caminho realmente utilizado pelos desenvolvedores e usuários internos. Bibliotecas internas continuam precisando de compatibilidade, versões e canais de distribuição adequados.

## PRV-04 — Operação e incidentes

Para serviços, identifique responsabilidade por deploy, alertas e recuperação, com procedimentos realizáveis. Defina ambientes, acesso a logs, política de retenção e classificação de dados com quem é responsável; não invente SLA, prazo de resposta, RTO ou RPO.

Quando houver exigência organizacional de aprovação ou segregação de funções, preserve-a. Automatize coleta de evidência e passos mecânicos em vez de remover controles em nome de velocidade. Um controle documental não prova conformidade.

Se existir banco ou armazenamento persistente, verifique política de backup e exercício de recuperação. Não realize restauração em produção para testar essa política.

## PRV-05 — Licenciamento e distribuição

Não adicione uma licença permissiva por padrão, mesmo em projeto privado. Identifique a política existente e direitos sobre dependências redistribuídas; encaminhe decisão de licença ao titular responsável. Não presuma que “interno” elimina obrigações das dependências. [S15]

## Saída esperada

Mostre lacunas de acesso, onboarding, rastreabilidade e operação. Não penalize a ausência de mecanismos públicos sem um público externo. Destaque separadamente qualquer preparação solicitada para abrir o código, pois envolve outro escopo de autorização.
