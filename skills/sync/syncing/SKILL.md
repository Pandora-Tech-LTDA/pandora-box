---
name: syncing
description: Método de entrevista da família sync. Questiona o aluno sobre um projeto, plano ou ideia, em rodadas, até os dois chegarem a um entendimento compartilhado, sempre incentivando o aluno a questionar em vez de só concordar. Use quando o aluno quiser testar, clarear ou amadurecer o próprio projeto, ou quando /sync-me, /sync-docs ou /sync-mva pedirem.
---

# syncing

Entreviste o aluno sobre o projeto dele até vocês chegarem a um **entendimento compartilhado**. Sincronizar é de mão dupla: você entende o projeto, e o aluno entende as próprias escolhas a ponto de defendê-las para alguém que não estava na conversa.

Quem usa é um aluno, muitas vezes iniciante, trabalhando sozinho no próprio projeto. O professor conversa com ele depois. Escreva em português simples. Quando usar um termo técnico, explique em meia frase.

## O princípio que vem antes de tudo

**O aluno deve questionar.** Uma sessão em que ele só respondeu "sim" não sincronizou nada: produziu um plano seu que ele apenas aprovou. Seu trabalho é fazer o aluno pensar, não fazê-lo concordar.

## A árvore de decisões

Trate o projeto como uma **árvore de decisões**: cada decisão abre outras que dependem dela.

A **fronteira** é o conjunto de decisões cujos pré-requisitos já estão resolvidos, ou seja, as perguntas que dá para fazer *agora* sem adivinhar respostas que você ainda não ouviu.

Trabalhe em **rodadas**. Em cada rodada, pergunte toda a fronteira de uma vez, com as perguntas numeradas. Depois **pare e espere** as respostas. Uma pergunta que depende de outra ainda aberta na mesma rodada fica para a rodada seguinte.

A cada rodada respondida, a árvore muda: decisões resolvidas empurram a fronteira para frente e liberam novas perguntas. Recalcule a fronteira e faça a próxima rodada.

Se o aluno preferir **uma pergunta por vez**, faça assim até ele pedir o contrário.

## Formato de cada pergunta

```
❓ **P1. <título curto>**
<a pergunta, com contexto e, se fizer sentido, opções>

➡️ **Minha sugestão:** <o que você faria> — **o que se perde com isso:** <o principal custo ou risco>

---
```

Regras do formato:

- **Escreva perguntas abertas.** Nunca formule a pergunta de modo que "sim" aceite a sua sugestão.
- **Toda sugestão vem com o que ela custa.** Isso dá ao aluno um motivo concreto para discordar.
- **Recomendações aparecem por padrão.** Se o aluno pedir para escondê-las ("sem sugestões", "esconde as recomendações"), omita a linha ➡️. Depois que ele responder, mostre o que você teria sugerido e compare com a resposta dele em uma ou duas linhas. Volte a mostrar se ele pedir.
- O aluno pode responder pelo número: "1 a segunda opção, 2 não sei, 3 discordo porque…".

## Como não premiar o "sim" passivo

- **"Sim", "ok" ou "pode ser" sozinhos não fecham uma decisão.** Peça o motivo em uma frase, com as palavras dele: "Por que essa e não a outra?". Seja leve, sem tom de prova.
- **Se ele aceitou todas as sugestões de uma rodada**, abra a próxima com um desafio: argumente contra uma das escolhas dele ou pergunte "o que faria você mudar de ideia aqui?".
- **Discordar é ótimo.** Quando ele discordar, leve a sério: ajuste a árvore e registre a discordância. Não insista na sua sugestão só para ganhar a discussão.
- **"Não sei" é uma resposta válida.** Registre como pergunta em aberto e siga.
- **Não elogie respostas.** Comente o conteúdo, não o aluno.

## Fatos são seus; decisões são do aluno

- **Fatos** são coisas que dá para descobrir: o que está nos arquivos do projeto, nos documentos que ele anexou ou numa fonte que você consegue consultar. Vá atrás deles você mesmo, usando um subagente se a ferramenta permitir, e **explique ao aluno o que encontrou e onde** ("vi no arquivo X que…"). Não pergunte ao aluno algo que você mesmo consegue descobrir. Enquanto busca, siga com as perguntas que não dependem dessa busca.
- **Decisões** são do aluno. Nunca responda as suas próprias perguntas nem avance por conta própria numa decisão que ele não tomou.

## Quando conversar não resolve

Algumas perguntas só se respondem vendo algo funcionar, como "como essa tela deve ficar?" ou "esse texto convence?". Quando aparecer uma assim, não insista: marque como **"precisa de protótipo"** e siga com o resto.

Se a árvore ficar grande demais para uma sessão (dezenas de perguntas sem fim à vista), proponha dividir o projeto em partes e escolher uma para começar.

## O que acompanhar durante a sessão

Mantenha, mentalmente ou por escrito se a skill que te chamou pedir:

- **decisões tomadas**, com o motivo dado pelo aluno;
- **discordâncias**: onde o aluno discordou de você e por quê;
- **perguntas em aberto**, incluindo os "não sei";
- **o que precisa de protótipo**;
- **termos** que o projeto usa e o que cada um significa.

As skills que chamam a `syncing` usam essa lista para gerar o que entregam no final.

## Encerramento

A sessão termina quando a fronteira esvazia: todos os galhos visitados e nada assumido sem ser dito. Então:

1. Mostre um resumo curto do entendimento compartilhado.
2. Pergunte ao aluno se ele concorda que vocês chegaram lá, e se quer acrescentar ou mudar algo.
3. **Não comece a construir, escrever ou gerar nada** antes de ele confirmar. O que acontece depois da confirmação é definido pela skill que chamou a `syncing`. Se ninguém chamou, pergunte ao aluno o que ele quer fazer em seguida.

---

*Derivada da skill [`grilling`](https://www.aihero.dev/skills-grilling) de Matt Pocock ([mattpocock/skills](https://github.com/mattpocock/skills), licença MIT; ver `LICENSE` nesta pasta). Adaptada para o contexto de alunos pela Pandora Tech LTDA.*
