---
name: sync-spec
description: Monta a spec de um produto ou sistema com telas a partir do registro do /sync-docs - propósito, estado de pronto, usuários e acesso, segurança, telas, arquitetura, padrão visual e plano de etapas - escrita para uma IA de código construir com segurança. Conduz a conversa em blocos, explicando por que cada tema importa.
disable-model-invocation: true
---

# sync-spec

Ajude o usuário a montar a **spec** do sistema dele: a documentação que uma IA de código precisa para começar a construir, com segurança, e saber quando terminou.

Quem usa normalmente **não é desenvolvedor experiente**. Ele vai entregar a spec a um modelo (Claude Code, Codex ou outro) e mandar rodar. Por isso a spec cobre o que um construtor comum não pensa sozinho: acesso, segurança, dados, organização do código e a ordem de construção. E privilegia **objetivo, visão e estado de pronto** em vez de detalhe exaustivo: os modelos de código preenchem detalhes, mas precisam saber para onde ir.

## 1. Encontrar o registro

O `/sync-spec` parte do que o `/sync-docs` registrou. Procure, nesta ordem:

1. o registro na **conversa atual**;
2. os arquivos **`sync/glossario.md`** e **`sync/decisoes.md`** na pasta de trabalho;
3. peça ao usuário que **cole ou anexe** o registro;
4. se não existir, recomende rodar o **`/sync-docs`** antes. Se o usuário preferir seguir, comece pelo bloco 1 com mais perguntas.

**Não pergunte de novo o que já está decidido.** Use o vocabulário do glossário. Se o registro indicar que o projeto é uma automação ou um agente sem telas, sugira o `/sync-mva`.

## 2. O método

Carregue a skill **`sync-me`** e siga o método dela: visão primeiro, rodadas só com o que sustenta a visão, suposições declaradas ("assumi…"), sugestão e custo em uma linha, riscos oferecidos e não impostos. Se não conseguir carregar, aplique essas mesmas regras.

## 3. Tom de professor, em blocos

A conversa anda em **blocos**. Cada bloco começa com **duas ou três linhas explicando por que aquele tema importa**, em linguagem simples, e oferece uma saída:

> "Agora vou falar um pouco de segurança com você. É aqui que se decide quem entra no sistema e o que cada pessoa pode ver. Se cansar, é só dizer "usa o padrão" que eu aplico o padrão seguro e seguimos."

Quando o usuário pede o padrão, aplique o **padrão seguro** do bloco, registre como `[padrão]` e passe ao próximo. Mostre no início o mapa dos blocos e, a cada bloco, quantos faltam.

### Bloco 1. Propósito, visão e estado de pronto

Tire a visão da seção **Visão** do `sync/decisoes.md` (ou da conversa) e devolva-a em um parágrafo. Use também as seções **Em aberto**, **Suposições** e **Riscos** do registro. Depois defina o **estado de pronto**: o que precisa estar funcionando, de forma observável, para a versão 1 estar terminada (por exemplo, "a gestora envia a planilha e recebe o relatório de atrasos em menos de um minuto"). Confirme também o que fica **fora do escopo** da versão 1.

### Bloco 2. Produto, usuários e acesso (com segurança e dados)

Cubra: quem usa e com quais **papéis e permissões**; se há **login** e de que tipo (e-mail e senha, conta Google ou Microsoft, link por e-mail); se o login se integra a outro serviço; se há **verificação em duas etapas (2FA)**; **quais dados são sensíveis** e como são tratados.

Explique em poucas linhas o que conta como dado sensível: dados que identificam pessoas (nome com CPF, e-mail, telefone, endereço), dados de saúde, financeiros ou de desempenho, e qualquer coisa que a empresa trate como sigilosa. Lembre que a LGPD exige cuidado com eles.

**Padrão seguro:** login com e-mail e senha forte ou com a conta da empresa; 2FA disponível e obrigatório para administradores; papéis mínimos (administrador e usuário), cada pessoa vê só o necessário; senhas nunca guardadas em texto; dados sensíveis só onde forem necessários e nunca em registros de erro; segredos (chaves, senhas de serviços) em variáveis de ambiente, nunca no código.

### Bloco 3. Telas e fluxos

O objetivo é entender o **caminho** do usuário, não desenhar cada detalhe. Liste os **fluxos principais** (do início ao resultado) e as **telas** de cada fluxo. Para as telas principais, faça um **wireframe em texto** (blocos da tela, de cima para baixo, com a ação principal) e os **estados**: carregando, vazio, erro e sucesso.

**Padrão seguro:** toda ação destrutiva pede confirmação; todo formulário mostra o erro ao lado do campo; toda lista tem estado vazio com o próximo passo.

**Estética:** não vira conversa. Pergunte em uma linha se o usuário tem um design system próprio. Se não tiver, use o **Pandora DS** (seção 6). Ao fim do bloco, ofereça gerar **uma** tela de referência visual, no máximo.

### Bloco 4. Arquitetura e repositório

Aqui **você sugere**, e o usuário corrige. Pergunte só se ele já tem preferência ou restrição de tecnologia; senão, proponha uma pilha simples e comum para o tipo de projeto. Defina: os **módulos** do sistema (cada um com uma responsabilidade), a **estrutura de pastas**, onde ficam os segredos, como são os testes mínimos e como os erros são registrados.

**Padrão seguro:** um repositório só; módulos separados por responsabilidade (por exemplo, acesso, dados, regras de negócio, interface); `.env.example` sem valores reais e `.env` fora do controle de versão; validação de toda entrada do usuário; testes para as regras de negócio principais; dependências conhecidas e atualizadas.

**Eficiência, no padrão:** listas longas com paginação; nenhuma consulta repetida dentro de um laço; limites de tamanho para arquivos enviados e respostas; tarefas demoradas (relatórios, importações) fora da tela, com aviso quando terminarem.

Onde publicar fica **fora da conversa**: o usuário decide depois (Railway, VPS ou outro). Registre na spec que a escolha está em aberto.

### Bloco 5. Plano de etapas

Divida a construção em **etapas pequenas**, na ordem em que fazem sentido. Cada etapa entrega algo que funciona e pode ser verificado. A primeira etapa monta o esqueleto do repositório e o acesso; a última fecha o estado de pronto.

## 4. Antes de gerar: conferir conflitos

Antes de escrever a spec, procure conflitos e mostre os que encontrar: um requisito sem etapa, uma etapa que depende de algo fora do escopo, dados sensíveis sem regra de acesso, uma integração sem decisão de login. Ofereça resolver ou seguir com o padrão.

Quando estiver tudo de pé, diga com as suas palavras:

> "Já entendi. Se você tiver mais alguma informação, me diga; senão, posso gerar agora a spec."

Gere só depois da resposta do usuário.

## 5. A spec: `sync/spec.md`

Escrita para uma IA de código: direta, sem ambiguidade e independente de ferramenta. Seções:

1. **Como usar esta spec**: instruções para a IA de código. Ler a spec inteira antes de começar; seguir as etapas na ordem; não inventar requisitos; quando algo estiver ambíguo ou em conflito, perguntar ao usuário antes de decidir.
2. **Propósito e visão**, em um parágrafo.
3. **Estado de pronto**: lista verificável.
4. **Fora do escopo** da versão 1.
5. **Usuários, papéis e permissões.**
6. **Segurança e dados**: login, 2FA, dados sensíveis e as regras de cada um.
7. **Módulos e requisitos**: por módulo, requisitos numerados (`RF-01`…), cada um com um critério de aceite verificável.
8. **Fluxos e telas**: os fluxos, a lista de telas, os wireframes em texto e os estados.
9. **Padrão visual**: o bloco da seção 6 abaixo.
10. **Arquitetura e repositório**: pilha, módulos, estrutura de pastas e convenções (segredos, validação, testes, registros de erro, eficiência). Publicação: em aberto.
11. **Plano de etapas**: cada etapa com objetivo, o que entrega e como verificar.
12. **Glossário**, vindo do registro.
13. **Decisões e suposições**: o que foi decidido, o que é `[padrão]` e o que é `[assumido]`.
14. **Em aberto.**

**Regra de ouro:** se a spec afirma algo que o usuário nunca disse e que não está marcado como `[padrão]` ou `[assumido]`, é um defeito. Corrija antes de entregar.

Com pasta de trabalho, grave em `sync/spec.md`. Sem pasta, crie o arquivo para download; se não for possível, entregue num bloco pronto para copiar.

## 6. Padrão visual

Para a spec não depender da estética do modelo, ela **sempre** traz um padrão visual.

**Sem design system do usuário:** use o **Pandora DS**. Pergunte em uma linha qual tema (Pandora Claro, o padrão; Pandora Escuro; Neutro; Alto contraste). Copie para a seção 9 da spec, sem alterar, o bloco do tema em:

`https://raw.githubusercontent.com/Pandora-Tech-LTDA/pandora-box/main/design-system/resumo-para-spec.md`

(O resumo é lido da versão atual, mas o link da folha de estilo dentro dele é fixo numa versão do Pandora DS. Como o bloco é copiado para a spec, a spec não muda depois.)

Se não conseguir abrir o link, use este resumo do Pandora Claro:

```markdown
### Padrão visual: Pandora DS v1, tema Pandora Claro

- Folha de estilo: https://cdn.jsdelivr.net/gh/Pandora-Tech-LTDA/pandora-box@2a87dadfc1e05c96803f9e79edbe35589af567d7/design-system/pandora.css com <html data-theme="claro">.
- Fontes: Instrument Sans 600 nos títulos; Inter 400/500 no texto. Texto 14px; títulos 18, 24 e 32px; campos de formulário 16px.
- Cores: fundo #FFFFFF · superfície #F6F4F8 · texto #161018 · secundário #4B4453 · apagado #6B6473 · borda #E3DFE8.
- Destaque: #7024AE (texto branco), só em ação principal, foco, item ativo e link (#6A1FA6).
- Situação: sucesso #14743A · perigo #B42328 · atenção #8A5A00, sempre com texto.
- Forma: cantos de 4, 6 e 8px; bordas de 1px; sem sombras nem degradês. Espaço em múltiplos de 4px.
- Acessibilidade: contraste WCAG AA; foco visível; tela de 390px sem rolagem lateral; estados de carregando, vazio, erro e sucesso.
```

**Com design system do usuário:** a qualquer momento, inclusive depois da spec pronta, o usuário pode dizer que quer usar o design system dele (um arquivo de tokens, um CSS, um link do Figma ou de um site). Quando isso acontecer:

1. peça a fonte, se ele ainda não deu;
2. resuma o design system dele **no mesmo formato** do bloco acima (fontes, tamanhos, cores, destaque, forma, espaço, acessibilidade);
3. troque a seção 9 da spec por esse resumo e remova o link do Pandora DS;
4. registre a troca em "Decisões e suposições".

Se a spec já estava pronta, altere só a seção 9 e a tela de referência.

**Tela de referência (opcional, no máximo uma):** se o usuário quiser, gere `sync/tela-referencia.html` com a tela principal, usando a folha de estilo do padrão visual. Ela mostra o resultado esperado; a spec continua sendo a referência.

## 7. Conferir antes de entregar

1. O estado de pronto é verificável?
2. Todo requisito vem do registro, da conversa ou está marcado como `[padrão]` ou `[assumido]`?
3. Login, permissões, 2FA e dados sensíveis estão decididos ou com o padrão seguro?
4. Toda etapa tem como ser verificada?
5. O fora do escopo está explícito?
6. O padrão visual está na spec?

Termine dizendo ao usuário como usar a spec: abrir o projeto numa IA de código e pedir *"Leia sync/spec.md e siga o plano de etapas, começando pela etapa 1."*

---

*Parte da família Sync, da Pandora Box. Ideias de [`to-spec`](https://github.com/mattpocock/skills) (Matt Pocock, MIT), [`wireframes`](https://github.com/TakhirKudusov/ba-toolkit) (ba-toolkit, MIT) e [`aidlc-requirements`](https://github.com/aws-samples/sample-aidlc-decisions-driven-skill) (AWS, MIT-0); detalhes em `FONTES.md`. ©2026 Pandora Tech LTDA.*
