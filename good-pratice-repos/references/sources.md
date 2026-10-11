# Fontes e decisões de adaptação

Consulta: **11 de outubro de 2026**. Os identificadores `[Sxx]` usados nos módulos apontam para esta lista. Textos operacionais e modelos são uma síntese aplicada; não são transcrições dos artigos nem uma certificação de cumprimento dos referenciais.

## Como os dois artigos foram usados

Do artigo de maio, foram aproveitados o foco em primeiro uso, documentação útil, automação e distribuição previsível. Do artigo de setembro, mudanças pequenas, feedback rápido e recuperação foram tratados como objetivos condicionados à capacidade técnica e ao risco. [S01] [S02]

Algumas escolhas foram deliberadamente qualificadas: a skill preserva responsabilidade/revisão humanas; não presume superioridade universal de IA; não exige múltiplos formatos sem demanda; não usa `latest` como única identidade; não trata “versão já existe” como sucesso sem verificação. Exemplos de infraestrutura pessoal dos artigos não são templates universais.

A separação entre auditoria, planejamento e implementação, as prioridades, os modelos de saída, a seleção de módulos e a política conservadora de patches são decisões desta skill. Não atribua essas escolhas aos autores das referências.

## Como atualizar

Antes de gerar configuração executável, confira a documentação oficial da versão/instalação usada. Revise especialmente permissões, gatilhos, tiers, identidades de CI e requisitos de assinatura. Não substitua SHA conhecido por outro inventado; consulte e valide a origem. Registre mudanças materiais nas políticas da skill.

## S01 — Fabio Akita: deploy e mudança de premissa

[Parem de inventar desculpas e façam mais deploy! — 22/09/2026](https://akitaonrails.com/2026/09/22/parem-de-inventar-desculpas-e-facam-mais-deploy-a-premissa-mudou/)
Base editorial para fluxo de entrega e atenção a reversibilidade, dados e consumidores externos. Relatos pessoais sobre produtividade não foram transformados em garantias.

## S02 — Fabio Akita: mínimo de projetos open source

[Boas práticas de projetos de código aberto com LLM — 30/05/2026](https://akitaonrails.com/2026/05/30/boas-praticas-projetos-codigo-aberto-llm-o-minimo/)
Base editorial para experiência inicial, documentação, CI e publicação utilizável. Plataformas de distribuição são escolhidas pelo contexto.

## S03 — Agent Skills

[Specification](https://agentskills.io/specification)
Formato do pacote, frontmatter e carregamento progressivo de referências.

## S04 — DORA: lotes pequenos

[Working in small batches](https://dora.dev/capabilities/working-in-small-batches/)
Referência para decomposição e redução do tempo de feedback.

## S05 — DORA: integração contínua

[Continuous integration](https://dora.dev/capabilities/continuous-integration/)
Referência para integração frequente, verificações rápidas, correção do build e TDD.

## S06 — DORA: testes

[Test automation](https://dora.dev/capabilities/test-automation/)
Referência para cobertura comportamental e suítes confiáveis mantidas pelos desenvolvedores.

## S07 — DORA: entrega contínua

[Continuous delivery](https://dora.dev/capabilities/continuous-delivery/)
Distingue capacidade de entregar de deploy automático e contextualiza a melhoria do processo.

## S08 — DORA: automação de deploy

[Deployment automation](https://dora.dev/capabilities/deployment-automation/)
Referência para promoção de pacotes, configuração separada, repetição e verificações pós-deploy.

## S09 — DORA: métricas

[DORA’s software delivery performance metrics](https://dora.dev/guides/dora-metrics/)
Orientação consultada com cinco métricas e cautelas de comparação. O módulo de entrega não utiliza uma lista desatualizada de quatro indicadores como se fosse a atual.

## S10 — SemVer

[Semantic Versioning 2.0.0](https://semver.org/)
Contrato de versionamento, API pública, pré-1.0 e versões publicadas.

## S11 — Keep a Changelog

[Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/)
Notas orientadas a pessoas, com mudanças organizadas por versão.

## S12 — GitHub: segurança de Actions

[Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use)
Privilégios, código externo, pinning de actions e execução segura de workflows.

## S13 — GitHub: evento privilegiado

[Securely using pull_request_target](https://docs.github.com/en/actions/reference/security/securely-using-pull_request_target)
Fronteira entre código de contribuições e acesso privilegiado. Defaults da plataforma devem ser reavaliados no momento de uso.

## S14 — GitHub: proteção de branches

[About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
Checks, revisões e proteção efetiva de integração; não apenas arquivos locais.

## S15 — GitHub: licenciamento

[Licensing a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)
Diferencia publicação do código e concessão de licença. A skill não escolhe termos jurídicos para o titular.

## S16 — OpenSSF: critérios de boas práticas

[OpenSSF Best Practices — Passing criteria](https://www.bestpractices.dev/en/criteria/0)
Referência de documentação, contribuição, relatos de segurança e manutenção. A skill não concede selo nem declara atendimento integral.

## S17 — GitLab: pipelines de merge request

[Merge request pipelines](https://docs.gitlab.com/ci/pipelines/merge_request_pipelines/)
Contextos de fork/projeto pai e acesso a recursos protegidos.

## S18 — GitLab: segurança de runners

[Security for self-managed runners](https://docs.gitlab.com/runner/security/)
Isolamento, persistência de execução e riscos de ambientes privilegiados.

## S19 — GitLab: segurança de deploy

[Deployment safety](https://docs.gitlab.com/ci/environments/deployment_safety/)
Concorrência, implantações antigas, ambientes e segurança operacional.

## S20 — OWASP: desenvolvimento com IA

[Secure Coding with AI Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secure_Coding_with_AI_Cheat_Sheet.html)
Responsabilidade humana, revisão de alterações sensíveis e proteção do contexto. A orientação mais cautelosa sobre aprovação humana foi preferida à substituição ampla da revisão por LLM.

## S21 — Reproducible Builds

[Definitions](https://reproducible-builds.org/docs/definition/)
Critério para alegar reprodução byte a byte, distinto de apenas repetir um comando de build.

## S22 — SLSA

[Build: Track Basics — v1.2](https://slsa.dev/spec/v1.2/build-track-basics)
Referência para provenance e garantias crescentes do processo de build. Um arquivo de atestação não demonstra, sozinho, atendimento aos requisitos de um nível.

## S23 — OWASP: prompt injection

[LLM Prompt Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html)
Dados não confiáveis, privilégio mínimo e controles externos ao modelo.

## S24 — Google Engineering Practices

[What to look for in a code review](https://google.github.io/eng-practices/review/reviewer/looking-for.html)
Critérios de design, correção, simplicidade, testes e documentação.

## S25 — Pete Hodgson: feature toggles

[Feature Toggles — MartinFowler.com](https://martinfowler.com/articles/feature-toggles.html)
Separação entre deploy e exposição, categorias de flags, testes e custo de manutenção.

## S26 — Danilo Sato: Parallel Change

[Parallel Change — MartinFowler.com](https://martinfowler.com/bliki/ParallelChange.html)
Transição compatível por expansão, migração e contração.

## S27 — GitHub: OIDC

[OpenID Connect reference](https://docs.github.com/en/actions/reference/security/oidc)
Claims e restrições de confiança para identidades de workflows.

## S28 — GitHub: eventos

[Events that trigger workflows](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows)
Gatilhos, restrições e encadeamento de execuções de CI.

## S29 — GitHub: merge queue

[Managing a merge queue](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue)
Validação do conjunto a integrar e evento `merge_group` em GitHub Actions.
