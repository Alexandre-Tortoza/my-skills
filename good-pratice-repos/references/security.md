# Segurança do repositório e da cadeia de fornecimento

Aplique proporcionalmente ao risco. Acesso privado não torna scripts, dependências ou contribuidores automaticamente confiáveis.

## SEC-01 — Segredos e dados

Verifique prevenção de commit acidental, detecção de segredos e acesso a variáveis de CI. Use ferramentas existentes e saída redigida; não reproduza tokens, chaves ou dados de clientes no relatório.

Segredo exposto exige revogação/rotação pelo responsável e análise do alcance. Remover o arquivo do último commit não invalida uma credencial. Não teste se a credencial funciona contra serviços reais nem faça reescrita de histórico sem autorização.

Exemplos de configuração devem conter valores fictícios inequívocos. Histórico, logs, caches, imagens, pacotes e anexos também entram no escopo quando houver evidência de exposição.

## SEC-02 — Dependências e atualizações

Confirme origem e nome de dependências novas. Avalie manutenção, compatibilidade, licenciamento e vulnerabilidades relevantes à versão e ao uso. Não instale um pacote apenas porque uma LLM sugeriu seu nome.

Fixe resoluções e ferramentas conforme o ecossistema e automatize propostas de atualização quando permitido. Pinning sem atualização acumula risco; atualização automática sem testes também.

Trate supressões de scanner com justificativa, escopo, responsável e prazo. Diferencie falso positivo demonstrado, risco aceito e problema ainda não avaliado. Não declare “zero vulnerabilidades” a partir de um único scanner.

## SEC-03 — Fronteiras de confiança no CI

Separe avaliação de código não confiável de jobs privilegiados. Testes e instalação de dependências executam código. Não entregue credenciais de produção, tokens de escrita, rede interna ou socket Docker a pipelines de contribuições externas.

Prefira runners isolados e efêmeros para código não confiável. Identifique persistência de workspace, credenciais e caches entre execuções. Container sozinho não prova isolamento suficiente, especialmente com execução privilegiada ou acesso ao host. [S12] [S18]

Restrinja permissões por job. Dados externos usados em shell devem ser tratados como dados, não interpolados como comandos. Proteja também artefatos consumidos por pipelines posteriores; um workflow privilegiado não torna confiável o arquivo que recebeu.

## SEC-04 — Identidade de entrega

Separe identidade de build da identidade de publicação/deploy. Prefira credenciais temporárias ou identidade federada quando suportadas. Restrinja emissor, audiência e identidade esperada da execução; OIDC com condições amplas ainda concede acesso indevido. [S27]

Confirme proteção de branch, tag, ambiente e registry onde aplicável. Não use permissões administrativas como solução para falha de pipeline. Um arquivo `CODEOWNERS` só é um controle efetivo quando a política de revisão correspondente está configurada.

## SEC-05 — Integridade de artefatos

Identifique revisão de origem, execução de build e digest do artefato. Um checksum publicado junto ao arquivo detecta corrupção, mas sozinho não comprova autenticidade se ambos puderem ser substituídos.

Quando o risco de distribuição justificar, gere e verifique provenance/atestações e uma SBOM com ferramenta apropriada. SBOM é inventário; não equivale a análise de vulnerabilidade nem a licença de redistribuição. Atestação não comprova ausência de defeitos.

Avalie requisitos SLSA por evidência de como o build e sua identidade são protegidos; não atribua nível por existir um arquivo de provenance. [S22]

## SEC-06 — Recuperação e resposta

Para componentes sensíveis, identifique dono e canal de resposta a incidente, versões afetadas e contenção possível. Defina continuidade com a equipe responsável, não com prazos inventados.

Não oculte um problema para manter badge verde. Achado crítico pode interromper a implementação solicitada para evitar ampliar o dano; relate o bloqueio e a ação de contenção necessária sem executar operações externas não autorizadas.

## Aceite

Evidencie que código não confiável não alcança segredos ou publicação; que dependências e artefatos têm origem rastreável; e que lacunas importantes possuem tratamento explícito. Sem acesso à configuração remota, classifique sua verificação como UNKNOWN.
