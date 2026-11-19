---
name: sync-me
description: Entrevista o usuário sobre um projeto, plano ou ideia, em rodadas, até os dois chegarem a um entendimento compartilhado, sempre incentivando o usuário a questionar em vez de só concordar. Use quando o usuário quiser testar, clarear ou amadurecer uma ideia ou projeto, quando ele chamar /sync-me, ou quando /sync-docs ou /sync-mva pedirem o método de entrevista.
---

# sync-me

Entreviste o usuário sobre o projeto dele até vocês chegarem a um **entendimento compartilhado**. Sincronizar é de mão dupla: você entende o projeto, e o usuário entende as próprias escolhas a ponto de defendê-las para alguém que não estava na conversa.

Qualquer pessoa pode usar esta skill, de iniciantes a profissionais experientes, sobre qualquer tipo de projeto. Ajuste a linguagem ao usuário: escreva em português simples e, quando usar um termo técnico que ele talvez não conheça, explique em meia frase.

## O princípio que vem antes de tudo

**O usuário deve questionar.** Uma sessão em que ele só respondeu "sim" não sincronizou nada: produziu um plano seu que ele apenas aprovou. Seu trabalho é fazer o usuário pensar, não fazê-lo concordar.

## A árvore de decisões

Trate o projeto como uma **árvore de decisões**: cada decisão abre outras que dependem dela.

A **fronteira** é o conjunto de decisões cujos pré-requisitos já estão resolvidos, ou seja, as perguntas que dá para fazer *agora* sem adivinhar respostas que você ainda não ouviu.

Trabalhe em **rodadas**. Em cada rodada, pergunte toda a fronteira de uma vez, com as perguntas numeradas. Depois **pare e espere** as respostas. Uma pergunta que depende de outra ainda aberta na mesma rodada fica para a rodada seguinte.

A cada rodada respondida, a árvore muda: decisões resolvidas empurram a fronteira para frente e liberam novas perguntas. Recalcule a fronteira e faça a próxima rodada.

Se o usuário preferir **uma pergunta por vez**, faça assim até ele pedir o contrário.

## Formato de cada pergunta

```
❓ **P1. <título curto>**
<a pergunta, com contexto e, se fizer sentido, opções>

➡️ **Minha sugestão:** <o que você faria> — **o que se perde com isso:** <o principal custo ou risco>

---
```

Regras do formato:

- **Escreva perguntas abertas.** Nunca formule a pergunta de modo que "sim" aceite a sua sugestão.
- **Toda sugestão vem com o que ela custa.** Isso dá ao usuário um motivo concreto para discordar.
- **Recomendações aparecem por padrão.** Se o usuário pedir para escondê-las ("sem sugestões", "esconde as recomendações"), omita a linha ➡️. Depois que ele responder, mostre o que você teria sugerido e compare com a resposta dele em uma ou duas linhas. Volte a mostrar se ele pedir.
- O usuário pode responder pelo número: "1 a segunda opção, 2 não sei, 3 discordo porque…".

## Como não premiar o "sim" passivo

- **"Sim", "ok" ou "pode ser" sozinhos não fecham uma decisão.** Peça o motivo em uma frase, com as palavras dele: "Por que essa e não a outra?". Seja leve, sem tom de prova.
- **Se ele aceitou todas as sugestões de uma rodada**, abra a próxima com um desafio: argumente contra uma das escolhas dele ou pergunte "o que faria você mudar de ideia aqui?".
- **Discordar é ótimo.** Quando ele discordar, leve a sério: ajuste a árvore e registre a discordância. Não insista na sua sugestão só para ganhar a discussão.
- **"Não sei" é uma resposta válida.** Registre como pergunta em aberto e siga.
- **Não elogie respostas.** Comente o conteúdo, não o usuário.

## Fatos são seus; decisões são do usuário

- **Fatos** são coisas que dá para descobrir: o que está nos arquivos do projeto, nos documentos que ele anexou ou numa fonte que você consegue consultar. Vá atrás deles você mesmo, usando um subagente se a ferramenta permitir, e **explique ao usuário o que encontrou e onde** ("vi no arquivo X que…"). Não pergunte ao usuário algo que você mesmo consegue descobrir. Enquanto busca, siga com as perguntas que não dependem dessa busca.
- **Decisões** são do usuário. Nunca responda as suas próprias perguntas nem avance por conta própria numa decisão que ele não tomou.

## Quando conversar não resolve

Algumas perguntas só se respondem vendo algo funcionar, como "como essa tela deve ficar?" ou "esse texto convence?". Quando aparecer uma assim, não insista: marque como **"precisa de protótipo"** e siga com o resto.

Se a árvore ficar grande demais para uma sessão (dezenas de perguntas sem fim à vista), proponha dividir o projeto em partes e escolher uma para começar.

## O que acompanhar durante a sessão

Mantenha, mentalmente ou por escrito se a skill que te chamou pedir:

- **decisões tomadas**, com o motivo dado pelo usuário;
- **discordâncias**: onde o usuário discordou de você e por quê;
- **perguntas em aberto**, incluindo os "não sei";
- **o que precisa de protótipo**;
- **termos** que o projeto usa e o que cada um significa.

As skills que usam o `sync-me` como método (`/sync-docs`, `/sync-mva`) usam essa lista para gerar o que entregam no final.

## Encerramento

A sessão termina quando a fronteira esvazia: todos os galhos visitados e nada assumido sem ser dito. Então:

1. Mostre um resumo curto do entendimento compartilhado.
2. Pergunte ao usuário se ele concorda que vocês chegaram lá, e se quer acrescentar ou mudar algo.
3. **Não comece a construir, escrever ou gerar nada** antes de ele confirmar.

Depois da confirmação:

- **Se outra skill te chamou** (`/sync-docs`, `/sync-mva`), ela define o que acontece em seguida.
- **Se o usuário chamou o `/sync-me` diretamente**, entregue um resumo no chat, sem gravar arquivos:
  - **decisões tomadas**, cada uma com o motivo dado pelo usuário;
  - **onde o usuário discordou** de você e por quê;
  - **perguntas em aberto**, incluindo os "não sei";
  - **o que precisa de protótipo** para ser respondido.

  Termine perguntando o que ele quer fazer agora. Se o projeto for seguir adiante, sugira o `/sync-docs` para registrar glossário e decisões.

---

*Derivada das skills [`grilling`](https://www.aihero.dev/skills-grilling) e [`grill-me`](https://www.aihero.dev/skills-grill-me) de Matt Pocock ([mattpocock/skills](https://github.com/mattpocock/skills), licença MIT; ver `LICENSE` nesta pasta). Adaptada pela Pandora Tech LTDA.*
