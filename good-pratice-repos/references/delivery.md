# Entrega contínua, deploy e recuperação

Use para software que a equipe opera. Para bibliotecas ou aplicativos instalados por terceiros, aplique também distribuição. Não confunda capacidade de entregar sob demanda com obrigação de colocar todo commit em produção. [S07]

## DEL-01 — Mudanças pequenas e integráveis

Prefira lotes pequenos e branches curtas, mantendo a branch de integração saudável. Não imponha GitFlow, trunk-based ou renomeação de `dev`/`main` sem entender a política existente. Meça esperas e reduza o gargalo real. [S04]

Correções emergenciais devem continuar rastreáveis e passar por verificações proporcionais ao risco. Build quebrado não deve ser normalizado como estado permanente da branch compartilhada.

## DEL-02 — Fluxo do serviço

Adapte este fluxo, identificando comandos reais e responsáveis:

```text
mudança pequena, com proteção por flag quando necessária
  -> testes e revisão do PR/MR
  -> integração validada
  -> build do artefato identificado
  -> testes do artefato candidato
  -> staging/preview de pré-produção e smoke test
  -> promoção do artefato aprovado para produção
  -> verificação operacional e ativação gradual, quando aplicável
  -> observação e feedback

falha -> interromper ativação -> conter -> recuperar -> verificar
```

A flag é implementada e testada com o código antes de integrar. Sua configuração pode controlar a exposição depois do deploy. Não é uma etapa de compilação entre CI e staging. Nem toda mudança precisa de flag. [S25]

Use pré-produção representativa para serviços; adapte a preview ou teste de instalação quando esse for o produto. Uma exceção precisa declarar o risco não coberto e sua mitigação, não apenas eliminar o ambiente para acelerar.

## DEL-03 — Artefato e promoção

Construa uma versão identificada por commit e digest, teste-a e promova o mesmo artefato entre ambientes compatíveis. Separe configuração de ambiente do pacote quando possível. Se a stack incorporar configuração no build, registre variantes e valide cada candidata; não alegue que bytes diferentes são o mesmo artefato. [S08]

Retenha a versão anterior utilizável. Não dependa apenas de `latest` ou de tag mutável para saber o que está em produção. Rastreie origem, build, configuração relevante e implantação.

Deploy deve receber uma versão explícita, validar pré-condições, detectar falha e verificar saúde. A repetição deve ter comportamento definido. Serialização por ambiente deve evitar dois deploys conflitantes; uma execução antiga não pode sobrescrever silenciosamente uma mais recente.

Mantenha build separado de migrações, publicação e efeitos externos. Não gere changelog por LLM nem escreva em banco durante a compilação.

## DEL-04 — Exposição e observação

Para flags temporárias, registre dono, default seguro, finalidade e critério de remoção. Para controles operacionais duradouros, registre responsável e política de revisão, sem exigir remoção artificial. Teste caminhos ligado/desligado e combinações relevantes, sem tentar todas as combinações indiscriminadamente. [S25]

Defina sinais de sucesso e interrupção antes da liberação: saúde, erros, latência, filas e indicadores de negócio pertinentes. Defina limiares com evidência do serviço; não invente percentuais ou janelas universais. Logs e traces não devem incluir segredos ou dados desnecessários.

A ativação de flag não substitui autorização no backend. Ocultar UI não protege uma operação sensível.

## DEL-05 — Código, estado e efeitos externos

Distinga quatro ações: desativar funcionalidade, reverter binário, recuperar dados e compensar efeitos externos. Elas não são equivalentes. Pagamento já efetuado ou mensagem já enviada não desaparece com `git revert`. [S01]

Para mudanças de schema/contrato, avalie **expand → migrate → contract**: introduza compatibilidade, migre consumidores/dados, confirme transição e só então remova o formato anterior. Defina backfill retomável, validação, controle de concorrência e janela compatível com rollback. [S26]

Considere coexistência de versões em web, workers, schedulers e mensagens já enfileiradas. Verifique desligamento gracioso, jobs em andamento e compatibilidade de payloads quando existirem esses componentes.

Mudanças destrutivas exigem procedimento específico e aprovação do responsável. Backup não basta: é preciso evidência de restauração em ambiente seguro. Não execute rollback automático de schema destrutivo supondo reversibilidade.

## DEL-06 — Exercício de recuperação

Documente quando interromper rollout, quem decide, como escolher a versão anterior, compatibilidade de dados e como verificar recuperação. Teste o procedimento em ambiente descartável/seguro antes de classificá-lo como disponível.

Use RTO/RPO somente se definidos pelo projeto. Registre tempo observado de recuperação sem convertê-lo em promessa. Para alto risco, preserve revisão especializada e controles independentes; correção rápida não elimina consequência irreversível.

## DEL-07 — Melhoria pelo resultado

Quando houver dados, acompanhe por aplicação: lead time da mudança, frequência de deploy, tempo de recuperação de deploy malsucedido, taxa de falha da mudança e taxa de retrabalho de deploy. São as cinco métricas da orientação DORA consultada em outubro de 2026. Não misture denominadores e janelas nem use métricas para ranquear indivíduos. [S09]

Sem dados, proponha instrumentação mínima. Não invente indicadores, benchmarks ou ganhos de produtividade de IA. Frequência é resultado de capacidade de entrega, não uma meta que justifica remover verificações.
