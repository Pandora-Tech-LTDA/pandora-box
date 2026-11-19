---
name: sync-mva
description: Monta um MVA (Minimum Viable Automation) a partir do registro do /sync-docs. Entrevista o usuário só sobre o que falta e entrega o pacote para montar o agente - o prompt com autoteste, os documentos de referência (com dados sintéticos) e o manual de montagem no Cowork.
disable-model-invocation: true
---

# sync-mva

Ajude o usuário a montar um **MVA (Minimum Viable Automation)**: a menor automação capaz de testar se uma ideia resolve um problema real e produzir evidência para decidir o próximo passo. O MVA não é a solução final. É um experimento.

O resultado é um **pacote**: o prompt do agente com autoteste, os documentos de referência e um manual para montar o agente no Cowork.

## 1. Encontrar o registro do `/sync-docs`

O `/sync-mva` parte do que o `/sync-docs` registrou. Procure, nesta ordem:

1. o registro na **conversa atual**;
2. os arquivos **`sync/glossario.md`** e **`sync/decisoes.md`** na pasta de trabalho;
3. peça ao usuário que **cole ou anexe** o registro;
4. se não existir registro, recomende rodar o **`/sync-docs`** antes, explicando em uma frase por quê: o MVA fica melhor quando o problema já está claro. Se o usuário preferir seguir mesmo assim, siga, mas comece pelas perguntas do problema.

## 2. Diagnosticar as lacunas

Antes de perguntar qualquer coisa, classifique cada item abaixo como **identificado**, **parcial**, **ausente** ou **hipótese**, e mostre a tabela ao usuário:

| Item | O que é |
|---|---|
| Problema | O que dói, como aparece e com que frequência |
| Pessoas | Quem vive o problema e quem vai usar o MVA |
| Processo atual | Os passos de hoje e o ponto do fluxo onde a dor aparece |
| Mudança desejada | Como seria sem o problema |
| Hipótese | O que o MVA vai fazer e o que se espera que mude |
| Contexto | Os documentos e dados que o agente precisa conhecer |
| Restrições | Dados pessoais ou sigilosos, regras, limites |
| Critério de sucesso | Como saber, com algo observável, que funcionou |

Não pergunte o que já está identificado.

## 3. Entrevistar só o que falta

Carregue a skill **`sync-me`** e siga o método dela (rodadas, perguntas abertas, sugestão com o que custa, nada de "sim" passivo). Se não conseguir carregar, pergunte em rodadas numeradas, com uma sugestão e o seu custo em cada pergunta, e peça o motivo de cada "sim".

Use as etapas do MVA como galhos da árvore:

**Modelagem.** Reconstrua o fluxo atual, o que influencia o problema e o contexto necessário. A arquitetura da automação não vem antes da arquitetura do problema.

**Hipótese.** Chegue a uma frase neste formato:

> Se intervirmos em **[ponto do fluxo]** por meio de **[capacidade do agente]**, esperamos reduzir **[tensão]** e produzir **[efeito]**, observável por **[evidência ou métrica]**.

**Contexto.** Para cada documento ou base, pergunte primeiro **o que o agente precisa saber** e só depois o formato. A falta de uma integração não impede o MVA: quando os dados reais não estiverem disponíveis ou forem sensíveis, o MVA usa dados sintéticos.

Pergunte só o necessário para o experimento poder ser executado e avaliado.

## 4. Fechar o entendimento

Quando tiver o suficiente para montar um teste que produza evidência útil, diga, com as suas palavras:

> "Já entendi. Se você tiver mais alguma informação, me diga; senão, posso gerar agora os materiais para você montar o seu MVA."

Mostre antes um resumo de uma tela: problema, hipótese, documentos que serão gerados e critério de sucesso. **Gere os materiais só depois da resposta do usuário.**

## 5. Gerar o pacote

Crie a pasta `mva/<nome-curto-do-mva>/` com:

```
mva/<nome>/
├── LEIA-ME.md
├── prompt-do-agente.md
├── documentos/
└── manual-cowork.md
```

Todos os arquivos em **Markdown ou CSV**. Nunca Excel, Word ou PDF.

### `LEIA-ME.md`

Problema, hipótese, o que o MVA testa, **o que ele não testa**, os documentos incluídos (e quais são sintéticos), o critério de sucesso e as suposições aceitas nesta versão.

### `documentos/`

Os documentos de referência que o agente vai consultar. Para dados sintéticos, carregue a skill **`syncdb`** e siga-a: ela gera os CSV ou Markdown e o dicionário de dados de cada base. Textos como políticas e procedimentos podem ser escritos diretamente em Markdown, marcados como fictícios quando forem.

### `prompt-do-agente.md`

As instruções completas do agente, com estas seções:

1. **Papel e objetivo.**
2. **Problema e hipótese** que o MVA está testando.
3. **Documentos disponíveis:** o nome de cada arquivo de `documentos/`, o que ele contém e quando usá-lo.
4. **Tarefas:** o que o agente faz, passo a passo.
5. **Regras e restrições**, incluindo o que o agente nunca deve fazer.
6. **Incerteza e exceções:** o que fazer quando faltar informação ou o caso fugir do previsto. O agente nunca inventa dados.
7. **Formato de saída.**
8. **Critério de sucesso** e o que registrar em cada execução para avaliar o MVA depois.
9. **Autoteste.** De 3 a 5 casos de teste, cada um com uma **entrada** e a **saída esperada**, cobrindo um caso típico e pelo menos um caso difícil dos dados. Inclua esta instrução no prompt:

   > Antes da primeira tarefa, e sempre que o usuário pedir "rode o autoteste", execute cada caso de teste usando os documentos, compare o seu resultado com a saída esperada e mostre uma tabela com caso, resultado e "passou" ou "falhou". Se algum caso falhar, diga o motivo provável e não siga para as tarefas reais sem avisar o usuário.

### `manual-cowork.md`

Um passo a passo para quem nunca montou um agente:

1. Criar uma pasta no computador para o MVA e copiar para ela o `prompt-do-agente.md` e a pasta `documentos/`.
2. Abrir o Claude Cowork nessa pasta.
3. Na primeira mensagem, pedir: *"Leia o prompt-do-agente.md e siga essas instruções a partir de agora. Comece rodando o autoteste."*
4. Conferir o resultado do autoteste e o que fazer se algum caso falhar.
5. Usar o agente nas tarefas reais e registrar o que funcionou e o que não funcionou, para avaliar o MVA pelo critério de sucesso.
6. Alternativa: usar um Projeto no Claude.ai, colando o prompt nas instruções do projeto e enviando os documentos como conhecimento.

### Onde entregar

Com pasta de trabalho, grave os arquivos nela. Sem pasta, crie os arquivos para download; se não for possível, entregue cada arquivo num bloco pronto para copiar, com o caminho completo.

## 6. Conferir antes de entregar

Antes de dizer que terminou, confira:

1. O MVA testa uma hipótese clara?
2. Os documentos bastam para executar os casos de teste?
3. Dá para rodar sem depender de sistemas da empresa?
4. Há critério de sucesso e o que registrar em cada execução?
5. Está explícito o que o MVA não testa?
6. Os arquivos foram de fato gerados?

Se algum item falhar, corrija antes de entregar. Termine dizendo ao usuário qual é o primeiro passo: abrir o `manual-cowork.md`.

---

*Parte da família Sync, da Pandora Box. Segue a metodologia MVA, ©2026 Pandora Tech LTDA. O método de entrevista vem do `sync-me`, derivado das skills de Matt Pocock (licença MIT).*
