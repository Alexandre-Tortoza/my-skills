# good-pratice-repos

Skill de engenharia de repositórios, em português, com perfis privados/open source e módulos específicos para GitHub e GitLab. Nome preservado conforme solicitado.

## Instalação e uso

Extraia o pacote e coloque a pasta inteira `good-pratice-repos` no diretório de skills aceito pelo seu agente, seguindo a configuração desse agente. O ponto de entrada é [SKILL.md](SKILL.md); os recursos referenciados precisam permanecer junto dele. Não copie apenas o arquivo principal.

O pacote utiliza o formato Agent Skills, sem sintaxe de invocação exclusiva de um produto. Descoberta, ativação e permissões dependem do agente hospedeiro. A entrega deste pacote não instala nem ativa a skill automaticamente. [S03]

Exemplos de pedidos, adaptando o alvo:

```text
Use good-pratice-repos para auditar este repositório privado.
Entregue os achados no chat; não altere arquivos nem publique comentários.
```

```text
Use good-pratice-repos para avaliar se esta biblioteca está pronta
para distribuição open source. Preserve a licença existente.
```

```text
Use good-pratice-repos para planejar a correção dos achados de CI.
Apresente a abordagem antes de implementar.
```

```text
Implemente somente as mudanças de configuração e testes já aprovadas,
usando good-pratice-repos. Não faça commit, push, merge ou deploy.
```

## Organização

```text
good-pratice-repos/
├── SKILL.md
├── README.md
├── references/
│   ├── baseline.md
│   ├── testing.md
│   ├── review.md
│   ├── security.md
│   ├── delivery.md
│   ├── distribution.md
│   ├── sources.md
│   ├── profiles/
│   │   ├── private.md
│   │   └── open-source.md
│   └── platforms/
│       ├── github.md
│       └── gitlab.md
├── assets/
│   ├── audit-template.md
│   ├── plan-template.md
│   ├── repository-contract-template.md
│   └── release-checklist.md
├── evals/
│   └── scenarios.md
└── tests/
    └── test_package.py
```

O arquivo principal roteia diretamente para módulos menores, carregados sob demanda. Eles são referências internas, não skills independentes que dependem de descoberta recursiva. Os modelos são opcionais e não devem ser copiados automaticamente para todo projeto.

A skill não fornece pipelines genéricas que fingem conhecer uma stack desconhecida. Ela instrui o agente a descobrir comandos, convenções, permissões e requisitos antes de propor a configuração adequada.

## Validação do pacote

Com Python 3.10 ou superior, a partir desta pasta:

```bash
python -m unittest discover -s tests -v
```

Os testes usam somente a biblioteca padrão e verificam integridade estrutural: arquivos obrigatórios, campos básicos do frontmatter, tamanho do ponto de entrada, referências, links locais, identificadores de fontes e formatação. Não são um parser YAML geral nem substituem um validador oficial da especificação.

Os [cenários de avaliação](evals/scenarios.md) descrevem testes de comportamento ainda **não executados em um agente**. Nenhum teste deste pacote comprova a segurança de um projeto auditado ou garante que o modelo obedecerá às instruções. Sandbox e controles de acesso precisam existir no hospedeiro.

## Fundamentação

Os [dois artigos e as referências complementares](references/sources.md) foram consultados em 11/10/2026. O pacote separa a inspiração editorial dos critérios técnicos e das escolhas próprias de política. Não inclui cópias dos artigos.
