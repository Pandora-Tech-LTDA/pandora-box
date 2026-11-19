---
name: sync-docs
description: Entrevista o usuário sobre um projeto ou processo e registra, durante a conversa, o glossário e as decisões em arquivos (sync/glossario.md e sync/decisoes.md). É o ponto de partida da família sync e, no fim, recomenda o próximo passo - /sync-spec para produtos com telas ou /sync-mva para automações e agentes.
disable-model-invocation: true
---

# sync-docs

Entreviste o usuário sobre o projeto dele até chegarem a um entendimento compartilhado e **registre o que for sendo resolvido**: os termos do projeto num glossário e as decisões num registro de decisões. O registro é o que permite continuar depois, em outra conversa, e é o ponto de partida do `/sync-spec` e do `/sync-mva`.

## O método de entrevista

Carregue a skill **`sync-me`** e siga o método dela: visão primeiro, rodadas com só o que sustenta a visão, suposições declaradas, sugestão e custo em uma linha, riscos oferecidos e não impostos, fatos são seus e decisões são do usuário, e nada é construído sem confirmação.

Se não conseguir carregar o `sync-me`, aplique estas regras mínimas:

- Comece pedindo a visão do usuário e devolva-a em um parágrafo.
- Pergunte em rodadas numeradas, só o que sustenta a visão; assuma o que é reversível e liste como "assumi".
- Em cada pergunta, uma linha de sugestão e uma de custo. Escreva perguntas abertas.
- Nas decisões que sustentam a visão, peça o motivo de um "sim" sozinho.
- Guarde os riscos numa lista e ofereça analisá-los; não os imponha a cada pergunta.
- Pesquise você mesmo os fatos e diga onde encontrou. As decisões são do usuário.

## Antes da primeira pergunta: onde o registro vai ficar

1. **Verifique se você consegue gravar arquivos** na pasta de trabalho (Claude Code, Cowork, repositório conectado).
2. **Se já existir uma pasta `sync/`**, leia `sync/glossario.md` e `sync/decisoes.md` antes de perguntar qualquer coisa. Não repita perguntas já decididas; continue de onde parou e diga isso ao usuário.
3. **Avise o usuário em uma frase** onde o registro vai ficar:
   - com arquivos: "Vou registrar o glossário e as decisões em `sync/glossario.md` e `sync/decisoes.md` enquanto conversamos."
   - sem arquivos: "Aqui não consigo gravar arquivos, então vou manter o registro no chat. Para continuar em outra conversa, salve o registro que eu entregar no fim, ou use uma pasta de projeto (Cowork ou Claude Code)."

## O que perguntar

Comece pela **visão**, como manda o método do `sync-me`. Depois, o primeiro galho é o **processo**, não a solução. Antes de falar de ferramenta, a árvore precisa cobrir:

- **O problema:** como ele se manifesta, em que momento aparece, com que frequência e quem mais sofre com ele.
- **O processo atual:** quem faz, passo a passo, com quais documentos e sistemas, e como a pessoa contorna o problema hoje.
- **O estado desejado:** como seria o trabalho sem esse problema.
- **O contexto:** que documentos, planilhas e regras existem; quais têm dados pessoais ou sigilosos.
- **O critério de sucesso:** como saber, com algo observável, que melhorou.

Quando o usuário descrever o processo como ele *deveria* ser, pergunte como ele *é* de fato. O processo executado vale mais que o documentado.

## Glossário: `sync/glossario.md`

Registre um termo **no momento em que ele se resolve**, não em lote no final. Um termo entra quando o projeto usa uma palavra com um sentido próprio, ou quando duas palavras disputam o mesmo sentido.

```markdown
# Glossário

**<Termo>**: <definição curta, em uma ou duas frases, nas palavras do projeto>.
Evitar: <sinônimos que não devem ser usados, se houver>.
```

O glossário é só vocabulário. Nada de detalhes de implementação, passo a passo ou anotações soltas. Se o usuário usar um termo de um jeito diferente do que está no glossário, aponte e pergunte qual vale.

## Decisões: `sync/decisoes.md`

Registre uma decisão **assim que o usuário a toma**, se ela muda o que vai ser construído ou como. Não registre detalhes menores; esses ficam só na conversa.

```markdown
# Decisões

## Visão
<o parágrafo da visão, validado pelo usuário>

## Em aberto
- <perguntas em aberto, incluindo os "não sei" e o que precisa de protótipo>

## Suposições
- <o que foi assumido e não corrigido pelo usuário>

## Riscos
- <riscos anotados e se já foram analisados>

## D<número>. <título curto>
- **Data:** <AAAA-MM-DD>
- **Decisão:** <o que foi decidido>
- **Motivo:** <o motivo, nas palavras do usuário>
- **Alternativas descartadas:** <o que se considerou e por que ficou de fora>
- **Discordância:** <se o usuário discordou da sua sugestão, registre aqui; senão, omita>
```

Se uma decisão nova substitui uma antiga, não apague a antiga: marque-a como **substituída por D<n>**.

Mantenha as seções **Visão**, **Em aberto**, **Suposições** e **Riscos** sempre atualizadas no topo do arquivo: é delas que o `/sync-spec` e o `/sync-mva` partem em outra conversa.

Sem arquivos, mantenha os dois registros no chat e mostre a versão atualizada a cada duas ou três rodadas, para o usuário não perder nada.

## Encerramento

Siga o encerramento do método: resumo do entendimento, confirmação do usuário e nada construído antes disso. Depois da confirmação:

1. Mostre o glossário e as decisões finais. Sem arquivos, entregue os dois num bloco pronto para copiar e salvar, com o nome de cada arquivo.
2. Liste as **perguntas em aberto** e o que **precisa de protótipo**.
3. **Recomende o próximo passo**, com o motivo em uma frase:
   - **`/sync-spec`** quando o projeto é um **produto ou sistema com telas**, com pessoas usando, que vai ser desenvolvido. Ele gera a spec para uma IA de código construir.
   - **`/sync-mva`** quando é uma **automação ou um agente** que trabalha sobre documentos e dados, sem telas próprias, e o objetivo é testar o valor rápido.
   - **Os dois**, quando a automação depois vira produto: o `/sync-mva` primeiro, para provar o valor, e o `/sync-spec` depois, para construir direito.

   A escolha é do usuário. Se ele não souber, explique a diferença em duas linhas e pergunte.

---

*Derivada da skill [`grill-with-docs`](https://www.aihero.dev/skills-grill-with-docs) de Matt Pocock ([mattpocock/skills](https://github.com/mattpocock/skills), licença MIT; ver `LICENSE` nesta pasta). Adaptada pela Pandora Tech LTDA.*
