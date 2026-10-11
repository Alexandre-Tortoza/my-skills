# Decisão de release ou deploy

Registrar candidato, revisão, digest quando aplicável, escopo e responsável autorizado. Para cada item relevante, informar PASS, FAIL, UNKNOWN ou N/A com evidência; não usar marcação automática pela presença de arquivo.

## Comum

- A revisão candidata e suas dependências estão identificadas e autorizadas.
- Os gates exigidos passaram na revisão/candidata correta.
- O artefato final foi validado e não contém material confidencial indevido.
- A identidade de publicação possui somente o acesso necessário.
- Exceções e riscos residuais têm decisão explícita.

## Serviço operado

- O artefato de produção corresponde ao candidato aprovado.
- Pré-produção, smoke tests e sinais de interrupção estão definidos e verificados.
- Flags pertinentes foram testadas e sua ativação está sob controle autorizado.
- Migrações e jobs coexistem com as versões necessárias.
- Contenção, recuperação de código e tratamento de dados são procedimentos distintos e verificáveis.

## Software distribuído

- Versão, tag e metadados obedecem ao contrato adotado.
- Notas explicam compatibilidade, deprecações e migração.
- Instalação e uso do pacote final foram testados nos alvos declarados.
- Retentativa não sobrescreve uma versão publicada nem oculta discrepâncias.
- Integridade e, quando exigida, autenticidade podem ser verificadas pelo consumidor.

## Decisão

Publicação/deploy autorizado: sim / não.
Resultado: apto no escopo / bloqueado / inconclusivo.
Itens bloqueantes ou desconhecidos: ...
Ação realmente realizada e comprovante: ...
Não executar a publicação apenas porque o checklist foi preenchido.
