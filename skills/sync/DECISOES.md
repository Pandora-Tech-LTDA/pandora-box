# Decisões: família de skills `sync`

## Decididas

- **Quem usa:** qualquer pessoa, sobre o próprio projeto. As skills não são ferramentas de sala de aula; o texto fala sempre em "usuário", nunca em "aluno". (Revisado: a primeira versão desta decisão era voltada a alunos, com mediação do professor.)
- **Princípio central:** o usuário deve sempre questionar. A skill não pode premiar o "sim" passivo.
- **Nome da família:** `sync` (sincronizar é de mão dupla; o objetivo é entendimento compartilhado).
- **Arquitetura**, espelhando a do original:
  - `/sync-me`: entrevista livre, sem gerar arquivos, e também o núcleo com o método de entrevista usado pelas outras skills (reúne o `grilling` e o `grill-me` do original). Pode ser invocada pelo usuário e pelo modelo. (Revisado: na primeira versão havia um núcleo separado chamado `syncing`; ele foi renomeado para `sync-me` para que o nome visível ao usuário seja o da skill que ele chama.)
  - `/sync-docs`: entrevista que registra glossário e decisões durante a sessão (equivale ao `grill-with-docs`).
  - `/sync-mva`: entrevista guiada pelas etapas e pelo núcleo da metodologia MVA.
  - `syncdb`: construção de bases de dados sintéticas (ver abaixo).
  - `/sync-docs` e `/sync-mva` têm `disable-model-invocation: true` e usam o método do `sync-me`.
- **Fluxo recomendado:** `/sync-docs` → `/sync-mva` → `syncdb`.
  - O usuário começa pelo `/sync-docs`. O `/sync-mva` constrói o MVA a partir do que o `/sync-docs` produziu.
  - Se o usuário começar direto pelo `/sync-mva`, a skill sugere passar pelo `/sync-docs` antes.
  - O `/sync-mva` usa o `syncdb` para criar a base sintética do MVA.
- **`syncdb`:** skill específica para construir bases de dados com dados sintéticos. Pode receber um arquivo de referência (XLS, CSV ou qualquer outro formato de dados) e gerar dados sintéticos de acordo com ele. Funciona nos dois modos: chamada pelo `/sync-mva` ou direto pelo usuário (`/syncdb`).
- **Ambiente:** Claude.ai, Claude Cowork e Claude Code (plataformas principais). Por seguirem o formato aberto Agent Skills, as skills também são documentadas para OpenAI Codex, VS Code com GitHub Copilot e outros agentes compatíveis, marcadas como "compatível, não testado". Há um guia de instalação por plataforma em `guias/instalar/`. No Claude.ai e no Cowork, a instalação é pelo envio de um .zip por skill; os .zip são gerados automaticamente (workflow `publicar-skills`) e publicados na release `skills` do GitHub, com links fixos.
- **Ritmo da entrevista:** igual ao `grilling`, em rodadas com todas as perguntas que já podem ser feitas, numeradas. Também aceita uma pergunta por vez.
- **Resposta recomendada:** aparece por padrão, e o usuário tem a opção de escondê-la, para responder sem ver a sugestão da IA.
- **`/sync-mva` usa as etapas 3 a 5 do MVA** (modelagem → hipótese → contexto) como árvore de decisões. Referência principal: `references/mva/templates/agente-construtor-mva-v0.1.md`.
- **Pacote do `/sync-mva` (v1):**
  - o prompt do agente, já com teste automatizado: alguns casos de teste (entrada + saída esperada) que o próprio agente executa para se avaliar antes de começar a trabalhar;
  - os documentos de referência (gerados com o `syncdb` quando forem dados sintéticos);
  - um manual de como montar o agente no Cowork.
- **Formato dos dados do `syncdb`:** a saída é sempre CSV ou Markdown, qualquer que seja o formato de entrada. Nunca Excel, Docs, PDF etc.
- **Entregável do `/sync-me`:** um resumo no chat ao final, com decisões tomadas, pontos de discordância do usuário, perguntas que ficaram sem resposta e o que só um protótipo resolve. Não grava arquivos.
- **Fatos:** como no `grilling`, a IA pesquisa os fatos sozinha, mas explica ao usuário o que encontrou e onde.
- **`syncdb` também pode ser invocada pelo modelo**, além de pelo usuário (`/syncdb`) e pelo `/sync-mva`.
- **Passagem do `/sync-docs` para o `/sync-mva`:** funciona em qualquer ambiente, com ou sem repositório.
  - **Registro do `/sync-docs`:** se houver sistema de arquivos ou repositório conectado, grava `sync/glossario.md` e `sync/decisoes.md` no projeto do usuário durante a sessão. Sem arquivos, entrega o registro no chat, em um bloco pronto para salvar.
  - **Aviso:** no início, o `/sync-docs` diz ao usuário onde o registro vai ficar. Se não houver onde gravar, avisa que, para continuar em outra conversa, ele precisa salvar o registro ou conectar um repositório.
  - **Busca do `/sync-mva`, nesta ordem:** (1) registro do `/sync-docs` na conversa atual; (2) arquivos em `sync/`; (3) pede ao usuário que cole ou anexe o registro; (4) se não existir, sugere rodar o `/sync-docs` antes.
- **Objetivo do `/sync-mva`:** é uma skill nova (usa o método de entrevista do `sync-me`, mas não tem equivalente no original). Serve para **montar um MVA**: entender o processo que o usuário quer automatizar, quais documentos e base de dados ele precisa e, ao final, gerar os materiais para ele montar o MVA como um projeto no Claude:
  - os documentos de contexto necessários (ex.: para uma análise de frequência de funcionários, a planilha de frequência);
  - o prompt (instruções) do projeto;
  - o passo a passo de como colar tudo isso no projeto dentro do Claude.
- **Encerramento do `/sync-mva`:** a entrevista segue até a própria skill concluir que entendeu. Então ela diz algo como: "Já entendi. Se você tiver mais alguma informação, me diga; senão, posso gerar agora os materiais para você montar o seu MVA." Os materiais só são gerados depois da resposta do usuário.
- **Estrutura de pastas:** cada skill fica em `skills/sync/<nome>/SKILL.md` (`sync-me`, `sync-docs`, `sync-mva`, `syncdb`). O guia de instalação copia toda subpasta com `SKILL.md`, exceto `references/`.
- **Créditos:** `/sync-me` e `/sync-docs` citam Matt Pocock com link para [mattpocock/skills](https://github.com/mattpocock/skills) e para a página da skill de origem. `/sync-mva` e `/syncdb` citam a metodologia MVA da Pandora Tech LTDA.
- **Documentação para iniciantes:** o README raiz lista as ferramentas e skills, e o guia `guias/como-instalar-skills.md` traz prompts prontos para instalar no Claude Code e no Cowork.

- **Situação (2026-11-19):** as quatro skills (`sync-me`, `sync-docs`, `sync-mva`, `syncdb`) estão publicadas na versão 0.1, em teste.

- **Instalação em um passo:** o repositório é um marketplace de plugins (`.claude-plugin/marketplace.json`) com o plugin `pandora` (raiz em `skills/`, manifesto em `skills/.claude-plugin/plugin.json`), que reúne todas as skills. O workflow publica `pandora.zip` (o plugin) e um .zip por skill; nos avulsos, a chave `disable-model-invocation` é removida porque o envio avulso de skills no Claude.ai não a aceita. Instaladas pelo plugin, as skills aparecem como `/pandora:<skill>`.

## Em aberto

Nenhum ponto em aberto. Próximo passo: escrever as skills.
