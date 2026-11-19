---
name: syncdb
description: Cria bases de dados sintéticas (fictícias, mas realistas) em CSV ou Markdown a partir de um arquivo de exemplo (planilha Excel, CSV, JSON, tabela em PDF ou documento) ou de uma descrição. Use quando o usuário precisar de dados de teste sem expor dados reais, quando chamar /syncdb, ou quando o /sync-mva precisar dos documentos de referência de um MVA.
---

# syncdb

Crie dados **sintéticos**: fictícios, mas com a mesma estrutura, os mesmos formatos e o mesmo comportamento dos dados reais. Eles servem para testar uma automação ou um agente sem expor pessoas, clientes ou números da empresa.

## Regras que não mudam

- **A saída é sempre CSV ou Markdown.** Mesmo que a entrada seja Excel, Word, PDF ou outro formato, nunca gere `.xlsx`, `.docx`, `.pdf` ou similares.
- **Nunca copie valores reais.** Do arquivo de exemplo, use só a estrutura: colunas, tipos, formatos, faixas de valores e relações. Nomes, documentos, e-mails, telefones, endereços e valores são sempre inventados.
- **Se o arquivo de exemplo tiver dados pessoais ou sigilosos**, avise o usuário em uma frase e confirme que nada deles vai para a saída.

## 1. Entender a estrutura

Se houver arquivo de exemplo, leia-o (use execução de código quando disponível) e levante:

- tabelas ou abas, e as colunas de cada uma;
- tipo e formato de cada coluna: texto, número, data e hora, moeda, código, categoria;
- formatos brasileiros quando existirem: datas `dd/mm/aaaa`, vírgula decimal, R$, CPF e CNPJ;
- valores possíveis das categorias e faixas dos números;
- chaves e relações entre tabelas (por exemplo, a matrícula que liga o cadastro à frequência).

Se não houver arquivo, construa essa estrutura com o usuário. Pergunte primeiro **o que a automação precisa saber**, e só depois o formato.

Mostre a estrutura levantada numa tabela curta e confirme com o usuário antes de gerar.

## 2. Combinar o conteúdo

Pergunte, em uma única rodada, só o que faltar (com a sua sugestão para cada item):

1. **Volume:** quantas linhas por tabela.
2. **Período:** de quando a quando, se houver datas.
3. **Casos difíceis:** quais exceções precisam aparecer para o teste valer (por exemplo, faltas, atrasos, registros duplicados, campos vazios, valores fora da faixa).
4. **Proporções:** a frequência aproximada de cada caso (por exemplo, 5% de atrasos).

Se for chamado pelo `/sync-mva` e essas respostas já estiverem no registro, não pergunte de novo.

## 3. Gerar

- Use código para gerar sempre que possível, com uma semente fixa, para que o resultado possa ser refeito.
- Mantenha as relações coerentes: toda chave estrangeira aponta para um registro que existe.
- Inclua os casos difíceis combinados, nas proporções combinadas, e marque-os no dicionário de dados.
- Use nomes e dados plausíveis para o Brasil, claramente fictícios. Documentos como CPF e CNPJ devem ser inventados e não pertencer a ninguém.

## 4. Entregar

Para cada base, entregue:

- **os dados**: `<nome>.csv` (separador `,`, codificação UTF-8, com cabeçalho) ou `<nome>.md` para textos como políticas e procedimentos;
- **o dicionário de dados**: `<nome>-dicionario.md`, com cada coluna (nome, tipo, formato, exemplo), as relações entre tabelas, os casos difíceis incluídos e a semente usada.

Com uma pasta de trabalho, grave os arquivos nela. Quando chamado pelo `/sync-mva`, grave em `documentos/` dentro da pasta do MVA. Sem pasta de trabalho, crie os arquivos para download; se não for possível, entregue-os em blocos de código prontos para copiar, com o nome de cada arquivo.

Termine dizendo em uma frase como os dados podem ser usados e lembrando que, antes de usar dados reais, é preciso verificar as regras de privacidade (LGPD) da organização.

---

*Parte da família Sync, da Pandora Box. Segue o protocolo de contexto sintético da metodologia MVA, ©2026 Pandora Tech LTDA.*
