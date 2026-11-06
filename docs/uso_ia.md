# 🤖 Registro de Uso de Inteligência Artificial
 
## Global Solution 2026.2 — FIAP
### Projeto: Cidadão Fácil AI Plus
### Desafio: CitizenTech — Citizen Assist AI
 
**Equipe:** [NOME DA EQUIPE]
 
**Integrantes e RMs:**
- [Nome completo] — RM [Número]
- [Nome completo] — RM [Número]
 
---
 
## 1. Introdução
 
Durante o desenvolvimento do projeto Cidadão Fácil AI Plus, a equipe utilizou ferramentas de Inteligência Artificial como apoio ao planejamento, à programação e à documentação.
 
A principal ferramenta utilizada foi o ChatGPT, desenvolvido pela OpenAI.
 
O uso da IA teve como objetivo auxiliar na organização das ideias, na interpretação dos requisitos da Global Solution e na construção de uma solução tecnológica voltada à orientação cidadã.
 
A Inteligência Artificial foi utilizada como ferramenta de apoio ao desenvolvimento, e não como substituta da análise crítica e da validação realizada pela equipe.
 
---
 
## 2. Ferramenta de IA Utilizada
 
**Ferramenta:** ChatGPT
 
**Desenvolvedor:** OpenAI
 
**Site:** https://chatgpt.com/
 
**Finalidade:** Apoio ao desenvolvimento de software, planejamento, documentação e elaboração de testes.
 
O protótipo Cidadão Fácil AI Plus não depende de APIs externas de inteligência artificial para funcionar.
 
Seu mecanismo de busca utiliza algoritmos implementados em Python, com comparação de palavras-chave e pontuação de relevância.
 
---
 
## 3. Aplicações da IA no Projeto
 
### 3.1 Planejamento e interpretação do desafio
 
O ChatGPT auxiliou na interpretação dos requisitos técnicos apresentados pela FIAP.
 
Foram analisados:
 
- Objetivos do projeto.
- Funcionalidades obrigatórias.
- Estruturas de dados necessárias.
- Requisitos de navegação.
- Tratamento de erros.
- Critérios de avaliação.
- Organização dos entregáveis.
 
A partir dessa análise, foi proposta a criação de um assistente digital voltado à orientação sobre documentos, saúde e benefícios sociais.
 
### 3.2 Organização da arquitetura
 
A IA auxiliou na definição da estrutura de arquivos:
 
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
 
Essa organização separa o código, os dados e a documentação, facilitando a manutenção do sistema.
 
### 3.3 Desenvolvimento do código Python
 
O ChatGPT foi utilizado para sugerir a estrutura inicial do código Python.
 
As sugestões incluíram:
 
- Leitura de arquivos JSON.
- Validação de registros.
- Normalização de textos.
- Busca por relevância.
- Identificação de ambiguidades.
- Tratamento de entradas inválidas.
- Organização do menu.
- Navegação entre assuntos relacionados.
- Histórico de consultas.
- Testes automatizados.
 
O código gerado com apoio de IA deverá ser revisado, executado e validado pela equipe antes da entrega.
 
### 3.4 Construção da base de conhecimento
 
A IA auxiliou na seleção dos temas e na elaboração inicial de orientações.
 
Foram definidos três temas principais:
 
**Documentos**
- Carteira de Identidade Nacional.
- CPF.
- Título de eleitor.
- Carteira de Trabalho Digital.
- Certidões.
 
**Saúde**
- Unidade Básica de Saúde.
- Cartão Nacional de Saúde.
- Vacinação.
- Agendamento de consultas.
- Atendimento de urgência.
 
**Benefícios sociais**
- Cadastro Único.
- CRAS.
- Bolsa Família.
- BPC.
- Tarifa Social de Energia Elétrica.
 
As orientações sugeridas pela IA não devem ser consideradas verificadas automaticamente.
 
Cada registro deverá ser conferido em uma fonte oficial específica, com o endereço da página consultada e a data real de verificação.
 
---
 
## 4. Estratégias de Prompts
 
Durante o desenvolvimento, foram definidos dois modelos de instrução para a apresentação das respostas.
 
### Modelo A — Resposta direta
 
**Prompt de referência:**
 
> Atue como um assistente de orientação cidadã. Utilize exclusivamente as informações presentes na base de conhecimento. Apresente uma resposta curta, objetiva e acompanhada da fonte consultada. Não invente informações.
 
**Formato esperado:**
 
```text
Orientação:
[Resposta encontrada]
 
Fonte:
[Referência consultada]
```
 
**Características:**
 
- Respostas curtas.
- Linguagem objetiva.
- Apresentação da fonte.
- Menor quantidade de informações complementares.
 
### Modelo B — Resposta estruturada
 
**Prompt de referência:**
 
> Atue como um assistente digital introdutório de orientação cidadã. Utilize apenas informações verificadas na base de conhecimento. Apresente o tema, a pergunta relacionada, a orientação resumida, a fonte e a data de verificação. Informe que o sistema não representa um órgão público. Quando não houver informação suficiente, não invente respostas e recomende a consulta aos canais oficiais.
 
**Formato esperado:**
 
```text
CIDADÃO FÁCIL AI PLUS
 
Tema:
[Categoria]
 
Pergunta:
[Pergunta relacionada]
 
Orientação:
[Resposta encontrada]
 
Fonte:
[Referência consultada]
 
Data de verificação:
[Data]
 
Aviso:
Este assistente não representa
um órgão público.
 
Confirme as informações nos
canais oficiais.
```
 
**Características:**
 
- Respostas organizadas.
- Identificação do assunto.
- Apresentação de referências.
- Data de verificação.
- Avisos de limitação.
- Maior transparência.
 
---
 
## 5. Comparação dos Modelos
 
| Critério | Modelo A | Modelo B |
|---|---|---|
| Resposta resumida | Sim | Sim |
| Fonte consultada | Sim | Sim |
| Identificação do tema | Não | Sim |
| Data de verificação | Não | Sim |
| Aviso de limitação | Não | Sim |
| Organização detalhada | Básica | Completa |
 
### Modelo selecionado
 
O Modelo B foi selecionado como formato padrão do protótipo.
 
A escolha foi baseada na presença de informações adicionais que ajudam o usuário a compreender a origem e os limites da orientação.
 
Entretanto, a maior clareza percebida deverá ser confirmada por meio de testes com usuários.
 
**Observação:** os modelos representam instruções e formatos implementados por regras Python. O sistema não executa esses prompts em um modelo generativo durante as consultas.
 
---
 
## 6. Validação Crítica das Sugestões de IA
 
As sugestões produzidas pelo ChatGPT devem passar por procedimentos de validação antes da entrega final.
 
### 6.1 Validação do código
 
A equipe deverá verificar:
 
- Se o código executa sem erros.
- Se os arquivos JSON são carregados corretamente.
- Se a busca retorna orientações adequadas.
- Se perguntas vazias são tratadas.
- Se consultas ambíguas são identificadas.
- Se perguntas desconhecidas recebem avisos.
- Se os indicadores são calculados corretamente.
 
### 6.2 Validação das informações
 
Cada orientação deverá ser confrontada com uma fonte institucional identificável.
 
A validação deverá considerar:
 
- Confiabilidade da fonte.
- Correspondência entre fonte e orientação.
- Atualização da informação.
- Clareza do texto.
- Ausência de instruções inventadas.
 
### 6.3 Validação dos testes
 
O sistema possui 12 cenários de teste planejados.
 
Os resultados deverão ser obtidos por meio da execução real do programa.
 
**Resultados da validação:**
 
- Testes executados: [PREENCHER]
- Testes corretos: [PREENCHER]
- Testes incorretos: [PREENCHER]
- Taxa de acerto: [PREENCHER]
- Tempo médio de consulta: [PREENCHER]
 
Esses campos devem ser preenchidos somente após a execução dos testes.
 
---
 
## 7. Limitações da Inteligência Artificial
 
Durante o desenvolvimento, foram consideradas limitações importantes das ferramentas de IA.
 
### 7.1 Possibilidade de informações incorretas
 
Ferramentas generativas podem produzir informações imprecisas ou desatualizadas.
 
Por esse motivo, as orientações precisam ser verificadas em fontes confiáveis.
 
### 7.2 Dependência do contexto
 
A qualidade das sugestões da IA depende das instruções fornecidas e das informações disponíveis.
 
### 7.3 Limitações da busca implementada
 
O assistente utiliza palavras-chave e pontuação de relevância.
 
Ele não possui compreensão semântica equivalente à de modelos avançados de linguagem.
 
### 7.4 Ausência de integração oficial
 
O sistema não está integrado aos bancos de dados de órgãos públicos.
 
Portanto, não realiza consultas cadastrais nem confirma automaticamente requisitos de serviços.
 
---
 
## 8. Ética, Privacidade e Responsabilidade
 
O projeto foi planejado considerando princípios de responsabilidade digital.
 
### Privacidade
 
O assistente não exige cadastro, CPF, endereço ou informações pessoais para realizar consultas.
 
O histórico é mantido temporariamente na memória durante a execução.
 
### Transparência
 
O sistema informa as fontes de referência e esclarece que não representa um órgão público.
 
### Confiabilidade
 
Quando não encontra uma orientação adequada, o assistente informa sua limitação.
 
### Responsabilidade humana
 
A equipe permanece responsável por revisar o código, validar as orientações e interpretar os resultados dos testes.
 
---
 
## 9. Benefícios do Uso de IA
 
O apoio do ChatGPT contribuiu para:
 
- Organizar os requisitos do desafio.
- Planejar a arquitetura do sistema.
- Estruturar o código Python.
- Propor funcionalidades adicionais.
- Definir modelos de resposta.
- Elaborar cenários de teste.
- Organizar a documentação técnica.
 
A utilização da IA também permitiu discutir a importância da validação humana, da transparência e do uso responsável da tecnologia.
 
---
 
## 10. Conclusão
 
A Inteligência Artificial foi utilizada como ferramenta de apoio ao desenvolvimento do Cidadão Fácil AI Plus.
 
O ChatGPT contribuiu principalmente para o planejamento, a estruturação do código, a definição de estratégias de resposta e a elaboração inicial da documentação.
 
O protótipo utiliza algoritmos próprios em Python para consultar uma base de conhecimento organizada, sem depender de modelos generativos durante sua execução.
 
O projeto demonstra que ferramentas de IA podem auxiliar no processo de desenvolvimento de software, desde que suas sugestões sejam compreendidas, revisadas e validadas criticamente.
 
A responsabilidade pela qualidade, confiabilidade e apresentação final da solução permanece com a equipe.
 
---
 
## 11. Referências
 
**OpenAI — ChatGPT**
 
https://chatgpt.com/
 
**Documentação oficial do Python**
 
https://docs.python.org/3/
 
**Portal de Serviços do Governo Federal**
 
https://www.gov.br/
 
**FIAP — Global Solution 2026.2**
 
Material acadêmico do desafio CitizenTech — Citizen Assist AI, disponibilizado pela instituição.
 
---
 
**FIAP — Global Solution 2026.2**
 
**Projeto:** Cidadão Fácil AI Plus
 
**Documento:** Registro de Uso de Inteligência Artificial