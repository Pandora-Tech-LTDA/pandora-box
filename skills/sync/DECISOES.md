# Decisões: família de skills `sync`

## Decididas

- **Quem usa:** o aluno roda a skill sozinho, sobre o próprio projeto; o professor media depois.
- **Princípio pedagógico:** o aluno deve sempre questionar. A skill não pode premiar o "sim" passivo.
- **Nome da família:** `sync` (sincronizar é de mão dupla; o objetivo é entendimento compartilhado).
- **Arquitetura**, espelhando a do original:
  - `syncing`: núcleo com o método de entrevista, invocável pelo modelo (equivale ao `grilling`).
  - `/sync-me`: entrevista livre, sem gerar arquivos (equivale ao `grill-me`).
  - `/sync-docs`: entrevista que registra glossário e decisões durante a sessão (equivale ao `grill-with-docs`).
  - `/sync-mva`: entrevista guiada pelas etapas e pelo núcleo da metodologia MVA.
  - As três portas têm `disable-model-invocation: true` e delegam para `syncing`.

## Em aberto

- Uma pergunta por vez ou rodadas (o original usa rodadas e aceita voltar para uma por vez).
- Como tratar a resposta recomendada para não induzir passividade.
- Qual entregável cada skill gera ao final.
- Onde o `/sync-docs` grava os registros no ambiente dos alunos.
- Como o `/sync-mva` usa as 7 etapas e os elementos do núcleo como árvore de decisões.
