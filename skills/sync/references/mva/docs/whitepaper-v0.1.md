# MVA — Minimum Viable Automation

> **Documento de trabalho — v0.1**  
> Metodologia em desenvolvimento pela Pandora.

## 1. Definição

O **MVA (Minimum Viable Automation)** é um processo estruturado de **descoberta, modelagem e experimentação de uma automação** que parte de um problema real da organização.

O processo começa pela definição e compreensão do problema, sua manifestação, quem é afetado e qual é seu impacto. Em seguida, o problema é modelado para identificar suas etapas e as fontes de contexto necessárias para compreendê-lo e testar possíveis soluções.

A partir dessas fontes, é gerado **contexto sintético** que permita experimentar de forma controlada. A automação é então construída e testada em versões sucessivas do MVA até atingir maturidade suficiente para ser apresentada a outras pessoas, que irão validar se ela efetivamente gera valor na resolução daquele problema específico.

O MVA, portanto, não começa com uma automação previamente definida. **A descoberta do que deve ser automatizado e de como essa automação deve funcionar faz parte da própria construção do MVA.**

## Origem do conceito e posicionamento da metodologia

O termo **Minimum Viable Automation (MVA)** antecede esta metodologia. Há registros públicos anteriores de seu uso, incluindo Adam Knight (2016), que aplicou princípios de MVP, Agile e iteração à automação, e formulações posteriores no campo de Business Process Automation, como a abordagem da **Info-Tech Research Group**.

Na formulação da Info-Tech, um MVA é uma automação concentrada em um caso de uso pequeno e específico, construída com esforço mínimo para um grupo delimitado de usuários. O objetivo é aprender rapidamente, avaliar a mudança e a aceitação da automação e usar esse aprendizado para desenvolver uma capacidade mais ampla de automação. A abordagem se conecta explicitamente ao ciclo **Build → Measure → Learn** e recomenda começar pequeno, medir valor e evoluir progressivamente.

A metodologia desenvolvida neste documento dialoga com esses antecedentes, mas propõe uma formulação específica: **o MVA não é apenas uma automação mínima usada para testar uma oportunidade previamente identificada; ele é um experimento que também produz evidências para qualificar o próprio problema, a hipótese de solução e o valor esperado.**

Essa distinção conecta o MVA aqui proposto à literatura de *problem discovery*: problema e solução não precisam ser tratados como elementos totalmente definidos antes do experimento. A experimentação pode aumentar a clareza sobre ambos.

### Gemba e a descoberta na operação

A etapa de descoberta também incorpora um princípio do **Lean**, o **Gemba** — a prática de ir ao local onde o trabalho e a criação de valor realmente acontecem. Na descoberta de oportunidades de automação, isso significa privilegiar a observação e a conversa com as pessoas que executam o processo, em vez de depender exclusivamente da descrição formal feita por quem o projetou ou gerencia.

A Info-Tech inclui essa prática em sua abordagem de automação e chama atenção para o risco de decisões baseadas em pressupostos de pessoas distantes da execução. Para o MVA, Gemba sustenta um princípio operacional:

> **O processo documentado é uma fonte; o processo executado é evidência.**

Entrevistas, observação e contato direto com quem realiza o trabalho alimentam a formulação inicial do problema. Formulários e mecanismos de coleta em maior escala podem ser usados posteriormente para estimar recorrência, alcance e impacto.

### Elementos de BPA que dialogam com o MVA

A literatura prática de Business Process Automation também oferece elementos úteis para a evolução desta metodologia, entre eles:

- **backlog de oportunidades**, para registrar, comparar e priorizar problemas e oportunidades;
- **avaliação de risco e mudança**, para considerar impacto, risco e disposição organizacional antes da expansão;
- **métricas de valor da automação**, como tempo, custo, velocidade, erros e compliance;
- **governança e maturidade**, especialmente na transição entre experimento e escala.

Esses elementos serão tratados como referências para o desenvolvimento do MVA, e não como reprodução integral de uma metodologia existente.

## 2. Princípio central

**O problema é conhecido; a automação é uma hipótese a ser descoberta e testada.**

A metodologia não parte da pergunta “o que podemos fazer com IA?”, mas da compreensão de um problema concreto da organização.

Isso significa que descobrir o MVA faz parte do MVA.

## 3. O MVA como metodologia cíclica

O MVA não deve ser entendido como um fluxo linear no qual o problema é definido uma única vez e, em seguida, transformado em uma automação. Ele é uma **metodologia cíclica de experimentação**.

A descoberta inicial produz uma formulação provisória do problema. A partir dela, são levantadas hipóteses e construído um experimento mínimo de automação. Os resultados desse experimento geram evidências que podem confirmar aspectos da hipótese, revelar novas dimensões do problema ou exigir sua reformulação.

Assim, a própria qualidade da definição do problema evolui conforme as iterações do MVA. O experimento não testa apenas uma solução: ele também produz conhecimento sobre o problema que originou a iniciativa.

A lógica se aproxima do método científico: observar uma situação, formular um problema, levantar uma hipótese, experimentar, medir os resultados e usar as evidências obtidas para refinar o entendimento e realizar um novo ciclo.

Essa visão encontra suporte empírico no estudo de **Johnathan R. Cromwell e Jean-François Harvey (2025)**, publicado na *Research Policy*. Os autores acompanharam **579 equipes** participantes de uma competição interna de inovação em uma empresa Fortune Global 500 para investigar como a clareza do problema evolui ao longo de projetos de inovação.

O resultado é particularmente relevante para o MVA: equipes que começaram com **menor clareza do problema e aumentaram essa clareza ao longo do desenvolvimento das ideias de solução** — processo que os autores chamam de *team problem discovery* — apresentaram uma taxa de conclusão de projetos de aproximadamente **80%**. Já equipes que seguiram uma trajetória mais tradicional, começando com alta clareza e mantendo-a durante o projeto, apresentaram aproximadamente **50%** de conclusão.

Os autores também destacam que o processo de *team problem discovery* é impulsionado por uma dinâmica de **exploração de ideias seguida de exploração orientada à execução (*exploitation*)**. Para o MVA, a implicação não é que problemas devam permanecer vagos, mas que **a formulação do problema pode e deve ganhar qualidade por meio da experimentação**. A solução em desenvolvimento produz evidências que ajudam a equipe a compreender melhor o próprio problema.

Essa evidência reforça a escolha do MVA por um ciclo no qual **problema, hipótese e experimento evoluem conjuntamente**, em vez de tratar a definição inicial do problema como uma especificação imutável.

> Cromwell, J. R.; Harvey, J.-F. (2025). *A problem half-solved is a problem well-stated: Increasing the rate of innovation through team problem discovery*. Research Policy, 54(3), 105186. [Artigo — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0048733325000150) · [DOI: 10.1016/j.respol.2025.105186](https://doi.org/10.1016/j.respol.2025.105186) · [Dados e código — Open Science Framework](https://osf.io/d5894/)

Por esse motivo, o objetivo não é "comprovar" previamente uma solução. O objetivo é **gerar evidências suficientes para sustentar uma decisão**.

### Ciclo canônico v0.1

```text
OBSERVAÇÃO
Identificar a fricção na operação
      ↓
FORMULAÇÃO DO PROBLEMA
Estruturar problema, impacto e população afetada
      ↓
HIPÓTESE
Definir a mudança esperada e o valor que ela pode gerar
      ↓
MODELAGEM E CONTEXTO
Compreender o processo e preparar o contexto necessário
      ↓
EXPERIMENTAÇÃO — MVA
Construir o experimento mínimo capaz de testar a hipótese
      ↓
MENSURAÇÃO
Comparar os resultados com a situação de referência
      ↓
APRENDIZADO
Interpretar o que as evidências dizem sobre a hipótese e sobre o problema
      ↓
DECISÃO
Iterar, reformular, validar, avançar ou interromper
      │
      └──────────────────────────────→ novo ciclo
```

A saída de um ciclo não precisa ser uma automação pronta para escala. Ela pode ser uma hipótese mais precisa, uma nova compreensão do problema, uma alteração no contexto necessário, uma nova versão do MVA ou a decisão de não continuar.

### Evidência e números

Cada MVA deve nascer com uma expectativa de impacto que possa ser observada. A métrica depende da natureza do problema: tempo, custo, esforço, qualidade, capacidade operacional, retrabalho, bloqueio ou outro indicador relevante.

Os números cumprem duas funções: permitem comparar a situação anterior com o resultado do experimento e fornecem critérios para decidir se há evidência suficiente para iniciar um novo ciclo, validar o MVA ou interromper a iniciativa.

## 4. Etapas

### 4.1. Descoberta do problema

A primeira etapa busca estabelecer uma definição compartilhada do problema.

O framework inicial deve responder, pelo menos:

1. **Qual é o problema?**
2. **Onde esse problema se manifesta?**
3. **Quem sofre esse problema?**
4. **Como seria a vida ou o trabalho dessa pessoa sem esse problema?**

O objetivo ainda não é propor uma solução definitiva. É produzir uma **formulação inicial do problema**, suficientemente clara para permitir a construção de hipóteses e o primeiro experimento. Essa formulação é provisória: ela poderá ser refinada pelas evidências produzidas durante os ciclos do MVA.

#### Como descobrir problemas

A descoberta deve começar, sempre que possível, em uma área ou equipe pequena e próxima da operação. Um caminho inicial é disponibilizar espaço para entrevistas individuais e utilizar o framework de perguntas como roteiro.

O conhecimento do processo está principalmente com **quem executa o trabalho**, e não apenas com quem desenhou ou documentou o processo. A realidade operacional frequentemente diverge do planejamento formal.

A entrevista pessoal é especialmente importante nos primeiros ciclos porque uma fricção recorrente afeta diretamente a experiência de quem executa aquele trabalho. A conversa permite compreender não apenas a descrição formal do problema, mas seus efeitos, frequência, contexto e consequências.

Depois das primeiras entrevistas, a descoberta pode ser ampliada por formulários ou outros mecanismos de coleta para identificar recorrência e estimar quantas pessoas são afetadas pelo mesmo problema. Essa informação alimenta a priorização por impacto.

#### Entrevista de descoberta

A descoberta do problema começa pela experiência concreta de quem executa o trabalho. A entrevista não deve começar perguntando diretamente **“qual é o seu problema?”**. A pessoa entrevistada conhece profundamente sua rotina, mas nem sempre formula as fricções que vive como problemas estruturados ou oportunidades de automação.

Por isso, a primeira parte da entrevista deve privilegiar **narrativa, rapport e escuta**. O entrevistador convida a pessoa a contar histórias sobre seu trabalho e acompanha o percurso real da operação.

Perguntas de abertura podem incluir:

- **Me conta um pouco sobre o seu trabalho e como é um dia normal para você.**
- **Quais atividades você realiza com mais frequência?**
- **Quais processos ou tarefas se repetem mais ao longo da sua rotina?**
- **Você consegue me contar como executa uma dessas atividades, do começo ao fim?**

A **frequência** é um sinal importante desde o início: uma fricção aparentemente pequena pode representar grande impacto quando ocorre muitas vezes, para a mesma pessoa ou para muitas pessoas.

O papel do entrevistador nesta fase é ouvir a história e identificar **tensões na operação**: momentos de interrupção, espera, repetição, retrabalho, improviso, troca excessiva entre ferramentas, dependência de outras pessoas, esforço cognitivo, estresse ou qualquer outro ponto em que o trabalho deixa de fluir como esperado.

As tensões devem ser anotadas durante a conversa. Quando aproximadamente **três tensões mais aparentes** tiverem emergido, o entrevistador pode começar a explorá-las individualmente e preencher a ficha de síntese do problema.

##### Duração e formatos

Como referência, uma entrevista de descoberta deve ter aproximadamente **40 a 60 minutos**, permitindo profundidade suficiente para compreender a rotina e explorar as tensões encontradas.

O processo pode acontecer em uma única entrevista ou ser dividido em duas conversas:

1. **Entrevista de detecção** — predominantemente narrativa, voltada à rotina, aos processos frequentes e à identificação das tensões.
2. **Entrevista de detalhamento** — opcional, utilizada quando é necessário retornar ao entrevistado para compreender melhor uma ou mais tensões e completar a documentação.

A ficha de síntese pode ser iniciada **durante a própria entrevista**. Ela não é um diagnóstico definitivo: é uma formulação provisória que continuará sendo qualificada pelas próximas etapas e pelos ciclos de experimentação do MVA.

#### Ficha de síntese do problema

Cada tensão selecionada deve gerar uma ficha própria. O objetivo é transformar uma observação narrativa em uma formulação de problema que possa posteriormente ser priorizada, modelada e testada.

O framework deve responder:

1. **Qual é o nome do problema?**  
   Dê um nome curto e reconhecível à tensão observada.

2. **Como esse problema se manifesta?**  
   O que acontece concretamente quando o problema ocorre?

3. **Em que momento ele aparece?**  
   Em qual atividade, etapa ou situação do trabalho essa tensão surge? Ex.: “quando vou executar X, acontece Y”.

4. **Como a pessoa lida com esse problema hoje? Qual é o processo atual?**  
   Reconstrua o caminho real: onde começa, por quais etapas passa, quais ferramentas utiliza, quais pessoas ou sistemas são acionados e o que é feito para conseguir concluir a tarefa apesar da tensão.

5. **Quem mais sofre com esse problema?**  
   Identifique outras pessoas, funções ou áreas que vivenciam a mesma tensão. Quando possível, estime o volume de pessoas afetadas e pergunte se o entrevistado pode indicar outras pessoas que deveriam ser ouvidas. Essas indicações ajudam simultaneamente a medir a recorrência do problema e a ampliar a descoberta com novos pontos de vista.

6. **Com que frequência esse problema acontece?**  
   Registre quantas vezes a tensão aparece em um período relevante para aquela atividade — por dia, semana, mês ou ciclo de trabalho. A frequência deve ser entendida em duas dimensões: **recorrência temporal** (quantas vezes acontece) e **recorrência entre pessoas** (quantas pessoas enfrentam a mesma situação).

7. **Como seria a vida ou o trabalho dessa pessoa sem esse problema?**  
   Explore o estado desejado sem pressupor uma solução tecnológica. O que ela faria em seguida? O que ficaria mais rápido ou simples? Quanto tempo poderia ser economizado? O processo seria menos estressante? Que impacto essa mudança teria no trabalho e na experiência dessa pessoa?

A última pergunta é especialmente importante porque começa a revelar o **valor potencial** da resolução do problema. Nesse momento ainda não se define a automação. Busca-se compreender a distância entre a experiência atual e uma experiência em que aquela tensão foi removida, reduzida ou simplificada.

### 4.2. Priorização por impacto

Depois de identificados os problemas, começa uma etapa de **sincronização** das fichas produzidas nas entrevistas. Problemas descritos por pessoas diferentes podem representar a mesma tensão operacional. Antes de comparar oportunidades, essas ocorrências devem ser agrupadas para que a organização consiga enxergar padrões.

#### Primeiro filtro: frequência

O primeiro filtro de priorização é a **frequência**, entendida em duas dimensões complementares:

1. **Frequência temporal — quantas vezes acontece?**  
   Quantas vezes o problema ocorre por dia, semana, mês ou ciclo operacional?

2. **Frequência entre pessoas — com quantas pessoas acontece?**  
   Quantas pessoas, funções, equipes ou áreas relatam a mesma tensão?

Um problema que parece pequeno em uma entrevista pode ter grande impacto acumulado quando ocorre dezenas de vezes por dia ou quando se repete para muitas pessoas. Por isso, a frequência ajuda a distinguir uma dificuldade individual e ocasional de uma tensão potencialmente sistêmica.

As próprias entrevistas alimentam esse filtro. Ao perguntar **“quem mais sofre com esse problema?”**, o entrevistador identifica novas pessoas que podem ser ouvidas e começa a estimar o alcance da tensão. Novas entrevistas podem confirmar, ampliar ou enfraquecer a hipótese de recorrência.

A frequência não determina sozinha qual problema deverá virar um MVA. Ela funciona como **primeiro filtro** para selecionar quais problemas merecem uma análise mais profunda de impacto.

Depois desse filtro, o impacto pode ser observado por outras dimensões, entre elas:

- **Custo:** quanto dinheiro o problema gera ou consome.
- **Tempo:** quantas horas ou quanto esforço são consumidos.
- **Impacto operacional:** como o problema afeta a execução de um processo.
- **Impacto impeditivo:** quando o problema impede a organização, uma área ou uma pessoa de realizar algo relevante.

A priorização ajuda a evitar a construção de automações tecnicamente interessantes, mas de baixo valor para a organização.

#### Pré-análise assistida por modelo

Antes da reunião de priorização, as fichas de síntese podem ser consolidadas com apoio de um modelo de linguagem. O papel do modelo é **organizar evidências, e não decidir pela organização**.

Para cada problema, a consolidação deve buscar, quando os dados existirem:

- frequência temporal;
- número estimado de pessoas, funções ou áreas afetadas;
- tempo consumido ou perdido;
- retrabalho;
- custo identificado;
- impacto operacional;
- caráter impeditivo;
- riscos relatados;
- ferramentas, sistemas e etapas envolvidas.

Quando uma informação não estiver disponível, o modelo deve marcá-la como **não identificada**, sem estimar ou inventar valores. O modelo também pode agrupar relatos que pareçam representar a mesma tensão, apontar divergências, identificar lacunas e produzir uma hipótese inicial de priorização com justificativa.

##### Prompt-base para consolidação

```text
Você está apoiando a priorização de problemas candidatos a um MVA
(Minimum Viable Automation).

Analise exclusivamente as entrevistas e fichas fornecidas.

1. Identifique problemas que possam representar a mesma tensão,
   mesmo quando descritos com nomes diferentes.
2. Para cada problema consolidado, extraia somente dados presentes
   nas evidências:
   - frequência temporal;
   - número de pessoas/áreas afetadas;
   - tempo consumido;
   - retrabalho;
   - custo;
   - impacto operacional;
   - caráter impeditivo;
   - riscos;
   - ferramentas e sistemas envolvidos.
3. Nunca preencha lacunas com estimativas próprias.
   Use "não identificado" quando não houver evidência.
4. Diferencie fatos relatados, percepções dos entrevistados e inferências.
5. Aponte contradições e dados que precisam ser confirmados.
6. Produza uma pré-análise de priorização e explique os critérios utilizados.
7. Destaque quais problemas parecem claramente relevantes pelos dados
   e quais dependem de julgamento humano.
8. Não escolha o MVA. A decisão final pertence às pessoas responsáveis
   pela operação e à liderança.
```

#### Dinâmica de priorização com a liderança

A decisão final acontece em uma reunião de priorização. A pré-análise do modelo funciona como material de apoio, mas a liderança e as pessoas que conhecem a operação adicionam uma dimensão que os dados isolados não capturam: **a percepção organizacional de valor**.

Cada problema candidato é representado em um post-it ou cartão. Os participantes discutem os problemas e os posicionam em uma matriz de quatro quadrantes:

```text
                     VALOR
                       ↑
                       │
        ALTO VALOR     │     ALTO VALOR
       BAIXO ESFORÇO   │     ALTO ESFORÇO
                       │
───────────────────────┼──────────────────────→ ESFORÇO
                       │
        BAIXO VALOR    │     BAIXO VALOR
       BAIXO ESFORÇO   │     ALTO ESFORÇO
                       │
```

**Valor** representa a percepção coletiva do benefício de reduzir ou remover aquela tensão, apoiada pelos números disponíveis.

**Esforço** significa o esforço necessário para **construir o experimento MVA**, e não o esforço estimado para desenvolver e implantar uma solução final em escala. Uma automação potencialmente complexa pode ter um experimento inicial simples.

O objetivo da matriz não é produzir uma pontuação matemática perfeita. Ela serve para tornar visíveis divergências, dúvidas e diferentes percepções de valor. Problemas cuja prioridade já é evidente pelos dados podem demandar pouca discussão; a reunião deve concentrar tempo principalmente nos casos ambíguos.

Ao final, o grupo seleciona o **primeiro candidato a MVA**.

**Princípio de decisão:** o modelo organiza e evidencia; as pessoas interpretam e decidem.

### 4.3. Modelagem do problema

Depois que um problema é priorizado, inicia-se uma nova etapa com as pessoas que vivem aquela tensão na operação. O objetivo é sair da formulação resumida da ficha e construir uma representação compartilhada de **como o problema funciona hoje**.

Essa etapa acontece preferencialmente em uma sessão facilitada de aproximadamente **60 a 90 minutos**, com um pequeno grupo de pessoas diretamente afetadas ou envolvidas no processo.

A sessão deve produzir três artefatos principais:

1. **Fluxo atual do problema**  
   Um fluxograma do processo real, reconstruído passo a passo a partir da execução cotidiana — e não apenas do processo oficial ou documentado.

2. **Mapa de influências**  
   Identificação dos elementos que interferem no fluxo: pessoas, decisões, regras, sistemas, dependências, exceções, eventos e condições que alteram o caminho normal.

3. **Mapa de contexto**  
   Identificação das informações necessárias em cada etapa: o que a pessoa precisa saber para agir ou decidir, de onde essa informação vem, em qual formato está disponível, quem pode acessá-la e quais lacunas existem.

#### Roteiro da sessão de modelagem

O facilitador reconstrói o processo junto aos participantes. Para cada etapa, deve buscar respostas para perguntas como:

- Onde esse processo começa?
- O que dispara essa atividade?
- Qual é a primeira ação realizada?
- O que acontece em seguida?
- Quem participa dessa etapa?
- Qual decisão precisa ser tomada?
- O que pode mudar o caminho normal?
- Quais exceções acontecem?
- Que ferramenta ou sistema é utilizado?
- Que informação é necessária para executar essa etapa?
- De onde essa informação vem?
- Quem tem acesso a ela?
- Em qual formato ela existe?
- O que acontece quando essa informação não está disponível ou está errada?
- Onde exatamente a tensão priorizada aparece no fluxo?
- O que acontece depois dela?

O facilitador deve desenhar o fluxograma **durante a reunião**, validando com os participantes se a representação corresponde ao processo realmente executado.

#### Formato mínimo do fluxograma

Cada elemento do fluxo deve, quando aplicável, registrar:

```text
[Entrada / gatilho]
        ↓
[Etapa]
- Quem executa?
- O que faz?
- Ferramenta/sistema
- Contexto necessário
        ↓
<Decisão / condição?>
      ↙   ↘
   caminho A   caminho B
        ↓
[Exceções / dependências]
        ↓
[Próxima etapa / saída]
```

O ponto ou os pontos em que o problema se manifesta devem ser destacados no desenho.

A sessão começa pela construção da **arquitetura do problema** — fluxo, influências e contexto — mas não precisa terminar nela. Depois que os participantes conseguem enxergar coletivamente como o problema funciona, a própria reunião pode avançar para a formulação de uma **primeira hipótese de automação**.

Essa hipótese deve nascer com participação das pessoas que sofrem o problema. Elas ajudam a responder onde uma intervenção poderia reduzir a tensão, o que deveria mudar no fluxo e como seria possível perceber que houve melhora.

A saída da sessão passa, portanto, a incluir quatro artefatos:

1. **Fluxo atual do problema**;
2. **Mapa de influências**;
3. **Mapa de contexto**;
4. **Hipótese inicial de automação**, construída e reconhecida pelas pessoas que vivem o problema.

Essa primeira hipótese ainda não é uma especificação técnica nem uma decisão de implementação. Ela é uma **hipótese orientada pela experiência**: traduz a percepção de quem conhece o problema por vivê-lo diariamente e registra uma possibilidade inicial de intervenção.

Uma formulação mínima pode assumir a forma:

> **Se intervirmos em [ponto do fluxo] por meio de [capacidade ou mudança proposta], esperamos reduzir [tensão observada] e produzir [efeito esperado], que poderá ser observado por [evidência ou métrica].**

A hipótese deve também registrar quais condições precisam ser verdadeiras para que ela faça sentido e quais dúvidas permanecem abertas.

**Princípio:** a arquitetura da automação não vem antes da arquitetura do problema. A primeira hipótese de automação nasce da compreensão compartilhada dessa arquitetura.

### 4.4. Ontologia do problema

Uma vez priorizado, o problema é decomposto e modelado.

Essa ontologia busca representar:

- as etapas pelas quais o problema passa;
- os atores envolvidos;
- os acontecimentos e decisões relevantes;
- as relações entre as etapas;
- os pontos nos quais contexto é necessário.

Essa representação cria uma visão comum do problema antes da construção da automação.

### 4.5. Refinamento técnico da hipótese

A hipótese produzida na sessão de modelagem preserva a perspectiva de quem sofre o problema, mas ainda é deliberadamente pouco técnica. O passo seguinte é entregá-la ao **time responsável por inovação, automação ou pelo desenvolvimento do MVA**, que deverá refiná-la sem perder a conexão com a tensão original.

Esse time combina conhecimento sobre o processo com conhecimento técnico de automação. Seu papel não é substituir a hipótese das pessoas da operação por uma solução tecnológica pronta, mas desenvolver **hipóteses técnicas derivadas** que possam ser experimentadas.

O refinamento deve analisar, entre outros pontos:

- se a intervenção proposta é tecnicamente experimentável;
- quais dados e contextos seriam necessários;
- se esses contextos existem ou podem ser simulados;
- quais ferramentas, integrações ou capacidades seriam necessárias;
- quais restrições, dependências e riscos existem;
- quais partes do processo precisam permanecer humanas no experimento;
- qual seria o menor experimento capaz de produzir evidência útil;
- quais métricas permitiriam comparar o experimento com a situação atual.

O foco desta análise é a **viabilidade do experimento**, e não a viabilidade ou arquitetura definitiva de uma solução em escala.

A primeira hipótese pode ser mantida, reformulada ou desdobrada em múltiplas hipóteses técnicas. Cada uma deve continuar rastreável ao problema, ao ponto do fluxo e ao valor esperado identificados na sessão de modelagem.

A relação entre as duas camadas pode ser representada assim:

```text
PESSOAS QUE VIVEM O PROBLEMA
          ↓
Arquitetura do problema
          ↓
Hipótese orientada pela experiência
          ↓
TIME DE INOVAÇÃO / AUTOMAÇÃO
          ↓
Análise de viabilidade do experimento
          ↓
Hipótese(s) técnica(s) de automação
          ↓
Definição do experimento MVA
```

Essa separação reduz dois riscos opostos: construir uma automação tecnicamente sofisticada que não resolve a tensão real, ou transformar uma boa percepção da operação em uma hipótese tecnicamente inviável.

**Princípio:** a operação qualifica o problema e a mudança desejada; o time de inovação transforma essa compreensão em hipóteses experimentáveis.

### 4.6. Fontes de contexto

A partir da ontologia, são identificadas e listadas as fontes de contexto necessárias para compreender e atuar sobre o problema.

Essas fontes podem incluir documentos, dados estruturados, conhecimento de pessoas, regras, sistemas, históricos, procedimentos e outras informações necessárias ao processo.

Nesta etapa, a pergunta central é:

**Que contexto uma automação precisaria ter para conseguir atuar sobre esse problema?**

### 4.7. Geração de contexto sintético

Com as fontes de contexto mapeadas, é criado um conjunto de contexto sintético capaz de representar suficientemente as condições do problema para permitir os primeiros experimentos.

O objetivo é criar um ambiente controlado de teste antes da dependência de dados reais, integrações definitivas ou exposição desnecessária de informações sensíveis.

O contexto sintético não precisa reproduzir toda a realidade. Ele precisa ser suficientemente representativo para testar as hipóteses do MVA.

### 4.8. Construção e versões do MVA

Com problema, ontologia e contexto disponíveis, começam os experimentos de automação.

A primeira versão não pretende ser uma solução final. Ela existe para testar uma hipótese.

Cada versão deve produzir aprendizado que alimente a seguinte:

```text
Hipótese → Construção → Teste → Evidência → Aprendizado → Nova versão
```

O MVA evolui por ciclos sucessivos até atingir um estado em que faça sentido submetê-lo à validação de outras pessoas.

### 4.9. Validação

A automação é apresentada a pessoas capazes de avaliar sua utilidade no contexto real do problema.

A validação deve responder principalmente:

**Esta automação gera valor para a resolução do problema que originou o MVA?**

As métricas dependem da natureza do problema e podem envolver tempo, custo, qualidade, esforço, redução de retrabalho, capacidade operacional ou outros indicadores definidos durante a descoberta.

### 4.10. Decisão

A validação gera evidências para decidir o próximo movimento.

Entre as possibilidades estão:

- continuar iterando o MVA;
- realizar uma nova rodada de validação;
- avançar para testes com contexto ou dados reais;
- preparar uma etapa de escala;
- reformular a hipótese;
- interromper a iniciativa caso o valor esperado não seja confirmado.

A decisão é consequência da evidência produzida pelo experimento, e não da existência prévia de uma tecnologia ou solução.

## 5. MVA e MVP

O MVA toma emprestada do conceito de **Minimum Viable Product (MVP)** a lógica de reduzir o tamanho inicial de uma iniciativa para acelerar aprendizado e validação.

Entretanto, o objeto de experimentação é diferente.

No MVP, o experimento está normalmente associado à validação de um produto e de sua proposta de valor.

No MVA, o objeto de descoberta é uma **automação aplicada a um problema e a um processo organizacional**.

A metodologia MVA começa antes da construção da automação: inclui descobrir e modelar o problema, compreender seu impacto, identificar o contexto necessário e formular a hipótese que será experimentada.

## 6. Pontos a desenvolver nas próximas versões

- Framework completo de descoberta do problema.
- Modelo de priorização e impacto.
- Método para construção da ontologia do problema.
- Framework de fontes de contexto.
- Critérios para geração e qualidade de contexto sintético.
- Regras para versionamento dos MVAs.
- Framework de métricas e validação.
- Critérios de passagem de experimento para escala.
- Segurança, governança e tratamento de dados.
- Papéis e responsabilidades dentro da organização.
- Educação e capacitação necessárias para adoção da metodologia.
- Relação entre MVA, IA generativa, agentes e automações tradicionais.

---

**Status:** documento inicial para desenvolvimento e versionamento da metodologia.


## 7. Referências

- Cromwell, J. R., & Harvey, J.-F. (2025). **A problem half-solved is a problem well-stated: Increasing the rate of innovation through team problem discovery.** *Research Policy, 54*(3), 105186. DOI: [10.1016/j.respol.2025.105186](https://doi.org/10.1016/j.respol.2025.105186). [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0048733325000150). Dados e código de análise disponibilizados pelos autores no [Open Science Framework](https://osf.io/d5894/).

- Knight, A. (2016). **Minimum Viable Automation.** *A Sisyphean Task*. [Texto original](https://www.a-sisyphean-task.com/2016/03/minimum-viable-automation.html).
- Info-Tech Research Group. **Develop Your Value-First Business Process Automation Strategy.** [Material de pesquisa](https://www1.infotech.com/research/ss/develop-your-value-first-business-process-automation-strategy).
