# MVA — Minimum Viable Automation

O **MVA** é uma metodologia cíclica para descobrir, testar e validar automações a partir de problemas reais da operação.

Em vez de começar pela ferramenta ou pela integração, o MVA começa pela **dor de quem executa o trabalho**, transforma essa dor em uma hipótese experimentável e testa valor com baixo risco antes de avançar para dados vivos e escala.

> **Status:** v0.1 — metodologia em desenvolvimento e pesquisa aplicada.

## Visão geral

```text
1. DESCOBERTA
   Entender a rotina e encontrar tensões reais
        ↓
2. PRIORIZAÇÃO
   Escolher um problema relevante e recorrente
        ↓
3. MODELAGEM
   Desenhar o processo, influências e contexto
        ↓
4. HIPÓTESE
   Formular e refinar uma automação experimentável
        ↓
5. CONTEXTO
   Criar contexto sintético suficiente para testar
        ↓
6. EXPERIMENTAÇÃO
   Construir, testar, medir e conectar progressivamente
        ↓
7. VALIDAÇÃO
   Colocar na mão de quem vive a dor e decidir
        ↺
   Aprendizado alimenta um novo ciclo
```

## Etapas

| Etapa | O que acontece | Principal saída |
|---|---|---|
| [**1. Descoberta**](docs/01-descoberta/README.md) | Entrevistas com quem executa o trabalho para identificar tensões, recorrência e impacto percebido. | Fichas de problemas |
| [**2. Priorização**](docs/02-priorizacao/README.md) | Problemas semelhantes são consolidados e avaliados por frequência, valor e esforço experimental. | Problema candidato ao MVA |
| [**3. Modelagem**](docs/03-modelagem/README.md) | O grupo reconstrói o processo real, suas influências e o contexto necessário. | Arquitetura do problema + hipótese inicial |
| [**4. Hipóteses**](docs/04-hipoteses/README.md) | O time de inovação transforma a hipótese da operação em uma hipótese tecnicamente experimentável. | Hipótese técnica |
| [**5. Contexto**](docs/05-contexto/README.md) | Fontes são mapeadas e representações sintéticas são preparadas sem depender inicialmente de integrações reais. | Contexto para experimentação |
| [**6. Experimentação**](docs/06-experimentacao/README.md) | O workflow é construído, testado, adaptado ao contrato real e conectado progressivamente a fontes vivas. | MVA funcionando em contexto real |
| [**7. Validação**](docs/07-validacao/README.md) | Quem vive a dor utiliza o MVA e as evidências orientam a próxima decisão. | Iterar, reformular, interromper ou preparar escala |

## Princípios

- **O problema vem antes da automação.**
- **O processo executado é evidência; o processo documentado é uma fonte.**
- **O modelo organiza e evidencia; as pessoas interpretam e decidem.**
- **Contexto sintético permite aprender antes de depender da infraestrutura real.**
- **O MVA produz evidência para decisão — não uma obrigação de escalar.**

## Base de trabalho

- [Visão geral da metodologia](docs/00-visao-geral.md)
- [Playbook de consultoria](playbook/README.md)
- [Aplicações da metodologia](applications/README.md)
- [Templates](templates/README.md)
- [Referências e fundamentação](references/README.md)
- [Decisões metodológicas](decisions/README.md)
- [Snapshot do whitepaper v0.1](docs/whitepaper-v0.1.md)

---

Esta base é mantida como **pesquisa aplicada**: aprendizados das consultorias geram evidências, que podem alterar hipóteses, templates e a própria metodologia em ciclos futuros.
