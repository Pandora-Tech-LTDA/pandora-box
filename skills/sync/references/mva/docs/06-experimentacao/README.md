# 06 — Experimentação MVA

**Objetivo:** transformar a hipótese técnica em um experimento executável, inicialmente desacoplado de integrações e dados vivos, e produzir evidência sobre seu funcionamento e valor.

## 6.1. Contexto antes da automação

O primeiro experimento não depende de conexão com a infraestrutura real. A partir do mapa de contexto, o time cria representações sintéticas suficientes para permitir que o construtor se concentre na **lógica da automação e no resultado esperado**.

Essas representações não precisam reproduzir exatamente o futuro payload de uma API ou esquema produtivo. Podem partir de colunas inferidas, CSV, planilhas, Markdown ou outros formatos plausíveis.

**Regra:** ausência de API ou conector não impede o MVA; adia o teste de integração.

## 6.2. Pacote mínimo executável

O experimento pode ser implementado em ambientes capazes de executar workflows com modelos, arquivos, skills e ferramentas. Seu núcleo é um conjunto de instruções que combina:

- problema e hipótese;
- objetivo;
- contexto disponível;
- workflow esperado;
- ferramentas/skills necessárias;
- critérios de sucesso;
- métricas externas e internas;
- formato de saída;
- casos de teste.

O construtor deve materializar também os arquivos necessários ao experimento, como Markdown, CSV e outros artefatos de contexto.

Ver [Agente Construtor de Experimentos MVA](../../templates/agente-construtor-experimento.md).

## 6.3. Validação funcional

As pessoas que participaram da construção da hipótese apresentam casos concretos e observam a saída da automação.

A validação é simples: **isso atende ou não atende? Por quê?**

O feedback sobre conteúdo, formato, ausência de informação ou comportamento esperado alimenta a próxima versão das instruções, contexto ou workflow.

## 6.4. Transição para a estrutura real

A passagem do sintético para o real acontece em três estados:

```text
Contexto sintético exploratório
        ↓
Contrato de dados real conhecido
        ↓
Contexto sintético compatível com o contrato real
        ↓
Novo teste do workflow
        ↓
Conexão progressiva com dados vivos
```

Quando TI disponibiliza o esquema definitivo — payload de API, tabela, campos, tipos e relações — o time recria os dados sintéticos nesse formato. O prompt e o workflow são adaptados e testados novamente **antes** de tocar dados vivos.

Esse teste responde: **a automação continua funcionando quando a estrutura é real, mesmo que os dados ainda não sejam?**

## 6.5. Conexões reais

Depois da validação com estrutura real sintética, fontes vivas são conectadas progressivamente. Isso pode exigir apoio de TI ou utilizar conectores nativos do ambiente.

**Conectar uma fonte por vez e testar novamente.**

A evolução deve ser documentada: fonte conectada, status, estrutura recebida, consistência do payload, erros encontrados e correções.

Durante esta fase, a automação deve operar de forma suficientemente verbosa para permitir depuração e checagem de confiabilidade.

### Checklist de confiabilidade

- Acessa todas as ferramentas necessárias?
- Cada conector funciona isoladamente?
- Os dados esperados estão chegando?
- Campos e tipos correspondem ao contrato?
- Existem dados ausentes ou inesperados?
- As buscas retornam as fontes corretas?
- O workflow executa de ponta a ponta?
- O resultado é sustentado pelos dados recuperados?
- Há sinais de conteúdo inventado ou não sustentado?
- Os casos de teste continuam passando após cada conexão?

## 6.6. Uso em contexto real

Com as fontes vivas conectadas, o MVA volta para a mão de quem vive a dor — idealmente o sponsor e um pequeno grupo de pessoas afetadas.

O objetivo é incorporar o experimento ao fluxo real durante um período e observar se o valor identificado nas etapas anteriores permanece quando a automação trabalha com contexto vivo.

A adoção não é tratada isoladamente como um problema de comportamento. A hipótese central é que **uma dor relevante e corretamente compreendida cria motivação para experimentar uma solução que efetivamente a reduza**. A observação em contexto real testa também a qualidade da descoberta inicial.

## 6.7. Cadência esperada

As durações abaixo são **hipóteses de referência**, não um cronograma rígido. Elas devem ser recalibradas à medida que a metodologia acumular evidências de campo. Etapas podem ocorrer em paralelo.

| Etapa | Faixa inicial |
|---|---|
| Descoberta — aproximadamente 12–15 entrevistas + consolidação | ~2 semanas |
| Priorização | 2–3 dias |
| Modelagem + hipótese inicial | 1 sessão de 60–90 min por problema priorizado |
| Refinamento técnico | 1–3 dias |
| Construção do experimento sintético | 3–5 dias |
| Validação funcional e iterações iniciais | 2–5 dias |
| Adequação ao contrato real, incluindo interação com TI | ~2 semanas |
| Conexão progressiva com fontes vivas | 1–2 semanas |
| Uso acompanhado em contexto real | 2–4 semanas |

Como referência inicial, um ciclo completo pode ocupar aproximadamente **8–12 semanas**, com sobreposição entre atividades.

**Tempo de construção não é tempo de evidência.** O workflow pode estar executável cedo, mas confiança suficiente para uma decisão depende também de observação em contexto real.

## 6.8. Saída da experimentação

Ao final, o MVA não está automaticamente “pronto para escala”. Ele está **pronto para uma decisão sustentada por evidências**: iterar, reformular, interromper ou iniciar um processo de escala.
