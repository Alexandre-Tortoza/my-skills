# Distribuição, versões e releases

Use para bibliotecas públicas ou internas, CLIs e aplicativos que chegam ao usuário como pacote, instalador ou binário. O mantenedor não controla quando cada consumidor atualiza.

## DIST-01 — Superfície suportada

Identifique quem instala e os canais necessários: registry do ecossistema, release com binário, imagem, instalador, gerenciador de pacotes ou loja. Priorize um caminho funcional antes de multiplicar formatos. Não exija publicação pública de pacote interno.

Mantenha matriz de suporte por sistema operacional, arquitetura, runtime e demais condições relevantes. Um binário exige compatibilidade de ABI, bibliotecas e configuração, não apenas arquitetura de CPU.

## DIST-02 — Empacotar não é recompilar tudo

Reutilize o artefato validado em canais compatíveis. “Compilar uma vez” significa uma vez por conjunto compatível de alvo, toolchain, ABI e configuração; não um binário universal para todas as plataformas.

Teste o pacote/instalador final em ambiente limpo. Verifique conteúdo, arquivos necessários, importação ou execução, `--version` quando existir, e um uso mínimo. Um pacote pode falhar apesar de os testes do checkout passarem. [S02]

Considere assinatura/notarização conforme plataforma e distribuição; confirme requisitos oficiais antes de implementar. Não invente certificado, custo ou entitlement.

## DIST-03 — Contrato de versão

Preserve a convenção adotada. Para SemVer, defina a API pública: patch para correção compatível, minor para funcionalidade compatível e major para incompatibilidade na série estável. Inclua contratos documentados de configuração, CLI e formatos de dados, não apenas funções exportadas.

A série `0.x` indica desenvolvimento inicial e precisa de política de compatibilidade própria; não aplique automaticamente a promessa de estabilidade de `1.x`. Nesta skill, breaking changes devem sempre ser explicitadas e não escondidas em patch, inclusive em projetos pré-1.0. Essa última exigência é política conservadora da skill. [S10]

Nem todo merge precisa gerar versão ou tag. Para serviço fechado, commit/digest pode identificar deploys, enquanto contratos externos têm versionamento próprio. Em monorepo, confirme se as versões são coordenadas ou independentes.

## DIST-04 — Preparar e publicar são etapas distintas

Faça preparação explícita de versão, metadados e notas. Quando esses arquivos são versionados, a alteração entra em revisão antes da publicação. O build normal não pode editar changelog, criar commit ou publicar.

O gatilho de release pode ser tag protegida ou outro evento aprovado. Verifique que aponta para a revisão autorizada e validada. Compare tag, versão do manifest e notas quando fizerem parte da convenção. Não publique apenas porque o nome da tag parece válido.

Separe permissões e credenciais de publicação das verificações de PR/MR. Não amplie privilégios para executar contribuições externas.

## DIST-05 — Repetição e falhas parciais

Publicações devem ser retomáveis sem sobrescrever conteúdo de uma versão já distribuída. Antes de considerar “já publicado” um sucesso, consulte o registry e confirme identidade/metadados e integridade quando verificável.

Se houver discrepância ou não for possível conferir, bloqueie para investigação. Não use um `grep` genérico de “already exists”, `|| true` ou ignorar exit code como idempotência.

Não mova tag publicada para apontar a outro código. Em falha de release, publique correção ou utilize deprecação/yank permitidos pelo registry com autorização e comunicação; isso não remove cópias já instaladas.

## DIST-06 — Informação para quem atualiza

Release notes devem explicar mudança, correções, riscos, deprecações e migração. Changelog é para pessoas, não uma cópia bruta do Git log. Mantenha uma fonte coerente entre notas e arquivo versionado; geração automática continua sujeita a revisão factual. [S11]

Associe artefatos ao commit de origem e forneça verificação de integridade. Para risco elevado ou exigência do ecossistema, complemente com autenticidade/provenance e instrução real de verificação.

## Aceite

O consumidor instala pelo canal declarado, identifica a versão, executa o exemplo e entende o impacto da atualização. Os resultados devem se referir ao artefato final, não apenas ao código-fonte.
