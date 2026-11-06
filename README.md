# 🤖 Cidadão Fácil AI Plus
## Global Solution 2026.2 — FIAP
### CitizenTech | Citizen Assist AI
 
**Nome da equipe:** [NOME DA EQUIPE]
 
**Integrantes e RMs:**
- [Nome completo] — RM [Número]
- [Nome completo] — RM [Número]
 
---
 
## 📌 1. Sobre o Projeto
 
O **Cidadão Fácil AI Plus** é um assistente digital de orientação cidadã desenvolvido em Python para a Global Solution do segundo semestre de 2026 da FIAP.
 
O projeto busca facilitar o acesso a informações confiáveis sobre documentos, serviços de saúde e benefícios sociais.
 
Muitos cidadãos enfrentam dificuldades para encontrar informações oficiais, compreender procedimentos e identificar os canais adequados para solicitar serviços públicos.
 
Nossa solução organiza orientações em uma base de conhecimento estruturada e permite que os usuários façam perguntas em linguagem natural.
 
O sistema utiliza algoritmos de busca por relevância para localizar informações e apresentar respostas acompanhadas de suas fontes.
 
**Importante:** o Cidadão Fácil AI Plus é um protótipo acadêmico e não representa nenhum órgão público.
 
---
 
## 🎯 2. Objetivos
 
### Objetivo geral
 
Desenvolver um assistente digital capaz de consultar uma base de conhecimento, identificar orientações relacionadas às perguntas dos usuários e apresentar respostas claras, acessíveis e fundamentadas.
 
### Objetivos específicos
 
- Facilitar o acesso a informações cidadãs.
- Organizar orientações verificadas em arquivos JSON.
- Implementar algoritmos de busca por relevância.
- Permitir consultas por perguntas ou categorias.
- Identificar perguntas ambíguas.
- Tratar entradas inválidas e consultas desconhecidas.
- Apresentar referências e datas de verificação.
- Implementar navegação entre assuntos relacionados.
- Comparar diferentes modelos de resposta.
- Avaliar o desempenho por meio de testes automatizados.
- Respeitar princípios de privacidade e responsabilidade digital.
 
---
 
## 👥 3. Público-Alvo
 
O sistema foi desenvolvido para pessoas que precisam de orientações introdutórias sobre serviços públicos.
 
Entre os possíveis beneficiados estão:
 
- Cidadãos com dúvidas sobre documentação.
- Pessoas que procuram serviços públicos de saúde.
- Famílias interessadas em programas sociais.
- Usuários com pouca familiaridade com plataformas digitais.
- Pessoas que desejam localizar fontes oficiais de informação.
 
---
 
## 🧠 4. Funcionalidades
 
### 4.1 Busca inteligente por relevância
 
O assistente permite que o usuário escreva perguntas sem precisar utilizar exatamente os termos cadastrados.
 
Exemplo:
 
**Pergunta:**
"Como tirar minha identidade?"
 
**Resultado esperado:**
Orientação sobre a emissão da Carteira de Identidade Nacional (CIN).
 
O algoritmo compara as palavras da consulta com as perguntas e palavras-chave da base.
 
### 4.2 Consulta por temas
 
O sistema disponibiliza três categorias principais:
 
1. Documentos
2. Saúde
3. Benefícios sociais
 
O usuário pode selecionar uma categoria para restringir sua pesquisa.
 
### 4.3 Tratamento de ambiguidades
 
Quando duas ou mais orientações recebem a mesma pontuação máxima, o assistente solicita que o usuário escolha a opção desejada.
 
Isso evita selecionar arbitrariamente uma resposta.
 
### 4.4 Navegação entre assuntos relacionados
 
Cada orientação pode possuir conexões com outros registros.
 
Exemplo:
 
Carteira de Identidade Nacional
→ CPF
→ Carteira de Trabalho Digital
 
Essas conexões permitem continuar a navegação sem iniciar uma nova pesquisa.
 
### 4.5 Histórico de consultas
 
O sistema registra temporariamente as perguntas realizadas durante a execução.
 
O histórico contém:
- Pergunta realizada.
- Resultado da consulta.
- Tempo de busca.
 
O histórico permanece apenas na memória e é encerrado junto com o programa.
 
### 4.6 Fontes e transparência
 
Cada orientação apresenta:
- Tema.
- Pergunta relacionada.
- Resposta resumida.
- Referência institucional.
- Data de verificação.
- Aviso sobre limitações.
 
As fontes específicas e as datas reais devem ser conferidas antes da entrega.
 
### 4.7 Testes automatizados
 
O sistema possui 12 cenários de teste para avaliar o algoritmo.
 
São analisados:
- Consultas diretas.
- Perguntas reformuladas.
- Entradas vazias.
- Consultas ambíguas.
- Perguntas fora da base.
 
### 4.8 Comparação de modelos de resposta
 
O assistente implementa dois formatos de resposta, permitindo comparar a apresentação das informações.
 
---
 
## 🛠️ 5. Tecnologias Utilizadas
 
**Linguagem:** Python 3
 
**Armazenamento:** JSON
 
**Interface:** Terminal
 
**Bibliotecas padrão utilizadas:**
 
- `json`: leitura da base de conhecimento.
- `os`: manipulação de caminhos de arquivos.
- `re`: tratamento de textos.
- `time`: medição de desempenho.
- `unicodedata`: normalização de caracteres.
 
O projeto não depende de APIs pagas, frameworks web ou bibliotecas externas de inteligência artificial.
 
---
 
## 📁 6. Estrutura do Projeto
 
```text
cidadao-facil-ai/
│
├── README.md
│
├── src/
│   └── sistema.py
│
├── data/
│   └── base.json
│
└── docs/
    ├── relatorio.pdf
    ├── link_video.txt
    └── uso_ia.md
```
 
### Descrição dos arquivos
 
**README.md**
 
Documentação do projeto, funcionamento, tecnologias e resultados.
 
**src/sistema.py**
 
Código principal do assistente digital.
 
**data/base.json**
 
Base de conhecimento com 15 orientações organizadas por temas.
 
**docs/relatorio.pdf**
 
Relatório técnico com explicações sobre desenvolvimento, algoritmos, testes e resultados.
 
**docs/link_video.txt**
 
Link do vídeo de apresentação publicado no YouTube.
 
**docs/uso_ia.md**
 
Registro do uso de inteligência artificial durante o desenvolvimento.
 
---
 
## 🗂️ 7. Base de Conhecimento
 
A base de conhecimento está armazenada em `data/base.json`.
 
Ela contém 15 orientações distribuídas em três categorias.
 
### Documentos
- Carteira de Identidade Nacional.
- CPF.
- Título de eleitor.
- Carteira de Trabalho Digital.
- Segunda via de certidões.
 
### Saúde
- Unidade Básica de Saúde.
- Cartão Nacional de Saúde.
- Histórico de vacinação.
- Agendamento de consultas.
- Atendimento de urgência.
 
### Benefícios sociais
- Cadastro Único.
- CRAS.
- Bolsa Família.
- Benefício de Prestação Continuada.
- Tarifa Social de Energia Elétrica.
 
### Estrutura de um registro
 
```json
{
  "id": "DOC001",
  "tema": "Documentos",
  "pergunta": "Como emitir a Carteira de Identidade Nacional?",
  "palavras_chave": [
    "identidade",
    "cin",
    "rg"
  ],
  "orientacao": "Consulte o órgão de identificação do seu estado para verificar os procedimentos de emissão.",
  "fonte": "https://www.gov.br/pt-br",
  "data_verificacao": "PENDENTE",
  "relacionados": [
    "DOC002",
    "DOC003"
  ]
}
```
 
O campo `fonte` deverá conter a página oficial específica utilizada para verificar a orientação.
 
O campo `data_verificacao` deverá registrar a data real da consulta.
 
---
 
## 🧩 8. Estruturas de Dados
 
### Listas
 
Utilizadas para armazenar registros da base, resultados de buscas, perguntas de teste e histórico de consultas.
 
### Dicionários
 
Utilizados para representar cada orientação e permitir o acesso aos dados por meio de chaves.
 
Exemplo:
 
```python
indice = {
    item["id"]: item
    for item in base
}
```
 
### Conjuntos
 
Utilizados para comparar palavras das perguntas e identificar termos em comum.
 
### Grafo simples
 
Representado pelos identificadores armazenados no campo `relacionados`.
 
Cada orientação funciona como um nó, enquanto as conexões permitem navegar entre assuntos.
 
---
 
## 🔎 9. Algoritmo de Busca
 
O sistema utiliza uma estratégia de busca baseada em pontuação de relevância.
 
### Etapas
 
1. Receber a pergunta.
2. Converter o texto para letras minúsculas.
3. Remover acentos e caracteres especiais.
4. Remover palavras pouco relevantes.
5. Comparar os termos com os registros.
6. Calcular a pontuação.
7. Ordenar os resultados.
8. Selecionar a melhor correspondência.
 
### Pontuação
 
A pontuação considera:
 
- Correspondência com palavras da pergunta cadastrada.
- Correspondência completa com palavras-chave.
- Correspondência parcial com palavras-chave.
 
Uma correspondência completa com palavra-chave recebe maior peso.
 
### Tratamento de resultados
 
**Correspondência única:** apresenta a orientação.
 
**Empate na maior pontuação:** solicita esclarecimento.
 
**Pontuação insuficiente:** informa que não encontrou resposta confiável.
 
O algoritmo é baseado em regras e não utiliza um modelo generativo de linguagem.
 
---
 
## 💬 10. Estratégias de Prompts e Respostas
 
Foram definidos dois modelos de instrução de resposta.
 
### Modelo A — Resposta direta
 
**Instrução:**
 
"Apresente a orientação resumida encontrada na base e informe a fonte utilizada. Não acrescente informações externas."
 
**Formato:**
 
```text
Orientação:
[Resposta]
 
Fonte:
[Referência]
```
 
### Modelo B — Resposta estruturada
 
**Instrução:**
 
"Atue como um assistente introdutório de orientação cidadã. Apresente o tema, a pergunta relacionada, a orientação resumida, a fonte e a data de verificação. Informe que o sistema não representa um órgão público e recomende confirmar informações atualizadas."
 
**Formato:**
 
```text
CIDADÃO FÁCIL AI
 
Tema:
[Categoria]
 
Pergunta:
[Consulta]
 
Orientação:
[Resposta]
 
Fonte:
[Referência]
 
Data de verificação:
[Data]
 
Aviso:
Confirme as informações nos canais oficiais.
```
 
### Comparação
 
O Modelo A apresenta respostas mais curtas.
 
O Modelo B fornece mais contexto, transparência e avisos.
 
Por esses motivos, o Modelo B foi selecionado como padrão do protótipo.
 
A avaliação de facilidade de compreensão deverá ser complementada com um teste de usabilidade.
 
---
 
## ⚙️ 11. Como Executar
 
### Requisitos
 
- Python 3 instalado.
- Visual Studio Code ou outro editor.
- Arquivos do projeto organizados nas pastas corretas.
 
### Passo 1
 
Baixe ou clone o repositório.
 
### Passo 2
 
Abra a pasta principal no terminal.
 
### Passo 3
 
Execute:
 
```bash
python src/sistema.py
```
 
### Passo 4
 
Escolha uma opção no menu:
 
```text
=============================================
CIDADÃO FÁCIL AI PLUS
Assistente de orientação cidadã
=============================================
 
1 - Fazer pergunta
2 - Consultar por tema
3 - Listar orientações
4 - Histórico da sessão
5 - Executar testes automáticos
6 - Comparar modelos de resposta
0 - Sair
```
 
---
 
## 💻 12. Exemplo de Funcionamento
 
### Entrada
 
```text
Digite sua pergunta:
Como tirar minha identidade?
```
 
### Saída esperada
 
```text
CIDADÃO FÁCIL AI - ORIENTAÇÃO
 
Tema: Documentos
 
Pergunta:
Como emitir a Carteira de Identidade Nacional?
 
Orientação:
Consulte o órgão de identificação do seu
estado para verificar os procedimentos
necessários para emissão da CIN.
 
Fonte:
[Link da página oficial verificada]
 
Data de verificação:
[Data real]
 
AVISO:
Este assistente não representa um órgão público.
Confirme informações e requisitos na fonte oficial.
```
 
### Entrada inválida
 
```text
Digite sua pergunta:
 
Digite uma pergunta válida.
```
 
### Pergunta desconhecida
 
```text
Digite sua pergunta:
Como renovar passaporte estrangeiro?
 
Não encontrei informação suficiente na base.
Tente outra pergunta ou escolha um tema.
```
 
---
 
## 🧪 13. Plano de Testes
 
O projeto possui 12 testes automatizados.
 
| Nº | Pergunta | Resultado esperado |
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
 
### Indicadores
 
**Taxa de acerto:**
 
```text
Taxa = (Acertos / Total de testes) × 100
```
 
**Tempo médio:**
 
```text
Tempo médio = Soma dos tempos / Total de consultas
```
 
O tempo é medido utilizando `time.perf_counter()`.
 
### Resultados reais
 
- Total de testes: 12
- Acertos: [PREENCHER]
- Erros: [PREENCHER]
- Taxa de acerto: [PREENCHER]%
- Tempo médio: [PREENCHER] segundos
 
Os valores deverão ser preenchidos após a execução dos testes.
 
### Teste de usabilidade
 
Realizar um teste com pelo menos um usuário.
 
Tarefas sugeridas:
 
1. Encontrar informações sobre a CIN.
2. Consultar orientações sobre saúde.
3. Navegar entre assuntos relacionados.
4. Testar uma pergunta desconhecida.
5. Avaliar a clareza das respostas.
 
**Resultados observados:** [PREENCHER]
 
**Dificuldades identificadas:** [PREENCHER]
 
**Melhorias sugeridas:** [PREENCHER]
 
---
 
## 🔒 14. Privacidade, Ética e Acessibilidade
 
O projeto segue princípios de responsabilidade digital.
 
### Privacidade
 
- Não exige cadastro.
- Não solicita CPF, endereço ou documentos pessoais.
- Não envia consultas para APIs externas.
- Mantém o histórico apenas durante a execução.
 
### Transparência
 
- Identifica fontes institucionais.
- Exibe datas de verificação.
- Informa limitações.
- Não se apresenta como serviço oficial.
 
### Acessibilidade
 
- Utiliza linguagem simples.
- Oferece navegação por menu.
- Apresenta mensagens compreensíveis.
- Permite consultas sem comandos complexos.
 
---
 
## ⚠️ 15. Limitações
 
O sistema possui algumas limitações:
 
1. A busca depende das palavras cadastradas.
2. Perguntas muito diferentes podem não ser reconhecidas.
3. A base possui apenas 15 orientações.
4. As informações podem mudar com o tempo.
5. Não existe integração em tempo real com órgãos públicos.
6. O sistema não substitui atendimento especializado.
7. A avaliação inicial possui um conjunto limitado de testes.
 
Quando não encontra informação suficiente, o assistente informa sua limitação em vez de inventar uma resposta.
 
---
 
## 🚀 16. Melhorias Futuras
 
Entre as possibilidades de evolução estão:
 
- Ampliar a base de conhecimento.
- Implementar mais sinônimos.
- Melhorar o algoritmo de relevância.
- Desenvolver uma interface gráfica acessível.
- Criar suporte a diferentes idiomas.
- Adicionar recursos de leitura de texto.
- Implementar revisão periódica das fontes.
- Expandir os testes de desempenho e usabilidade.
 
---
 
## 🤖 17. Uso de Inteligência Artificial
 
O ChatGPT foi utilizado como ferramenta de apoio durante o desenvolvimento.
 
As atividades apoiadas incluem:
 
- Planejamento do projeto.
- Organização das funcionalidades.
- Estruturação do código.
- Sugestão de algoritmos.
- Elaboração de modelos de resposta.
- Planejamento de testes.
- Revisão da documentação.
 
O sistema desenvolvido não depende de uma API de inteligência artificial generativa.
 
As sugestões produzidas com apoio de IA devem ser revisadas e validadas pela equipe.
 
O registro detalhado está disponível em:
 
`docs/uso_ia.md`
 
---
 
## 🎥 18. Vídeo de Apresentação
 
**Link do vídeo:**
 
[INSERIR LINK DO YOUTUBE]
 
O vídeo deverá apresentar o problema, o funcionamento do sistema, os algoritmos, os testes e as principais decisões técnicas.
 
---
 
## 📚 19. Referências Institucionais
 
Portais de referência para verificação das orientações:
 
- Governo Federal: https://www.gov.br/
- Receita Federal: https://www.gov.br/receitafederal/pt-br
- Tribunal Superior Eleitoral: https://www.tse.jus.br/
- Ministério da Saúde: https://www.gov.br/saude/pt-br
- Ministério do Desenvolvimento Social: https://www.gov.br/mds/pt-br
- Instituto Nacional do Seguro Social: https://www.gov.br/inss/pt-br
- Agência Nacional de Energia Elétrica: https://www.gov.br/aneel/pt-br
 
**Observação:** esses endereços são portais institucionais. Cada orientação do arquivo JSON deverá conter uma página específica que sustente seu conteúdo e uma data real de verificação.
 
---
 
## 🏁 20. Conclusão
 
O Cidadão Fácil AI Plus demonstra como a programação pode contribuir para facilitar o acesso à informação cidadã.
 
A solução utiliza Python, estruturas de dados, algoritmos de busca, manipulação de arquivos e regras computacionais para organizar orientações e responder perguntas.
 
O projeto também valoriza transparência, privacidade, acessibilidade e avaliação objetiva.
 
Por meio do desenvolvimento, a equipe aplica conhecimentos das fases 1 a 6 do curso, com ênfase nos conteúdos de manipulação de dados, algoritmos, estratégias de resposta e testes.
 
O protótipo representa uma aplicação introdutória de tecnologia voltada às necessidades reais das pessoas.
 
---
 
**FIAP — Global Solution 2026.2**
 
**Projeto:** Cidadão Fácil AI Plus
 
**Desafio:** CitizenTech — Citizen Assist AI