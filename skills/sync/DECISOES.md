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
  - `syncdb`: construção de bases de dados sintéticas (ver abaixo).
  - As três portas têm `disable-model-invocation: true` e delegam para `syncing`.
- **Fluxo recomendado:** `/sync-docs` → `/sync-mva` → `syncdb`.
  - O aluno começa pelo `/sync-docs`. O `/sync-mva` constrói o MVA a partir do que o `/sync-docs` produziu.
  - Se o aluno começar direto pelo `/sync-mva`, a skill sugere passar pelo `/sync-docs` antes.
  - O `/sync-mva` usa o `syncdb` para criar a base sintética do MVA.
- **`syncdb`:** skill específica para construir bases de dados com dados sintéticos. Pode receber um arquivo de referência (XLS, CSV ou qualquer outro formato de dados) e gerar dados sintéticos de acordo com ele. Funciona nos dois modos: chamada pelo `/sync-mva` ou direto pelo aluno (`/syncdb`).
- **Passagem do `/sync-docs` para o `/sync-mva`:** funciona em qualquer ambiente, com ou sem repositório.
  - **Registro do `/sync-docs`:** se houver sistema de arquivos ou repositório conectado, grava `sync/glossario.md` e `sync/decisoes.md` no projeto do aluno durante a sessão. Sem arquivos, entrega o registro no chat, em um bloco pronto para salvar.
  - **Aviso:** no início, o `/sync-docs` diz ao aluno onde o registro vai ficar. Se não houver onde gravar, avisa que, para continuar em outra conversa, ele precisa salvar o registro ou conectar um repositório.
  - **Busca do `/sync-mva`, nesta ordem:** (1) registro do `/sync-docs` na conversa atual; (2) arquivos em `sync/`; (3) pede ao aluno que cole ou anexe o registro; (4) se não existir, sugere rodar o `/sync-docs` antes.
- **Objetivo do `/sync-mva`:** é uma skill nova (usa o método de entrevista do `syncing`, mas não tem equivalente no original). Serve para **montar um MVA**: entender o processo que o aluno quer automatizar, quais documentos e base de dados ele precisa e, ao final, gerar os materiais para ele montar o MVA como um projeto no Claude:
  - os documentos de contexto necessários (ex.: para uma análise de frequência de funcionários, a planilha de frequência);
  - o prompt (instruções) do projeto;
  - o passo a passo de como colar tudo isso no projeto dentro do Claude.
- **Encerramento do `/sync-mva`:** a entrevista segue até a própria skill concluir que entendeu. Então ela diz algo como: "Já entendi. Se você tiver mais alguma informação, me diga; senão, posso gerar agora os materiais para você montar o seu MVA." Os materiais só são gerados depois da resposta do aluno.

## Em aberto

- Uma pergunta por vez ou rodadas (o original usa rodadas e aceita voltar para uma por vez).
- Como tratar a resposta recomendada para não induzir passividade.
- Qual entregável cada skill gera ao final.
- Como o `/sync-mva` usa as etapas e os elementos do núcleo do MVA como árvore de decisões (referência principal: `references/mva/templates/agente-construtor-mva-v0.1.md`).
- `syncdb`: além de ser chamada pelo aluno e pelo `/sync-mva`, o modelo pode invocá-la por conta própria?
- Formato exato do pacote final do `/sync-mva` (o que entra além de documentos, prompt e guia de montagem: casos de teste? critérios de sucesso? lista de suposições?).
