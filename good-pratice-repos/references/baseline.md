# Baseline do repositório

Use para avaliar se uma pessoa consegue compreender, configurar, verificar e modificar o software sem conhecimento tribal. Aplique os controles ao produto real, não a uma árvore de diretórios idealizada.

## BASE-01 — Primeiro uso e README

Comece pelo problema resolvido, público e resultado esperado. Separe o caminho do usuário do caminho de quem desenvolve. Verifique pré-requisitos, uma forma principal de instalação/execução, um exemplo mínimo e como saber que funcionou. O quickstart deve apontar para capacidades existentes, não promessas de roadmap. [S02]

Teste o caminho documentado em ambiente limpo e compatível quando autorizado. Registre versões, comando e resultado. Se depender de cadastro, licença, download grande ou hardware específico, explicite antes do primeiro comando. Não esconda custo ou autenticação sob “um comando”.

Para bibliotecas, o primeiro uso é instalar/importar; para serviços internos, pode ser obter acesso e executar um fluxo; para documentação, navegar e validar o conteúdo. Não exija binários de uma biblioteca nem Docker de um site estático.

## BASE-02 — Entradas explícitas

Mapeie runtimes suportados, gerenciador de dependências, lockfiles segundo a convenção do ecossistema, serviços externos, portas e variáveis obrigatórias. Use instalações travadas quando suportadas. Não imponha a política de lockfile de uma aplicação a bibliotecas de outro ecossistema.

Para cada configuração necessária que não pode ser versionada com valores reais, mantenha um exemplo sanitizado consumível pelo parser correto, ou equivalente documentado e testado. O exemplo deve indicar campos obrigatórios, defaults e origem dos segredos. Não invente nomes de variáveis nem URLs funcionais.

O software deve recusar configuração inválida com mensagem útil, sem despejar o segredo. Diferencie configuração em build e runtime. Um `.env.example` não compensa um caminho de inicialização que ignora as variáveis.

## BASE-03 — Comandos canônicos

Identifique comandos existentes para instalar/preparar, verificar, testar, buildar e executar. Adicione release/deploy apenas quando fizerem parte do produto. Documente esses comandos em uma fonte principal e reutilize-os no CI quando fizer sentido.

Não crie `Makefile`, `Taskfile` ou scripts wrappers apenas para renomear comandos nativos. Se um wrapper reduzir passos frágeis, faça-o falhar corretamente, documente dependências e teste repetição e entradas inválidas.

Antes de rodar “setup”, examine hooks de instalação, downloads e operações destrutivas. Não execute `reset`, seed destrutivo ou limpeza de volumes fora de ambiente descartável.

## BASE-04 — Build controlado

Exija que o build consuma entradas declaradas e gere artefatos, sem publicar, sincronizar sistemas ou alterar fontes. Dependências externas inevitáveis devem ser identificadas, fixadas e verificadas; prefira preparar/snapshotar conteúdo antes do build.

Valide em workspace isolado que os arquivos versionados permanecem inalterados e que não há acesso a bancos de produção, credenciais de deploy ou APIs de negócio. Escritas em diretórios de saída/cache são esperadas quando declaradas.

Distinga build repetível de **build reproduzível byte a byte**. Para alegar o segundo, reconstrua com as condições documentadas e compare os artefatos relevantes. Controle ambiente, timestamps e entradas; não use a presença de um lockfile como prova. [S21]

## BASE-05 — Documentação e limites

Mantenha documentação proporcional: visão dos componentes, responsabilidade de cada parte, contratos externos e instruções de operação relevantes. Preserve decisões com alternativas e consequências quando houver decisão material; não produza ADR para toda alteração.

Descreva o sistema como ele funciona hoje. Marque propostas e dívida separadamente. Remova comandos obsoletos e referências enganosas, sem apagar histórico útil indiscriminadamente. Em fluxos complexos, use diagrama somente se esclarecer responsabilidades ou entradas/saídas.

Instruções de agentes devem ser curtas: comandos reais, limites, áreas sensíveis e verificações. Não duplique toda a documentação em `AGENTS.md` ou equivalente, nem altere arquivos de instruções sem autorização explícita para esse escopo.

## BASE-06 — Higiene com evidência

Procure código morto demonstrável, dependências não usadas, arquivos gerados ou temporários versionados por acidente, duplicação de conhecimento e configurações divergentes. Diferencie fixtures e artefatos intencionalmente versionados de lixo.

Não remova arquivo ou dependência somente porque uma busca textual não encontrou uso: considere descoberta dinâmica, public API, CI, packaging e consumidores externos. Preserve as convenções do framework. [S24]

## Aceite mínimo

Uma pessoa nova consegue seguir um caminho documentado até o primeiro resultado; configuração necessária está descrita; comandos de verificação existem; fontes e build permanecem separados. Registre separadamente o que foi inspecionado e o que foi executado.
