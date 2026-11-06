# RELATÓRIO TÉCNICO
## Cidadão Fácil AI Plus
### Global Solution 2026.2 — FIAP
### CitizenTech — Citizen Assist AI
 
**Equipe:** [NOME DA EQUIPE]
 
**Integrantes:**
- [NOME COMPLETO] — RM [NÚMERO]
- [NOME COMPLETO] — RM [NÚMERO]
 
**Curso:** [NOME DO CURSO]
 
**Turma:** [TURMA]
 
**Ano:** 2026
 
---
 
# 1. INTRODUÇÃO
 
## 1.1 Contextualização
 
O acesso à informação é fundamental para o exercício da cidadania. Entretanto, muitas pessoas enfrentam dificuldades para encontrar orientações confiáveis sobre documentos, serviços de saúde e benefícios sociais.
 
Essas dificuldades podem estar relacionadas à distribuição das informações em diferentes plataformas, à utilização de termos técnicos e à falta de orientações organizadas.
 
Diante desse cenário, foi desenvolvido o **Cidadão Fácil AI Plus**, um protótipo de assistente digital de orientação cidadã.
 
O sistema foi criado utilizando a linguagem Python e tem como finalidade facilitar a consulta a informações organizadas em uma base de conhecimento.
 
## 1.2 Problema identificado
 
O problema central é a dificuldade de localizar e compreender informações relacionadas a serviços públicos.
 
Entre os desafios identificados estão:
 
- Informações distribuídas em diferentes sites.
- Dificuldade para identificar fontes confiáveis.
- Linguagem técnica pouco acessível.
- Falta de organização das orientações.
- Dificuldade para encontrar respostas a perguntas simples.
 
## 1.3 Objetivo geral
 
Desenvolver um assistente digital capaz de receber perguntas, consultar uma base de conhecimento e apresentar orientações claras acompanhadas de referências.
 
## 1.4 Objetivos específicos
 
- Organizar informações em arquivos JSON.
- Implementar algoritmos de busca por relevância.
- Permitir consultas por temas.
- Identificar perguntas ambíguas.
- Tratar entradas inválidas.
- Apresentar fontes e datas de verificação.
- Criar navegação entre assuntos relacionados.
- Avaliar o desempenho por meio de testes.
- Aplicar princípios de privacidade e transparência.
 
---
 
# 2. ARQUITETURA E ORGANIZAÇÃO DO SISTEMA
 
## 2.1 Tecnologias utilizadas
 
O sistema foi desenvolvido em Python 3, utilizando exclusivamente bibliotecas padrão da linguagem.
 
As principais bibliotecas são:
 
| Biblioteca | Finalidade |
|---|---|
| json | Leitura da base de conhecimento |
| os | Localização dos arquivos |
| re | Tratamento de textos |
| time | Medição do tempo de consulta |
| unicodedata | Normalização de caracteres |
 
O projeto funciona por meio de uma interface textual no terminal.
 
Não é necessário utilizar APIs pagas, frameworks web ou modelos externos de inteligência artificial.
 
## 2.2 Estrutura de arquivos
 
```text
cidadao-facil-ai/
├── README.md
├── src/
│   └── sistema.py
├── data/
│   └── base.json
└── docs/
    ├── relatorio.pdf
    ├── link_video.txt
    └── uso_ia.md
```
 
## 2.3 Base de conhecimento
 
A base de conhecimento é armazenada no arquivo `data/base.json`.
 
Ela contém 15 registros distribuídos em três temas:
 
**Documentos:**
- Carteira de Identidade Nacional.
- CPF.
- Título de eleitor.
- Carteira de Trabalho Digital.
- Certidões.
 
**Saúde:**
- Unidade Básica de Saúde.
- Cartão Nacional de Saúde.
- Vacinação.
- Agendamento de consultas.
- Atendimento de urgência.
 
**Benefícios sociais:**
- Cadastro Único.
- CRAS.
- Bolsa Família.
- BPC.
- Tarifa Social de Energia Elétrica.
 
Cada registro contém identificador, tema, pergunta, palavras-chave, orientação, fonte, data de verificação e assuntos relacionados.
 
As orientações devem ser conferidas em páginas oficiais específicas antes da entrega.
 
## 2.4 Estruturas de dados
 
### Listas
 
Utilizadas para armazenar os registros, resultados de busca, testes e histórico de consultas.
 
### Dicionários
 
Utilizados para representar as orientações e acessar informações por identificador.
 
### Conjuntos
 
Utilizados para comparar palavras presentes nas perguntas e nos registros.
 
### Grafo simples
 
Representado pelas conexões entre orientações por meio do campo `relacionados`.
 
Essa estrutura permite navegar entre diferentes assuntos.
 
---
 
# 3. ALGORITMOS E LÓGICA DO ASSISTENTE
 
## 3.1 Funcionamento geral
 
O sistema segue as seguintes etapas:
 
1. Carrega a base de conhecimento.
2. Valida os registros.
3. Apresenta o menu principal.
4. Recebe a pergunta do usuário.
5. Normaliza o texto.
6. Busca orientações relacionadas.
7. Calcula a pontuação de relevância.
8. Seleciona a melhor correspondência.
9. Apresenta a resposta e a fonte.
10. Sugere assuntos relacionados.
 
## 3.2 Normalização de texto
 
A normalização permite comparar perguntas com pequenas diferenças de escrita.
 
Por exemplo:
 
**Entrada:**
 
"Como tirar minha IDENTIDADE?"
 
**Texto normalizado:**
 
"como tirar minha identidade"
 
O algoritmo converte letras para minúsculas, remove acentos e elimina caracteres especiais.
 
## 3.3 Busca por relevância
 
O sistema utiliza um algoritmo baseado na comparação de palavras.
 
A pontuação considera:
 
- Palavras correspondentes à pergunta cadastrada.
- Correspondências completas com palavras-chave.
- Correspondências parciais com palavras-chave.
 
As correspondências completas recebem maior peso.
 
Os registros são ordenados pela pontuação obtida.
 
## 3.4 Tratamento de ambiguidades
 
Quando duas ou mais orientações possuem a mesma pontuação máxima, o sistema apresenta as opções para que o usuário escolha.
 
Isso evita selecionar automaticamente uma resposta quando existem múltiplas possibilidades.
 
## 3.5 Tratamento de erros
 
O sistema considera três situações principais:
 
**Entrada vazia:**
 
Solicita que o usuário digite uma pergunta válida.
 
**Pergunta desconhecida:**
 
Informa que não encontrou orientação suficiente na base.
 
**Consulta ambígua:**
 
Apresenta alternativas para esclarecimento.
 
## 3.6 Modelos de resposta
 
Foram definidos dois modelos de apresentação.
 
### Modelo A — Direto
 
Apresenta apenas a orientação e a fonte.
 
### Modelo B — Estruturado
 
Apresenta:
 
- Tema.
- Pergunta.
- Orientação.
- Fonte.
- Data de verificação.
- Aviso de limitação.
 
O Modelo B foi escolhido como padrão por oferecer mais contexto e transparência.
 
Essa escolha deverá ser avaliada durante os testes de usabilidade.
 
---
 
# 4. TESTES E INDICADORES DE DESEMPENHO
 
## 4.1 Metodologia
 
Para avaliar o funcionamento do sistema, foi planejado um conjunto de 12 testes.
 
Os testes verificam se o algoritmo consegue localizar orientações e tratar situações não previstas.
 
## 4.2 Perguntas de teste
 
| Nº | Consulta | Resultado esperado |
|---|---|---|
| 1 | Como tirar identidade? | DOC001 |
| 2 | Consultar CPF | DOC002 |
| 3 | Tirar título de eleitor | DOC003 |
| 4 | Carteira de trabalho digital | DOC004 |
| 5 | Segunda via de certidão | DOC005 |
| 6 | Encontrar UBS | SAU001 |
| 7 | Consultar vacinas | SAU003 |
| 8 | Cadastro Único | BEN001 |
| 9 | Encontrar CRAS | BEN002 |
| 10 | Entrada vazia | VAZIO |
| 11 | Cadastro | AMBIGUO |
| 12 | Renovar passaporte estrangeiro | SEM_RESPOSTA |
 
## 4.3 Registro dos resultados
 
Preencher após executar os testes reais.
 
| Teste | Obtido | Acerto/Erro | Tempo (s) |
|---|---|---|---|
| 1 | [PREENCHER] | [PREENCHER] | [PREENCHER] |
| 2 | [PREENCHER] | [PREENCHER] | [PREENCHER] |
| 3 | [PREENCHER] | [PREENCHER] | [PREENCHER] |
| 4 | [PREENCHER] | [PREENCHER] | [PREENCHER] |
| 5 | [PREENCHER] | [PREENCHER] | [PREENCHER] |
| 6 | [PREENCHER] | [PREENCHER] | [PREENCHER] |
| 7 | [PREENCHER] | [PREENCHER] | [PREENCHER] |
| 8 | [PREENCHER] | [PREENCHER] | [PREENCHER] |
| 9 | [PREENCHER] | [PREENCHER] | [PREENCHER] |
| 10 | [PREENCHER] | [PREENCHER] | [PREENCHER] |
| 11 | [PREENCHER] | [PREENCHER] | [PREENCHER] |
| 12 | [PREENCHER] | [PREENCHER] | [PREENCHER] |
 
## 4.4 Taxa de acerto
 
A taxa de acerto é calculada por:
 
Taxa = (Quantidade de acertos / Total de testes) × 100
 
**Resultados:**
 
- Total de testes: 12
- Acertos: [PREENCHER]
- Erros: [PREENCHER]
- Taxa de acerto: [PREENCHER]%
 
## 4.5 Tempo médio de consulta
 
O tempo médio é calculado pela soma dos tempos individuais dividida pela quantidade de consultas.
 
Tempo médio = Soma dos tempos / Número de testes
 
**Tempo médio obtido:** [PREENCHER] segundos.
 
A medição utiliza a função `time.perf_counter()`.
 
## 4.6 Interpretação dos resultados
 
[DESCREVER OS RESULTADOS REAIS]
 
Informar:
 
- Quais consultas foram identificadas corretamente.
- Quais perguntas apresentaram dificuldades.
- Se ocorreram ambiguidades inesperadas.
- Se o tempo de consulta foi adequado.
- Quais melhorias foram identificadas.
 
---
 
# 5. USABILIDADE, ÉTICA E LIMITAÇÕES
 
## 5.1 Teste de usabilidade
 
Além dos testes automatizados, deverá ser realizado um teste com pelo menos uma pessoa.
 
### Tarefas propostas
 
1. Encontrar uma orientação sobre identidade.
2. Consultar um serviço de saúde.
3. Navegar entre assuntos relacionados.
4. Realizar uma pergunta desconhecida.
5. Avaliar a clareza da resposta.
 
### Registro da avaliação
 
**Participante:** Usuário de teste anônimo.
 
**Data:** [PREENCHER]
 
**Tarefas concluídas:** [PREENCHER]
 
**Dificuldades observadas:** [PREENCHER]
 
**Comentários do participante:** [PREENCHER]
 
**Conclusão da avaliação:** [PREENCHER]
 
## 5.2 Privacidade
 
O sistema não exige cadastro nem solicita informações pessoais para realizar consultas.
 
O histórico de perguntas permanece apenas na memória durante a execução do programa.
 
Não existe envio automático de dados para serviços externos.
 
## 5.3 Transparência
 
O assistente apresenta fontes e datas de verificação associadas às orientações.
 
Também informa que não representa órgãos públicos.
 
As informações devem ser confirmadas nos canais oficiais.
 
## 5.4 Acessibilidade
 
O sistema utiliza uma interface textual com menus numerados e mensagens em linguagem simples.
 
Essa abordagem reduz a complexidade de navegação.
 
Entretanto, o protótipo ainda não possui recursos específicos de acessibilidade, como leitura de tela integrada.
 
## 5.5 Limitações
 
As principais limitações são:
 
- Base de conhecimento restrita a 15 orientações.
- Dependência de palavras-chave.
- Ausência de compreensão semântica avançada.
- Possibilidade de informações desatualizadas.
- Ausência de integração com órgãos públicos.
- Avaliação inicial com número reduzido de testes.
 
## 5.6 Melhorias propostas
 
**Melhoria 1 — Aprimoramento da busca**
 
Ampliar o conjunto de sinônimos e melhorar o tratamento de perguntas com diferentes formas de escrita.
 
**Melhoria 2 — Ampliação da base**
 
Adicionar novos temas e estabelecer um processo de revisão periódica das fontes.
 
**Melhoria 3 — Acessibilidade**
 
Desenvolver uma interface mais acessível, com suporte a tecnologias assistivas.
 
---
 
# 6. CONCLUSÃO
 
O Cidadão Fácil AI Plus foi concebido como uma solução tecnológica introdutória para facilitar o acesso à informação cidadã.
 
O projeto demonstra a aplicação de conceitos de programação Python, manipulação de arquivos JSON, estruturas de dados, algoritmos de busca e lógica computacional.
 
A organização da base de conhecimento permite localizar orientações sobre documentos, saúde e benefícios sociais.
 
O sistema também contempla mecanismos para identificar ambiguidades, tratar entradas inválidas e apresentar referências.
 
A avaliação por testes automatizados e testes de usabilidade permite identificar pontos fortes e oportunidades de melhoria.
 
O desenvolvimento reforça a 
AI Tools Directory - dealsbe.com
Find useful AI tools for content, code, design, research, and automation.
 
importância da transparência, da privacidade e da validação das informações em aplicações voltadas ao público.
 
Como evolução futura, pretende-se ampliar a base de conhecimento, aperfeiçoar a busca e desenvolver recursos adicionais de acessibilidade.
 
---
 
# 7. REFERÊNCIAS
 
## Referências técnicas
 
**Python Software Foundation.**
Documentação oficial do Python.
https://docs.python.org/3/
 
**OpenAI.**
ChatGPT — Ferramenta de apoio ao desenvolvimento.
https://chatgpt.com/
 
## Referências institucionais
 
**Governo Federal.**
https://www.gov.br/
 
**Receita Federal.**
https://www.gov.br/receitafederal/pt-br
 
**Tribunal Superior Eleitoral.**
https://www.tse.jus.br/
 
**Ministério da Saúde.**
https://www.gov.br/saude/pt-br
 
**Ministério do Desenvolvimento e Assistência Social.**
https://www.gov.br/mds/pt-br
 
**Instituto Nacional do Seguro Social.**
https://www.gov.br/inss/pt-br
 
**Agência Nacional de Energia Elétrica.**
https://www.gov.br/aneel/pt-br
 
As referências específicas das 15 orientações deverão ser verificadas e documentadas antes da entrega.
 
---
 
**FIAP — Global Solution 2026.2**
 
**Projeto:** Cidadão Fácil AI Plus
 
**Desafio:** CitizenTech — Citizen Assist AI
Python 3.15.2 documentation
The official Python documentation.
