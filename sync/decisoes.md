# Decisões

Projeto: skill `/sync-spec`, da família Sync (Pandora Box). As decisões D1 a D4 vieram da conversa anterior e também estão em `skills/sync/DECISOES.md`.

## D1. Nome e papel da skill
- **Data:** 2026-11-19
- **Decisão:** a skill se chama `/sync-spec` e gera o mapa de requisitos (`sync/requisitos.md`): a documentação necessária para começar a desenvolver, incluindo referências, direção visual, telas e wireframes.
- **Motivo:** "depois do sync-docs, ele precisa de um mapa de requerimentos, que é a documentação necessária para começar a desenvolver alguma coisa"; "sync-spec fica melhor".
- **Alternativas descartadas:** `/sync-map` e `/sync-reqs`.

## D2. Lugar no fluxo
- **Data:** 2026-11-19
- **Decisão:** o `/sync-docs` recomenda, com motivo, o próximo passo: `/sync-mva` para automações e agentes, `/sync-spec` para produtos com telas; quando for os dois, MVA primeiro e spec depois. A escolha final é do usuário.
- **Motivo:** "precisa informar o sync-docs qual seria o próximo passo mais coerente, se é mva ou spec".

## D3. Design system de referência
- **Data:** 2026-11-19
- **Decisão:** a família terá um design system básico de referência, com pelo menos dois temas genéricos da Pandora, claro e escuro, usado quando o usuário não tiver marca própria.
- **Motivo:** "é importante termos algumas paletas prontas para design padrão, como um tema pandora genérico branco e outro preto muito bom; vale a pena já ter um design system de referência bem básico".

## D4. Fontes para derivar
- **Data:** 2026-11-19
- **Decisão:** derivar de `to-spec` e `prototype` (Matt Pocock, MIT), `wireframes` (ba-toolkit, MIT) e `aidlc-requirements` (AWS, MIT-0).
- **Motivo:** escolhidas na pesquisa no GitHub por cobrirem, juntas, síntese do registro, telas com estados e validação de lacunas, com licenças que permitem derivar.

## D5. Público da spec
- **Data:** 2026-11-19
- **Decisão:** a spec é escrita principalmente para IAs de código (várias, não uma só). Precisa ser explícita, sem ambiguidade e independente de ferramenta.
- **Motivo:** "muito provavelmente uma IA de código, mas várias delas, na verdade. A especificação vai ter que ser bem voltada para IA de código mesmo."
- **Alternativas descartadas:** spec escrita para uma pessoa desenvolvedora; spec presa a uma única ferramenta.

## D6. Formato das telas
- **Data:** 2026-11-19
- **Decisão:** as telas saem como wireframes em texto. No máximo uma tela de referência visual, para mostrar como ficaria. O foco é especificar o sistema, não o visual; o usuário conecta a spec ao design system que tiver depois.
- **Motivo:** "o wireframe em texto já está bom e, no máximo, uma referência de uma tela de como ficaria visualmente, mas o foco não é ser visual, é fazer a especificação para um sistema. Depois ele pode conectar isso com o design system."
- **Alternativas descartadas:** prévia em HTML de todas as telas.
- **Discordância:** a sugestão era wireframe em texto mais prévia em HTML de cada tela; o usuário preferiu manter o foco na especificação.
