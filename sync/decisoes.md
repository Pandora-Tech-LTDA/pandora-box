# Decisões

Projeto: skill `/sync-spec`, da família Sync (Pandora Box). As decisões D1 a D4 vieram da conversa anterior e também estão em `skills/sync/DECISOES.md`.

## D1. Nome e papel da skill (nome do arquivo substituído por D18)
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

## D4. Fontes para derivar (substituída por D14)
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

## D7. Papel do design system de referência
- **Data:** 2026-11-19
- **Decisão:** a spec sempre traz um padrão visual do design system de referência (cores, tipografia, contraste, espaçamento), que a IA de código aplica quando o usuário não conecta um design system próprio. Se o usuário tiver um, ele substitui o padrão. Refina a D3.
- **Motivo:** "ele serve para gerar alguma coisa que faça sentido mesmo sem conectar um design system. Senão você vai ter uma especificação que vai depender da estética do próprio modelo. Então a gente pelo menos garante que a leitura vai estar boa, os contrastes vão estar bons, que vai ser uma tela coerente."
- **Alternativas descartadas:** usar o design system só na tela de referência; tirar o design system do `/sync-spec`.

## D8. Plano de implementação em etapas e módulos
- **Data:** 2026-11-19
- **Decisão:** a spec inclui um plano de implementação em etapas e organiza o sistema em módulos. É uma versão 1, sem complexidade desnecessária, mas já com direcionamentos de segurança, eficiência e um repositório coerente.
- **Motivo:** "é bom manter um plano de implementação e etapas e principalmente pensar em módulos; garantir que a especificação já vai trazer direcionamentos que vão trazer uma certa segurança no desenvolvimento. Não é para ser altamente complexo, porque é uma versão 1."
- **Alternativas descartadas:** spec só com requisitos, deixando a ordem de construção para depois.

## D9. Perfil de quem usa a spec e o que ela cobre
- **Data:** 2026-11-19
- **Decisão:** o usuário não é desenvolvedor avançado nem DevOps; ele vai colocar a spec num modelo e mandar rodar. Por isso a spec cobre o que um construtor comum não pensa sozinho: segurança (login, integração do login com outros serviços, 2FA, proteção de dados), eficiência, estrutura do repositório e modularização.
- **Motivo:** "essa pessoa não é um DevOps, não é um desenvolvedor super avançado, ele vai só pegar essa especificação, botar dentro de um modelo e botar para rodar. A gente já tem que ter o cuidado de botar questões de segurança, de eficiência, de garantir um repositório coerente."

## D10. Estilo da conversa: professoral, em blocos com saída para o padrão
- **Data:** 2026-11-19
- **Decisão:** o `/sync-spec` conduz a conversa em blocos temáticos (por exemplo, segurança e estética). Cada bloco começa explicando, em linguagem simples, por que aquele tema importa, e oferece uma saída: se o usuário cansar, a skill usa o padrão seguro do bloco e segue para o próximo.
- **Motivo:** "o processo de construção desse documento tem que ser um processo professoral, quase. Eu vou falar um pouquinho de segurança com você; se você cansar, é só falar para a gente passar de segurança, que a gente usa o padrão."

## D11. Blocos da conversa (versão simplificada)
- **Data:** 2026-11-19
- **Decisão:** a conversa do `/sync-spec` percorre, nesta ordem:
  1. **Propósito, visão e estado de pronto**, tirados do registro do `/sync-me` e do `/sync-docs` (é o bloco central);
  2. **Produto, usuários e níveis de acesso**;
  3. **Telas e fluxos**, só o bastante para entender o caminho do usuário;
  4. **Arquitetura e repositório**, sugeridos pela skill de acordo com a tecnologia;
  5. **Plano de etapas**.
  Publicação e operação ficam fora da conversa: o usuário decide depois onde publicar (Railway, VPS ou outro).
- **Motivo:** "está faltando o propósito mesmo, a visão, o estado de pronto, que você vai tirar do Sync Me e do Sync Docs"; "telas e fluxos, muito mais para entender o caminho"; "publicação e operação ele pode tomar essa decisão quando ele quiser"; "está longo, dá para simplificar".
- **Alternativas descartadas:** a lista de oito blocos, com dados e privacidade, estética e publicação e operação como blocos próprios.
- **Discordância:** a sugestão era a lista de oito blocos; o usuário pediu menos blocos e mais foco em objetivo e visão.

## D12. Nível de detalhe da spec
- **Data:** 2026-11-19
- **Decisão:** a spec privilegia objetivo, visão e estado de pronto em vez de detalhe exaustivo. Os modelos de código atuais preenchem detalhes sozinhos; o que eles precisam é saber para onde ir e quando está pronto.
- **Motivo:** "a gente não precisa de tanto detalhe para novos modelos. A gente precisa muito mais falar de objetivo e visão."

## D13. Segurança, dados e estética dentro dos blocos
- **Data:** 2026-11-19
- **Decisão:** segurança e dados entram no bloco de usuários e acesso (login, integração do login, 2FA, dados sensíveis e LGPD). Estética não vira conversa: a spec aplica o padrão da Pandora (D7), e a skill só pergunta, em uma linha, se o usuário tem um design system próprio. Para compensar o risco de a proteção de dados passar rápido, a skill explica em poucas linhas o que conta como dado sensível, no tom professoral da D10.
- **Motivo:** proposta aceita pelo usuário ("isso"), coerente com a D11 (menos blocos) e com a D9 (segurança como prioridade).

## D14. Fontes: só as ideias, com crédito
- **Data:** 2026-11-19
- **Decisão:** o `/sync-spec` aproveita só as ideias de três fontes, escritas com as nossas palavras: `to-spec` (Matt Pocock, MIT), `wireframes` (ba-toolkit, MIT) e `aidlc-requirements` (AWS, MIT-0). Não copia as skills para `references/`; um `FONTES.md` na pasta da skill lista link, commit e o que foi aproveitado de cada uma. A `prototype` sai da lista. Se algum trecho for copiado literalmente, a licença daquela fonte vai junto.
- **Motivo:** "precisa de todas essas skills juntas? Não dá pra extrair o que precisamos delas?"
- **Alternativas descartadas:** copiar as quatro skills inteiras para `references/`.

## D15. Onde fica o design system de referência
- **Data:** 2026-11-19
- **Decisão:** o design system de referência fica numa pasta `design-system/` da Pandora Box, fora da skill. A spec leva um resumo do tema escolhido (cores, fontes, tamanhos e contraste mínimo), para a IA de código trabalhar mesmo sem abrir o link, e aponta para uma versão fixa do design system. O design system deve ser moderno e simples, pensado para experimentos.
- **Motivo:** "o design system de referência pode estar em um repositório, pra não ficar carregado na skill"; "deixe bem moderno e simples para experimentos".
- **Alternativas descartadas:** design system dentro da skill; spec só com o link, sem resumo.

## D16. Troca pelo design system do usuário
- **Data:** 2026-11-19
- **Decisão:** o `/sync-spec` reconhece quando o usuário quer usar o próprio design system, em qualquer momento da conversa ou depois da spec pronta, e troca o padrão da Pandora por ele: registra a origem, resume os tokens do design system do usuário no lugar do resumo da Pandora e remove o link da Pandora.
- **Motivo:** "a skill precisa entender quando o usuário quiser trocar por um DS dele".

## D17. Versão fixa do design system (commit substituído por D19)
- **Data:** 2026-11-19
- **Decisão:** a v1 do Pandora DS é fixada pelo commit `2a87dadfc1e05c96803f9e79edbe35589af567d7` no link do CDN (`cdn.jsdelivr.net/gh/Pandora-Tech-LTDA/pandora-box@<commit>/design-system/pandora.css`), no lugar da tag `design-system-v1`, que o ambiente de trabalho não conseguiu publicar. Se a tag for criada depois, os links podem passar a usá-la.
- **Motivo:** a spec precisa apontar para uma versão que não muda (D15).

## D18. Nome do arquivo da spec
- **Data:** 2026-11-19
- **Decisão:** a spec é gravada em `sync/spec.md`, não em `sync/requisitos.md` como dizia a D1.
- **Motivo:** o nome acompanha o nome da skill (`/sync-spec`), adotado na implementação; apontado na auditoria.

## D19. Versão fixa do Pandora DS v1.1
- **Data:** 2026-11-19
- **Decisão:** a folha de estilo citada nas specs passa a ser a do Pandora DS v1.1, fixada no commit `3d9b720cdc7b742ddd9068431e2b982aa410cbb1`. O `/sync-spec` lê o resumo dos temas da versão atual (`main`), mas o link da folha de estilo dentro dele é sempre um commit fixo; como o bloco é copiado para a spec, a spec não muda depois. Substitui o commit da D17.
- **Motivo:** a auditoria mostrou que o resumo do commit da D17 ainda apontava para uma tag inexistente, e a v1.1 corrigiu contraste e foco.
