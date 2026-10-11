# Perfil open source

Carregue para software com licença open source confirmada ou para planejar sua abertura. Um repositório público sem licença não deve ser rotulado como open source; registre licenciamento indefinido e peça a decisão do titular, sem escolher por ele. [S15]

## OSS-01 — Primeiro uso externo

Valide instalação e exemplo mínimo sem depender do ambiente do mantenedor. Priorize o canal utilizado pelo público. Amplie formatos e plataformas somente com demanda e capacidade de manutenção; não exija todos os gerenciadores de pacotes.

Documente sistemas, arquiteturas, versões e limitações realmente suportados. Um download publicado sem teste de instalação é distribuição não verificada. Para serviço self-hosted, descreva pré-requisitos e operação; para biblioteca, teste consumo do pacote publicado/empacotado, não apenas imports do checkout. [S02]

## OSS-02 — Licença e conteúdo distribuído

Confirme arquivo de licença, metadados de pacote e avisos necessários de terceiros. Considere também imagens, documentação, datasets e modelos: podem ter termos diferentes do código. Não modifique termos, autoria, copyright, CLA ou DCO sem decisão explícita.

Ao preparar um projeto privado para publicação, avalie histórico, artefatos, anexos e configurações quanto a material confidencial. Não torne o repositório público, reescreva histórico ou publique um espelho como parte implícita da auditoria.

## OSS-03 — Caminho de contribuição

Ofereça instruções de setup e testes, escopo aceito, como enviar bug reproduzível e como propor uma mudança. Use templates apenas quando reduzirem retrabalho; não invente regras que os mantenedores não pretendem cumprir.

Uma política de segurança deve indicar versões suportadas e canal privado de relato que exista. Não direcione vulnerabilidades sensíveis para issue pública nem publique contato fictício. Defina regras de convivência e responsáveis por aplicá-las conforme a comunidade. [S16]

## OSS-04 — Contribuições não confiáveis

Use CI de forks sem segredos e sem acesso à infraestrutura interna. Não execute reprodução colada em issue antes de inspecioná-la. Trate mudanças em workflows, hooks, instruções de agentes e dependências como parte relevante da revisão, não arquivos auxiliares inofensivos. [S12] [S17]

Bots de triagem ou review devem ter capacidades mínimas. Conteúdo externo não pode autorizar um bot a publicar releases, modificar regras ou expor variáveis.

## OSS-05 — Contrato com consumidores

Defina API pública, compatibilidade e política de versão; ofereça release notes e migração quando necessárias. Mudanças públicas incluem CLI, formatos persistidos, configuração, mensagens/saídas documentadas e defaults, não só assinaturas de função. Aplique o módulo de distribuição.

Não confunda publicar correção rapidamente com atualizar instalações de terceiros. Mantenha identificação de versões afetadas e canais de aviso. Não apague tags para ocultar um problema.

## OSS-06 — Manutenção honesta

Explique estado do projeto, como receber suporte e limitações. Não prometa atendimento ou roadmap inexistente. Um projeto arquivado pode ter documentação e distribuição corretas; avalie se sua condição está clara.

Acompanhe obstáculos reais de instalação e relatos dos usuários. Contagem de estrelas, linhas geradas e número bruto de testes não demonstram qualidade. Não solicite telemetria obrigatória para avaliar adoção.

## Saída esperada

Priorize impedimentos para instalar, contribuir, reportar segurança e atualizar com previsibilidade. Dê a exigências de licença seu escopo específico: podem bloquear a declaração/publicação como open source sem impedir desenvolvimento interno.
