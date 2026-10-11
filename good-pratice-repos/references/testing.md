# Testes, TDD e gates de qualidade

Use para mudanças de comportamento, correções de bugs, configuração executável e políticas de merge/release. Teste os contratos relevantes, não a existência de pastas chamadas `tests`.

## TEST-01 — Red → Green → Refactor

1. Extraia o comportamento esperado de requisitos, contratos ou de uma decisão explícita. A implementação atual não é a única especificação.
2. Escreva uma verificação pequena que falha pelo defeito ou comportamento ausente.
3. Execute e registre o RED. Falha de dependência, sintaxe ou ambiente não demonstra uma regressão reproduzida.
4. Faça a menor alteração de produção capaz de atender ao contrato.
5. Execute o teste específico e os testes relacionados; obtenha GREEN.
6. Refatore preservando comportamento e execute novamente as verificações afetadas.

No legado sem cobertura, caracterize o comportamento necessário antes de alterar. Não consagre um bug conhecido como contrato só porque o teste fica fácil. Quando não houver infraestrutura para executar, informe a limitação; teste escrito não é teste aprovado. [S05]

## TEST-02 — Escolha a fronteira certa

Use testes unitários para regras isoladas; integração para banco, filesystem, filas e contratos entre componentes; testes de aceitação/E2E para jornadas essenciais. Simule dependências fora da fronteira, não a própria operação que deveria estar sendo verificada.

Priorize cenários de falha pertinentes: entrada inválida, autorização negada, timeout, concorrência, duplicidade, reexecução, operação parcial e interrupção de processo. Não imponha toda a lista a um projeto que não possui essas capacidades.

Para software distribuído, acrescente instalação e uso do pacote final. Para CI/infra, valide sintaxe/schema e o comportamento dos gatilhos e permissões em ambiente apropriado. Para documentação, execute exemplos e valide referências quando seguro. [S06]

## TEST-03 — Qualidade da suíte

Torne tempo, aleatoriedade e dependências controláveis onde fizer sentido. Não use dados de produção ou acesso à internet como pré-requisito oculto de teste unitário. Separe testes que exigem serviços externos e declare ambiente, custo e credenciais de teste.

Um teste instável exige diagnóstico. Quarentena só pode ocorrer com justificativa, responsável, prazo e cobertura compensatória do risco. Repetir até passar não transforma intermitência em confiança.

Cobertura ajuda a localizar lacunas; não prova correção. Preserve limiares acordados, avalie comportamento alterado e evite impor um percentual universal. Não gere asserts triviais apenas para elevar uma métrica.

## TEST-04 — Gate que realmente bloqueia

Mapeie lint/formatação em modo de verificação, análise estática/tipos quando aplicável, testes, build e verificações de segurança. Reutilize ferramentas existentes antes de acrescentar outras.

Confirme o status obrigatório configurado na plataforma e suas dependências. Uma pipeline pode terminar verde com trabalho relevante omitido. Investigue filtros de caminho, regras de branch, jobs opcionais e condições que pulam verificações; estabeleça um gate agregador ou mecanismo equivalente que avalie resultados esperados.

Não aceite `continue-on-error`, `allow_failure`, `|| true` ou supressões em controles obrigatórios sem exceção explícita. Nem toda verificação precisa bloquear todo PR: diferencie feedback rápido, validação completa e gate de release, sem liberar uma versão antes das validações que ela exige.

## TEST-05 — Feedback e desempenho

Meça duração e tempo até o primeiro diagnóstico. Execute as verificações rápidas primeiro; use paralelismo e caches com isolamento de confiança. Não retire testes de cenário necessários só para diminuir duração.

Matrizes devem corresponder às plataformas e versões suportadas. Uma suíte enorme em um único ambiente não comprova compatibilidade com todos os demais. [S05] [S06]

## Evidência de saída

Para cada execução, informe comando, diretório, revisão, ambiente relevante, exit code e resumo. Diferencie execução local de CI remoto. Registre testes ignorados, infraestrutura indisponível e quais verificações permaneceram apenas propostas.
