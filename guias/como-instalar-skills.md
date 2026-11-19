# Como instalar as skills

**Nível:** Iniciante · **Tempo:** 5 a 10 minutos

Este guia mostra como instalar as skills deste repositório no **Claude Code** ou no
**Claude Cowork**. Você não precisa saber programar: em cada caso há um **prompt pronto**
para copiar e colar, e o próprio Claude faz o trabalho pesado.

> 🚧 **Família `sync` em construção.** O guia já vale para quando as skills forem publicadas.
> Até lá, o prompt vai avisar que ainda não há skills na pasta.

---

## Antes de começar: o que é uma skill?

Uma **skill** é um pacote de instruções que ensina o Claude a fazer uma tarefa de um
jeito específico. Depois de instalada, você a usa digitando uma **barra** seguida do nome
dela no chat, por exemplo:

```
/sync-docs
```

Cada skill é uma pasta com um arquivo `SKILL.md` dentro. Instalar é colocar essas pastas
no lugar onde o Claude procura.

## Qual ferramenta você usa?

| Você usa… | Siga |
|---|---|
| **Claude Code** (no terminal, no app desktop ou na extensão do VS Code) | [Opção A](#opção-a-claude-code) |
| **Claude Cowork** (no app desktop do Claude) | [Opção B](#opção-b-claude-cowork) |

Não sabe? Se você conversa com o Claude dentro de uma pasta do seu computador e ele mexe nos
arquivos, provavelmente é o **Cowork**. Se você digita comandos num terminal, é o **Claude Code**.

---

## Opção A: Claude Code

1. Abra o Claude Code (em qualquer pasta).
2. Copie o prompt abaixo e cole no chat:

```text
Instale as skills da família "sync" para mim:

1. Baixe a pasta skills/sync do repositório público https://github.com/Pandora-Tech-LTDA/wiki (branch main).
2. Para cada subpasta de skills/sync que tenha um arquivo SKILL.md, copie a subpasta inteira para ~/.claude/skills/<nome-da-subpasta>/. Ignore a pasta "references".
3. Se alguma skill já existir em ~/.claude/skills, me pergunte antes de substituir.
4. Apague os arquivos temporários do download.
5. No final, me mostre uma tabela com as skills instaladas e uma frase sobre o que cada uma faz, e me diga qual usar primeiro.

Se não houver nenhuma skill publicada ainda, apenas me avise.
```

3. O Claude pode pedir permissão para rodar comandos. Leia e aprove.
4. **Feche e abra o Claude Code de novo** para ele carregar as skills.
5. Teste digitando `/sync-docs` no chat.

## Opção B: Claude Cowork

No Cowork, as skills são instaladas na sua conta do Claude enviando um arquivo `.zip`
por skill. O Claude prepara os arquivos para você.

1. Abra o Cowork e escolha uma pasta do seu computador (por exemplo, `Downloads`).
2. Copie o prompt abaixo e cole no chat:

```text
Prepare as skills da família "sync" para eu instalar:

1. Baixe a pasta skills/sync do repositório público https://github.com/Pandora-Tech-LTDA/wiki (branch main).
2. Para cada subpasta de skills/sync que tenha um arquivo SKILL.md, crie um arquivo <nome-da-subpasta>.zip nesta pasta, com a subpasta inteira dentro. Ignore a pasta "references".
3. Apague os arquivos temporários do download.
4. No final, liste os .zip criados e me explique, passo a passo e em linguagem simples, como enviar cada um nas configurações do Claude para ativar as skills.

Se não houver nenhuma skill publicada ainda, apenas me avise.
```

3. Envie cada `.zip` nas configurações do Claude, na área de **Skills** (em geral, em
   *Configurações → Capacidades*). Os nomes do menu podem mudar com o tempo; se não
   encontrar, pergunte ao próprio Claude onde fica.
4. **Envie todas as skills**, inclusive a `syncing`. As outras dependem dela.
5. Abra uma nova conversa e teste digitando `/sync-docs`.

---

## Qual skill usar primeiro?

```
/sync-docs  →  /sync-mva  →  /syncdb
```

1. **`/sync-docs`**: comece aqui. O Claude faz perguntas sobre o seu projeto e registra o
   vocabulário e as decisões. Questione as sugestões dele: a ideia é você pensar, não só dizer "sim".
2. **`/sync-mva`**: depois, monte o seu MVA. Ele usa o que o `/sync-docs` registrou e entrega
   o prompt do agente, os documentos e o manual de montagem no Cowork.
3. **`/syncdb`**: quando precisar de dados de exemplo (sintéticos) para testar, em CSV ou Markdown.

Quer só conversar sobre uma ideia, sem gerar arquivos? Use **`/sync-me`**.

## Problemas comuns

| Problema | O que fazer |
|---|---|
| Digito `/sync-docs` e nada acontece | Feche e abra o Claude de novo. Confira se a pasta ou o `.zip` da skill foi instalado. |
| A skill faz todas as perguntas de uma vez, sem sugestões | Ela não carregou a `syncing`. Confira se a `syncing` está instalada e peça: "carregue a skill syncing". |
| Quero continuar o projeto em outra conversa | Salve o registro que o `/sync-docs` entregou, ou trabalhe numa pasta/repositório para que ele grave os arquivos em `sync/`. |

## Créditos

As skills `syncing`, `/sync-me` e `/sync-docs` são derivadas das skills
[`grilling`](https://www.aihero.dev/skills-grilling), [`grill-me`](https://www.aihero.dev/skills-grill-me)
e [`grill-with-docs`](https://www.aihero.dev/skills-grill-with-docs) de **Matt Pocock**
([mattpocock/skills](https://github.com/mattpocock/skills), licença MIT).
O `/sync-mva` e o `/syncdb` seguem a metodologia MVA, © 2026 Pandora Tech LTDA.
