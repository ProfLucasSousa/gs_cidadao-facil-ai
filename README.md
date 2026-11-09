# Cidadão Fácil AI Plus

Global Solution 2026.2 — FIAP | CitizenTech — Citizen Assist AI

**Equipe:** Cidadão Fácil AI Plus.

| Integrante | RM |
|---|---|
| Lucas Sousa | 573029 |
| Dayse Borges de Sousa | 573036 |

## Vídeo e repositório

- [Vídeo de apresentação no YouTube](https://youtu.be/4-hekDBazhM).
- [Repositório do projeto no GitHub](https://github.com/ProfLucasSousa/gs_cidadao-facil-ai).

## Problema e público beneficiado

Informações sobre serviços públicos estão distribuídas em diferentes canais e podem ser difíceis de compreender. Este protótipo organiza orientações introdutórias para cidadãos que buscam documentos, serviços de saúde e benefícios sociais, inclusive pessoas com pouca familiaridade digital.

O sistema é acadêmico, não representa órgãos públicos, não realiza solicitações e não confirma direitos individuais. As orientações devem ser confirmadas nas fontes oficiais.

## Como executar

Requer Python 3.10 ou superior e somente a biblioteca padrão. Na raiz do repositório:

```bash
python src/sistema.py
```

O menu permite perguntar, filtrar por tema, listar registros, consultar o histórico da sessão, executar testes e comparar modelos. Digite `0` para sair. Após uma resposta, escolha assuntos relacionados quantas vezes desejar; pressione Enter para voltar.

Para repetir as avaliações, sem dependências externas:

```bash
python src/sistema.py --testes --comparar-modelos --usabilidade --regressoes
```

As avaliações mostram os resultados no terminal e não criam arquivos auxiliares. O relatório PDF contém o registro da execução de referência. Os testes e o roteiro estão incorporados ao código principal.

## Arquivos da entrega

```text
PROJECT.md                  Requisitos do trabalho
README.md                   Documentação e instruções de execução
src/sistema.py              Assistente e procedimentos de avaliação
data/base.json              Base com 15 orientações e fontes
docs/relatorio.pdf          Relatório, fontes, testes e roteiro de tarefas
docs/uso_ia.md              Registro de uso de IA e validação crítica
docs/link_video.txt         Endereço completo do vídeo de apresentação
```

Os registros de avaliação e a conferência documental das fontes foram incorporados ao relatório PDF e às evidências detalhadas deste README.

## Temas e base de conhecimento

A base possui cinco orientações de Documentos (CIN, CPF, título, CTPS Digital e certidões), cinco de Saúde (UBS, CNS, vacinação, consultas e urgência) e cinco de Benefícios (Cadastro Único, CRAS, Bolsa Família, BPC e Tarifa Social).

Cada registro exige `id`, `tema`, `pergunta`, `palavras_chave`, `orientacao`, `fonte`, `data_verificacao` e `relacionados`. O carregador valida tipos, conteúdo obrigatório, palavras-chave, IDs únicos, referências entre registros, URL HTTPS e data ISO válida que não esteja no futuro. Arquivo ausente, vazio, JSON inválido e inconsistências são tratados com mensagem e encerramento controlado.

A verificação documental das 15 referências foi registrada em 09/11/2026 em [relatório PDF, seção de fontes](docs/relatorio.pdf), incluindo a limitação de acesso direto ao CNJ e o alcance municipal das referências de UBS. Novos registros e correções podem ser feitos no JSON sem alterar as regras centrais.

## Estruturas de dados e navegação

Listas guardam registros, resultados, cenários e histórico. Dicionários representam orientações e o índice de IDs. Conjuntos comparam termos. O campo `relacionados` forma um grafo simples de assuntos; o tema de cada nó organiza as categorias. Por exemplo: CIN → CPF → Carteira de Trabalho Digital. A navegação é iterativa e permite continuar ou voltar sem crescer a pilha de chamadas.

## Estratégia de busca e regras de resposta

1. Um identificador exato, como `DOC001`, recupera o registro dentro do tema selecionado.
2. O texto é convertido para minúsculas, sem acentos ou pontuação; palavras curtas e pouco relevantes são removidas. O sinônimo limitado `cadastral` → `cadastro` aproxima as duas formas.
3. Cada termo em comum com a pergunta cadastrada vale 2 pontos. Cada palavra-chave integralmente contida na consulta vale 5; uma correspondência parcial soma os termos em comum.
4. Pontuações de pelo menos 2 são ordenadas de forma decrescente. Empates no primeiro lugar pedem esclarecimento. Uma correspondência única apresenta o registro; nenhuma correspondência informa o limite e lista os temas disponíveis.

A pontuação é uma heurística lexical, sem compreensão semântica. Consultas fora do escopo que compartilhem palavras da base ainda podem produzir uma correspondência indevida; confirmar a pergunta associada e a fonte é necessário. O sistema não gera instruções externas à base.

Entradas vazias recebem uma mensagem específica. Opções inexistentes no menu, tema, desambiguação e navegação relacionada são rejeitadas. A opção de temas restringe a consulta à categoria escolhida.

## Modelos de instrução de resposta

Estes são modelos internos de instrução para apresentar as orientações da base.

**Modelo A — direto:** apresentar somente a orientação cadastrada e sua fonte, sem acrescentar instruções externas.

**Modelo B — estruturado:** apresentar tema, pergunta associada, orientação, fonte, data de verificação e aviso para confirmar as informações nos canais oficiais; esclarecer que o assistente não representa um órgão público.

Na ausência de orientação, os dois modelos preservam o estado de limitação. O Modelo B é o padrão.

Os dois modelos foram executados nas 22 perguntas do plano. Nas 17 consultas com orientação localizada, ambos mantiveram o mesmo conteúdo e a mesma fonte; o Modelo B também apresentou tema, pergunta, data e aviso de informação não oficial. Os critérios estruturais passaram em 17/17 respostas localizadas. Nas demais consultas, ambos preservaram o estado de limitação, sem fabricar uma orientação.

O Modelo A usa em média 359 caracteres e o Modelo B, 600. O Modelo B foi escolhido por tornar a origem e os limites explícitos. Essa comparação avalia consistência e transparência; não demonstra preferência ou compreensão de pessoas. Os critérios, os resultados por pergunta e exemplos completos dos dois formatos estão no [relatório PDF](docs/relatorio.pdf).

## Exemplos de consulta

| Entrada | Comportamento |
|---|---|
| Como tirar minha identidade? | DOC001: indica a lista oficial de órgãos emissores da CIN e recomenda conferir agendamento e documentos. |
| Consultar CPF | DOC002: indica o comprovante de situação cadastral da Receita Federal. |
| Onde vejo as vacinas que tomei? | SAU003: orienta consultar o Meu SUS Digital e procurar a unidade responsável por registros ausentes. |
| cadastro | Solicita escolha entre situação cadastral do CPF e Cadastro Único. |
| entrada vazia | Solicita uma pergunta válida. |
| renovar passaporte estrangeiro | Informa ausência de orientação e apresenta os temas disponíveis. |

As respostas incluem as fontes específicas da [base](data/base.json). Exemplo de referência para a CIN: [Governo Digital](https://www.gov.br/governodigital/pt-br/identidade/identificacao-do-cidadao-e-carteira-de-identidade-nacional/duvidas-frequentes-sobre-a-cin-campanha).

## Plano de testes, indicadores e resultados

São 22 perguntas com diretas, reformulações, código, questões externas, entrada vazia e ambiguidade. Os resultados individuais, a orientação esperada, a resposta obtida e a duração estão em [relatório PDF, registro dos testes](docs/relatorio.pdf).

Execução: 2026-11-09T12:04:06.156144-03:00. Ambiente: Windows, Python 3.14.0.

- Consultas: 22.
- Acertos: 22.
- Erros: 0.
- Taxa de acerto: 100.00%.
- Tempo médio de consulta: 0.000538 segundos.

Taxa = acertos / total × 100. Tempo médio = soma dos tempos / total.
O tempo mede apenas `diagnosticar`, sem leitura inicial do JSON, espera por digitação ou impressão. A entrada vazia é incluída no conjunto e normalmente tem duração muito pequena.


O conjunto obteve os resultados esperados após corrigir a ambiguidade de “cadastro”. O índice representa seleção de registro/estado, sem comprovar a qualidade de toda consulta possível. A amostra é pequena, conhecida durante o desenvolvimento e sem medição estatística de desempenho. A interpretação completa está em [relatório PDF](docs/relatorio.pdf).

A suíte adicional possui oito métodos de teste para arquivos ausentes ou inválidos, dados inconsistentes, filtro de tema, menus, navegação e consistência dos modelos. A avaliação por roteiro de tarefas está em [relatório PDF, roteiro de tarefas](docs/relatorio.pdf); sua execução é automatizada e não equivale à avaliação com pessoas.

### Registro resumido das consultas

| Nº | Consulta | Esperado | Obtido | Resultado | Tempo (s) |
|---|---|---|---|---|---|
| 1 | como tirar identidade | DOC001 | DOC001 | Acerto | 0.000701 |
| 2 | consultar cpf | DOC002 | DOC002 | Acerto | 0.000509 |
| 3 | tirar titulo eleitor | DOC003 | DOC003 | Acerto | 0.000514 |
| 4 | carteira trabalho digital | DOC004 | DOC004 | Acerto | 0.000539 |
| 5 | segunda via certidao | DOC005 | DOC005 | Acerto | 0.000493 |
| 6 | encontrar ubs | SAU001 | SAU001 | Acerto | 0.000479 |
| 7 | consultar vacinas | SAU003 | SAU003 | Acerto | 0.000480 |
| 8 | cadastro unico | BEN001 | BEN001 | Acerto | 0.000573 |
| 9 | encontrar cras | BEN002 | BEN002 | Acerto | 0.000462 |
| 10 | (entrada vazia) | VAZIO | VAZIO | Acerto | 0.000001 |
| 11 | cadastro | AMBIGUO | AMBIGUO | Acerto | 0.000465 |
| 12 | renovar passaporte estrangeiro | SEM_RESPOSTA | SEM_RESPOSTA | Acerto | 0.000523 |
| 13 | DOC001 | DOC001 | DOC001 | Acerto | 0.000003 |
| 14 | Como emitir a Carteira de Identidade Nacional? | DOC001 | DOC001 | Acerto | 0.000597 |
| 15 | Onde vejo as vacinas que tomei? | SAU003 | SAU003 | Acerto | 0.000547 |
| 16 | Como acessar meu cartao SUS? | SAU002 | SAU002 | Acerto | 0.000537 |
| 17 | Onde buscar atendimento de urgencia? | SAU005 | SAU005 | Acerto | 0.000555 |
| 18 | Quero informacoes do Bolsa Familia | BEN003 | BEN003 | Acerto | 0.000574 |
| 19 | Onde consultar o BPC? | BEN004 | BEN004 | Acerto | 0.000462 |
| 20 | Como obter desconto energia? | BEN005 | BEN005 | Acerto | 0.002159 |
| 21 | Receita de bolo de cenoura | SEM_RESPOSTA | SEM_RESPOSTA | Acerto | 0.000658 |
| 22 | (entrada vazia) | VAZIO | VAZIO | Acerto | 0.000001 |

O PDF inclui as orientações esperadas e as respostas obtidas, além da comparação dos modelos e do roteiro executado.

## Clareza, acessibilidade e privacidade

A interface usa texto, menus numerados, linguagem simples e mensagens de erro. Não depende de cores ou de cadastro. Recursos de acessibilidade precisam ser validados com leitores de tela e pessoas com necessidades diversas.

Não são solicitados CPF, senha ou endereço. Consultas não são enviadas a serviços externos. O histórico fica apenas na memória e se encerra com o programa. As avaliações usam somente perguntas fixas de teste e exibem resultados no terminal; o relatório entregue contém esses cenários, sem o histórico real de usuários.

## Uso de inteligência artificial

Ferramentas de IA foram utilizadas como suporte ao desenvolvimento, revisão e verificação/validação: análise de requisitos, discussão de alternativas, revisão de código e textos, identificação de inconsistências e apoio aos testes. As conclusões são sustentadas pelos arquivos de avaliação e pelas referências documentadas, com seus limites explícitos. A equipe permanece responsável pela revisão final.

O protótipo usa regras Python e não chama modelos generativos. O registro completo está em [uso_ia.md](docs/uso_ia.md).

## Limitações e melhorias

A busca depende de palavras-chave e de um limiar simples; não interpreta contexto, negações ou intenção com segurança. A base é pequena, os procedimentos locais variam e as informações podem mudar. Os testes não substituem avaliação com cidadãos nem atendimento especializado.

Melhorias propostas: ampliar sinônimos e perguntas inéditas, aumentar e revisar periodicamente a base, testar acessibilidade com tecnologias assistivas e avaliar compreensão com pessoas.

## Conclusão

O protótipo integra Python, arquivos estruturados, busca lexical, grafo de navegação, instruções de resposta e indicadores reproduzíveis para facilitar o acesso introdutório à informação cidadã. As evidências demonstram o comportamento no conjunto avaliado e registram as limitações de fontes, busca e usabilidade.

## Conteúdos mobilizados e impacto social

As fases 1 a 3 apoiam lógica, funções, listas e dicionários. A fase 4 é mobilizada na organização dos dados e no grafo de assuntos; a fase 5, na leitura de JSON, modelos de instrução e saídas estruturadas; a fase 6, na busca, no assistente e nas métricas de avaliação. Nem todos os conteúdos de cada fase são necessários ao escopo do protótipo.

O impacto esperado é reduzir o esforço para localizar canais oficiais e compreender orientações iniciais. Trata-se de uma contribuição potencial: não foram medidos benefícios sociais em campo. Acesso a terminal e alfabetização digital limitam o alcance; atendimento humano e outros canais continuam necessários.

## Evidências detalhadas

Os registros abaixo foram incorporados dos arquivos de avaliação. A execução de referência ocorreu em 09/11/2026, antes da consolidação dos procedimentos em `src/sistema.py`; após a incorporação, as 22 consultas, seis tarefas e oito testes de regressão foram reexecutados com sucesso. Os tempos abaixo pertencem à execução de referência e variam a cada execução.

### Fontes consultadas e validação documental

Consulta documental realizada em 09/11/2026. A data registra a consulta à referência e não garante atualização futura. Não foram feitas solicitações de serviços nem informados dados pessoais.

| Registro | Referência | Orientação conferida |
|---|---|---|
| DOC001 | [Como emitir a Carteira de Identidade Nacional?](https://www.gov.br/governodigital/pt-br/identidade/identificacao-do-cidadao-e-carteira-de-identidade-nacional/duvidas-frequentes-sobre-a-cin-campanha) | Consulte a lista de institutos de identificação dos estados e do Distrito Federal na página oficial da CIN. Confira no órgão do seu estado o agendamento e os documentos exigidos para a emissão. |
| DOC002 | [Como consultar a situação cadastral do CPF?](https://solucoes.receita.fazenda.gov.br/Servicos/cpf/ConsultaSituacao/ConsultaPublica.asp) | Acesse o serviço de Comprovante de Situação Cadastral no CPF da Receita Federal. Informe os dados solicitados somente no site oficial. O comprovante informa a situação cadastral e não comprova a situação financeira ou fiscal da pessoa. |
| DOC003 | [Como tirar o título de eleitor?](https://www.tse.jus.br/servicos-eleitorais/titulo-eleitoral/autoatendimento-eleitoral) | Consulte o Autoatendimento Eleitoral do TSE para solicitar o primeiro título e verificar a documentação. Confirme a disponibilidade do serviço, os prazos eleitorais e eventuais etapas presenciais com a zona eleitoral. |
| DOC004 | [Como acessar a Carteira de Trabalho Digital?](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/trabalhador/carteira-de-trabalho/perguntas-frequentes-carteira-de-trabalho-digital) | A Carteira de Trabalho Digital pode ser acessada pelo aplicativo ou pela versão web indicada pelo Ministério do Trabalho e Emprego, com autenticação na conta gov.br do próprio interessado. Confira as orientações e os canais de suporte na página oficial. |
| DOC005 | [Como solicitar uma segunda via de certidão?](https://www.cnj.jus.br/2a-via-de-certidoes-de-nascimento-e-de-obito-podem-ser-solicitadas-via-internet/) | Para obter segunda via de certidão de nascimento ou de óbito, consulte o cartório responsável ou o Portal do Registro Civil indicado pelo CNJ. Confira os dados necessários, os valores e as formas de entrega antes de solicitar. |
| SAU001 | [Como encontrar uma Unidade Básica de Saúde?](https://prefeitura.sp.gov.br/web/saude/w/unidades-basicas-de-saude-ubs) | Procure a Secretaria Municipal de Saúde para localizar a UBS de referência e confirmar os serviços e horários locais. A página de referência descreve as UBS da cidade de São Paulo; em outros municípios, confirme os canais da prefeitura local. |
| SAU002 | [Como consultar informações do Cartão Nacional de Saúde?](https://www.gov.br/saude/pt-br/composicao/seidigi/meususdigital/perguntas-e-respostas/cidadao/10-onde-encontro-o-numero) | No Meu SUS Digital, acesse Perfil e selecione o ícone do cartão para consultar as informações do Cartão Nacional de Saúde. Ao virar o cartão na tela, é possível visualizar o número do CNS e o QR Code de identificação. |
| SAU003 | [Como consultar meu histórico de vacinação?](https://www.gov.br/saude/pt-br/assuntos/noticias/2026/outubro/quer-consultar-suas-vacinas-saiba-como-acessar-a-carteira-de-vacinacao-pelo-meu-sus-digital/) | Acesse o Meu SUS Digital com sua conta gov.br e consulte a área de vacinas. Os registros dependem do envio pelos serviços de saúde. Se uma dose não aparecer ou estiver incorreta, procure a unidade onde ela foi aplicada ou a Secretaria Municipal de Saúde. |
| SAU004 | [Como agendar uma consulta na rede pública de saúde?](https://prefeitura.sp.gov.br/web/saude/w/unidades-basicas-de-saude-ubs) | Procure sua UBS ou a Secretaria Municipal de Saúde para confirmar como agendar uma consulta na atenção básica. A fonte apresenta serviços e consultas das UBS de São Paulo; os procedimentos e a disponibilidade variam conforme o município. |
| SAU005 | [Onde buscar atendimento de urgência?](https://www.gov.br/saude/pt-br/composicao/saes/samu-192) | Em uma emergência de saúde, ligue 192 para o SAMU e siga as orientações da equipe de regulação. O serviço avalia a situação e orienta o atendimento, com envio de equipe quando necessário. Este assistente não avalia sintomas nem substitui atendimento de emergência. |
| BEN001 | [Como fazer o Cadastro Único?](https://www.gov.br/pt-br/servicos/inscrever-se-no-cadastro-unico-para-programas-sociais-do-governo-federal) | Procure o posto do Cadastro Único no município para consultar os critérios, os documentos e o atendimento de inscrição ou atualização. Se não souber onde ir, busque orientação no CRAS ou no setor responsável pelo Bolsa Família. |
| BEN002 | [Como encontrar um CRAS?](https://www.gov.br/pt-br/servicos/acessar-o-cras-centro-de-referencia-da-assistencia-social) | Consulte a prefeitura ou o localizador indicado na página oficial do serviço para encontrar o CRAS mais próximo. Confirme com a unidade os horários, a necessidade de agendamento e as formas de atendimento. |
| BEN003 | [Como consultar informações sobre o Bolsa Família?](https://www.gov.br/pt-br/servicos/receber-o-bolsa-familia) | Consulte a página oficial do Bolsa Família para conhecer os critérios e as etapas do programa. Mantenha o Cadastro Único atualizado e procure o CRAS ou o setor municipal responsável para orientações. Este assistente não confirma elegibilidade nem garante a concessão do benefício. |
| BEN004 | [Onde consultar informações sobre o BPC?](https://www.gov.br/inss/pt-br/noticias/como-pedir-beneficio-de-prestacao-continuada-bpc) | Consulte os canais oficiais do INSS para conhecer os critérios e o pedido do BPC. O CRAS pode orientar sobre o Cadastro Único e o acesso ao benefício. A concessão depende de análise oficial; este assistente não confirma o direito ao pagamento. |
| BEN005 | [Como consultar a Tarifa Social de Energia Elétrica?](https://www.gov.br/aneel/pt-br/assuntos/tarifas/tarifa-social) | Consulte a página da ANEEL sobre a Tarifa Social e a distribuidora de energia para verificar os critérios e a aplicação do benefício. As regras diferenciam a energia consumida de outras cobranças da fatura; confirme os detalhes nos canais oficiais. |

## Alcance da verificação

- As referências de UBS descrevem São Paulo. Os resumos explicitam esse alcance e orientam confirmar os procedimentos em outros municípios.
- A página do CNJ foi conferida pelo conteúdo indexado na busca; a abertura direta retornou HTTP 403. O resumo limita-se às segundas vias de nascimento e óbito descritas na referência. Recomenda-se nova consulta manual antes da entrega.
- A conferência é documental: não comprova disponibilidade de atendimento, elegibilidade individual ou conclusão de serviços.
- Não foram incluídos critérios numéricos de renda, valores de benefícios ou prazos de concessão.
- Revisar as páginas antes da apresentação e quando houver mudanças nos canais ou nas regras.

### Registro completo das consultas

<details>
<summary>Teste 1: &#x27;como tirar identidade&#x27; — DOC001 — Acerto</summary>

Esperado: **DOC001**. Obtido: **DOC001**. Tempo: **0.000701 s**.

Orientação/estado esperado:

```text
Consulte a lista de institutos de identificação dos estados e do Distrito Federal na página oficial da CIN. Confira no órgão do seu estado o agendamento e os documentos exigidos para a emissão.
```

Resposta obtida na avaliação:

```text
CIDADÃO FÁCIL AI - ORIENTAÇÃO
Tema: Documentos
Pergunta: Como emitir a Carteira de Identidade Nacional?

Orientação:
Consulte a lista de institutos de identificação dos estados e do Distrito Federal na página oficial da CIN. Confira no órgão do seu estado o agendamento e os documentos exigidos para a emissão.

Fonte: https://www.gov.br/governodigital/pt-br/identidade/identificacao-do-cidadao-e-carteira-de-identidade-nacional/duvidas-frequentes-sobre-a-cin-campanha
Data de verificação: 2026-11-09

AVISO:
Este assistente não representa um órgão público.
Confirme informações e requisitos na fonte oficial.
```

</details>

<details>
<summary>Teste 2: &#x27;consultar cpf&#x27; — DOC002 — Acerto</summary>

Esperado: **DOC002**. Obtido: **DOC002**. Tempo: **0.000509 s**.

Orientação/estado esperado:

```text
Acesse o serviço de Comprovante de Situação Cadastral no CPF da Receita Federal. Informe os dados solicitados somente no site oficial. O comprovante informa a situação cadastral e não comprova a situação financeira ou fiscal da pessoa.
```

Resposta obtida na avaliação:

```text
CIDADÃO FÁCIL AI - ORIENTAÇÃO
Tema: Documentos
Pergunta: Como consultar a situação cadastral do CPF?

Orientação:
Acesse o serviço de Comprovante de Situação Cadastral no CPF da Receita Federal. Informe os dados solicitados somente no site oficial. O comprovante informa a situação cadastral e não comprova a situação financeira ou fiscal da pessoa.

Fonte: https://solucoes.receita.fazenda.gov.br/Servicos/cpf/ConsultaSituacao/ConsultaPublica.asp
Data de verificação: 2026-11-09

AVISO:
Este assistente não representa um órgão público.
Confirme informações e requisitos na fonte oficial.
```

</details>

<details>
<summary>Teste 3: &#x27;tirar titulo eleitor&#x27; — DOC003 — Acerto</summary>

Esperado: **DOC003**. Obtido: **DOC003**. Tempo: **0.000514 s**.

Orientação/estado esperado:

```text
Consulte o Autoatendimento Eleitoral do TSE para solicitar o primeiro título e verificar a documentação. Confirme a disponibilidade do serviço, os prazos eleitorais e eventuais etapas presenciais com a zona eleitoral.
```

Resposta obtida na avaliação:

```text
CIDADÃO FÁCIL AI - ORIENTAÇÃO
Tema: Documentos
Pergunta: Como tirar o título de eleitor?

Orientação:
Consulte o Autoatendimento Eleitoral do TSE para solicitar o primeiro título e verificar a documentação. Confirme a disponibilidade do serviço, os prazos eleitorais e eventuais etapas presenciais com a zona eleitoral.

Fonte: https://www.tse.jus.br/servicos-eleitorais/titulo-eleitoral/autoatendimento-eleitoral
Data de verificação: 2026-11-09

AVISO:
Este assistente não representa um órgão público.
Confirme informações e requisitos na fonte oficial.
```

</details>

<details>
<summary>Teste 4: &#x27;carteira trabalho digital&#x27; — DOC004 — Acerto</summary>

Esperado: **DOC004**. Obtido: **DOC004**. Tempo: **0.000539 s**.

Orientação/estado esperado:

```text
A Carteira de Trabalho Digital pode ser acessada pelo aplicativo ou pela versão web indicada pelo Ministério do Trabalho e Emprego, com autenticação na conta gov.br do próprio interessado. Confira as orientações e os canais de suporte na página oficial.
```

Resposta obtida na avaliação:

```text
CIDADÃO FÁCIL AI - ORIENTAÇÃO
Tema: Documentos
Pergunta: Como acessar a Carteira de Trabalho Digital?

Orientação:
A Carteira de Trabalho Digital pode ser acessada pelo aplicativo ou pela versão web indicada pelo Ministério do Trabalho e Emprego, com autenticação na conta gov.br do próprio interessado. Confira as orientações e os canais de suporte na página oficial.

Fonte: https://www.gov.br/trabalho-e-emprego/pt-br/servicos/trabalhador/carteira-de-trabalho/perguntas-frequentes-carteira-de-trabalho-digital
Data de verificação: 2026-11-09

AVISO:
Este assistente não representa um órgão público.
Confirme informações e requisitos na fonte oficial.
```

</details>

<details>
<summary>Teste 5: &#x27;segunda via certidao&#x27; — DOC005 — Acerto</summary>

Esperado: **DOC005**. Obtido: **DOC005**. Tempo: **0.000493 s**.

Orientação/estado esperado:

```text
Para obter segunda via de certidão de nascimento ou de óbito, consulte o cartório responsável ou o Portal do Registro Civil indicado pelo CNJ. Confira os dados necessários, os valores e as formas de entrega antes de solicitar.
```

Resposta obtida na avaliação:

```text
CIDADÃO FÁCIL AI - ORIENTAÇÃO
Tema: Documentos
Pergunta: Como solicitar uma segunda via de certidão?

Orientação:
Para obter segunda via de certidão de nascimento ou de óbito, consulte o cartório responsável ou o Portal do Registro Civil indicado pelo CNJ. Confira os dados necessários, os valores e as formas de entrega antes de solicitar.

Fonte: https://www.cnj.jus.br/2a-via-de-certidoes-de-nascimento-e-de-obito-podem-ser-solicitadas-via-internet/
Data de verificação: 2026-11-09

AVISO:
Este assistente não representa um órgão público.
Confirme informações e requisitos na fonte oficial.
```

</details>

<details>
<summary>Teste 6: &#x27;encontrar ubs&#x27; — SAU001 — Acerto</summary>

Esperado: **SAU001**. Obtido: **SAU001**. Tempo: **0.000479 s**.

Orientação/estado esperado:

```text
Procure a Secretaria Municipal de Saúde para localizar a UBS de referência e confirmar os serviços e horários locais. A página de referência descreve as UBS da cidade de São Paulo; em outros municípios, confirme os canais da prefeitura local.
```

Resposta obtida na avaliação:

```text
CIDADÃO FÁCIL AI - ORIENTAÇÃO
Tema: Saúde
Pergunta: Como encontrar uma Unidade Básica de Saúde?

Orientação:
Procure a Secretaria Municipal de Saúde para localizar a UBS de referência e confirmar os serviços e horários locais. A página de referência descreve as UBS da cidade de São Paulo; em outros municípios, confirme os canais da prefeitura local.

Fonte: https://prefeitura.sp.gov.br/web/saude/w/unidades-basicas-de-saude-ubs
Data de verificação: 2026-11-09

AVISO:
Este assistente não representa um órgão público.
Confirme informações e requisitos na fonte oficial.
```

</details>

<details>
<summary>Teste 7: &#x27;consultar vacinas&#x27; — SAU003 — Acerto</summary>

Esperado: **SAU003**. Obtido: **SAU003**. Tempo: **0.000480 s**.

Orientação/estado esperado:

```text
Acesse o Meu SUS Digital com sua conta gov.br e consulte a área de vacinas. Os registros dependem do envio pelos serviços de saúde. Se uma dose não aparecer ou estiver incorreta, procure a unidade onde ela foi aplicada ou a Secretaria Municipal de Saúde.
```

Resposta obtida na avaliação:

```text
CIDADÃO FÁCIL AI - ORIENTAÇÃO
Tema: Saúde
Pergunta: Como consultar meu histórico de vacinação?

Orientação:
Acesse o Meu SUS Digital com sua conta gov.br e consulte a área de vacinas. Os registros dependem do envio pelos serviços de saúde. Se uma dose não aparecer ou estiver incorreta, procure a unidade onde ela foi aplicada ou a Secretaria Municipal de Saúde.

Fonte: https://www.gov.br/saude/pt-br/assuntos/noticias/2026/outubro/quer-consultar-suas-vacinas-saiba-como-acessar-a-carteira-de-vacinacao-pelo-meu-sus-digital/
Data de verificação: 2026-11-09

AVISO:
Este assistente não representa um órgão público.
Confirme informações e requisitos na fonte oficial.
```

</details>

<details>
<summary>Teste 8: &#x27;cadastro unico&#x27; — BEN001 — Acerto</summary>

Esperado: **BEN001**. Obtido: **BEN001**. Tempo: **0.000573 s**.

Orientação/estado esperado:

```text
Procure o posto do Cadastro Único no município para consultar os critérios, os documentos e o atendimento de inscrição ou atualização. Se não souber onde ir, busque orientação no CRAS ou no setor responsável pelo Bolsa Família.
```

Resposta obtida na avaliação:

```text
CIDADÃO FÁCIL AI - ORIENTAÇÃO
Tema: Benefícios
Pergunta: Como fazer o Cadastro Único?

Orientação:
Procure o posto do Cadastro Único no município para consultar os critérios, os documentos e o atendimento de inscrição ou atualização. Se não souber onde ir, busque orientação no CRAS ou no setor responsável pelo Bolsa Família.

Fonte: https://www.gov.br/pt-br/servicos/inscrever-se-no-cadastro-unico-para-programas-sociais-do-governo-federal
Data de verificação: 2026-11-09

AVISO:
Este assistente não representa um órgão público.
Confirme informações e requisitos na fonte oficial.
```

</details>

<details>
<summary>Teste 9: &#x27;encontrar cras&#x27; — BEN002 — Acerto</summary>

Esperado: **BEN002**. Obtido: **BEN002**. Tempo: **0.000462 s**.

Orientação/estado esperado:

```text
Consulte a prefeitura ou o localizador indicado na página oficial do serviço para encontrar o CRAS mais próximo. Confirme com a unidade os horários, a necessidade de agendamento e as formas de atendimento.
```

Resposta obtida na avaliação:

```text
CIDADÃO FÁCIL AI - ORIENTAÇÃO
Tema: Benefícios
Pergunta: Como encontrar um CRAS?

Orientação:
Consulte a prefeitura ou o localizador indicado na página oficial do serviço para encontrar o CRAS mais próximo. Confirme com a unidade os horários, a necessidade de agendamento e as formas de atendimento.

Fonte: https://www.gov.br/pt-br/servicos/acessar-o-cras-centro-de-referencia-da-assistencia-social
Data de verificação: 2026-11-09

AVISO:
Este assistente não representa um órgão público.
Confirme informações e requisitos na fonte oficial.
```

</details>

<details>
<summary>Teste 10: &#x27;&#x27; — VAZIO — Acerto</summary>

Esperado: **VAZIO**. Obtido: **VAZIO**. Tempo: **0.000001 s**.

Orientação/estado esperado:

```text
VAZIO
```

Resposta obtida na avaliação:

```text
VAZIO
```

</details>

<details>
<summary>Teste 11: &#x27;cadastro&#x27; — AMBIGUO — Acerto</summary>

Esperado: **AMBIGUO**. Obtido: **AMBIGUO**. Tempo: **0.000465 s**.

Orientação/estado esperado:

```text
AMBIGUO
```

Resposta obtida na avaliação:

```text
AMBIGUO
```

</details>

<details>
<summary>Teste 12: &#x27;renovar passaporte estrangeiro&#x27; — SEM_RESPOSTA — Acerto</summary>

Esperado: **SEM_RESPOSTA**. Obtido: **SEM_RESPOSTA**. Tempo: **0.000523 s**.

Orientação/estado esperado:

```text
SEM_RESPOSTA
```

Resposta obtida na avaliação:

```text
SEM_RESPOSTA
```

</details>

<details>
<summary>Teste 13: &#x27;DOC001&#x27; — DOC001 — Acerto</summary>

Esperado: **DOC001**. Obtido: **DOC001**. Tempo: **0.000003 s**.

Orientação/estado esperado:

```text
Consulte a lista de institutos de identificação dos estados e do Distrito Federal na página oficial da CIN. Confira no órgão do seu estado o agendamento e os documentos exigidos para a emissão.
```

Resposta obtida na avaliação:

```text
CIDADÃO FÁCIL AI - ORIENTAÇÃO
Tema: Documentos
Pergunta: Como emitir a Carteira de Identidade Nacional?

Orientação:
Consulte a lista de institutos de identificação dos estados e do Distrito Federal na página oficial da CIN. Confira no órgão do seu estado o agendamento e os documentos exigidos para a emissão.

Fonte: https://www.gov.br/governodigital/pt-br/identidade/identificacao-do-cidadao-e-carteira-de-identidade-nacional/duvidas-frequentes-sobre-a-cin-campanha
Data de verificação: 2026-11-09

AVISO:
Este assistente não representa um órgão público.
Confirme informações e requisitos na fonte oficial.
```

</details>

<details>
<summary>Teste 14: &#x27;Como emitir a Carteira de Identidade Nacional?&#x27; — DOC001 — Acerto</summary>

Esperado: **DOC001**. Obtido: **DOC001**. Tempo: **0.000597 s**.

Orientação/estado esperado:

```text
Consulte a lista de institutos de identificação dos estados e do Distrito Federal na página oficial da CIN. Confira no órgão do seu estado o agendamento e os documentos exigidos para a emissão.
```

Resposta obtida na avaliação:

```text
CIDADÃO FÁCIL AI - ORIENTAÇÃO
Tema: Documentos
Pergunta: Como emitir a Carteira de Identidade Nacional?

Orientação:
Consulte a lista de institutos de identificação dos estados e do Distrito Federal na página oficial da CIN. Confira no órgão do seu estado o agendamento e os documentos exigidos para a emissão.

Fonte: https://www.gov.br/governodigital/pt-br/identidade/identificacao-do-cidadao-e-carteira-de-identidade-nacional/duvidas-frequentes-sobre-a-cin-campanha
Data de verificação: 2026-11-09

AVISO:
Este assistente não representa um órgão público.
Confirme informações e requisitos na fonte oficial.
```

</details>

<details>
<summary>Teste 15: &#x27;Onde vejo as vacinas que tomei?&#x27; — SAU003 — Acerto</summary>

Esperado: **SAU003**. Obtido: **SAU003**. Tempo: **0.000547 s**.

Orientação/estado esperado:

```text
Acesse o Meu SUS Digital com sua conta gov.br e consulte a área de vacinas. Os registros dependem do envio pelos serviços de saúde. Se uma dose não aparecer ou estiver incorreta, procure a unidade onde ela foi aplicada ou a Secretaria Municipal de Saúde.
```

Resposta obtida na avaliação:

```text
CIDADÃO FÁCIL AI - ORIENTAÇÃO
Tema: Saúde
Pergunta: Como consultar meu histórico de vacinação?

Orientação:
Acesse o Meu SUS Digital com sua conta gov.br e consulte a área de vacinas. Os registros dependem do envio pelos serviços de saúde. Se uma dose não aparecer ou estiver incorreta, procure a unidade onde ela foi aplicada ou a Secretaria Municipal de Saúde.

Fonte: https://www.gov.br/saude/pt-br/assuntos/noticias/2026/outubro/quer-consultar-suas-vacinas-saiba-como-acessar-a-carteira-de-vacinacao-pelo-meu-sus-digital/
Data de verificação: 2026-11-09

AVISO:
Este assistente não representa um órgão público.
Confirme informações e requisitos na fonte oficial.
```

</details>

<details>
<summary>Teste 16: &#x27;Como acessar meu cartao SUS?&#x27; — SAU002 — Acerto</summary>

Esperado: **SAU002**. Obtido: **SAU002**. Tempo: **0.000537 s**.

Orientação/estado esperado:

```text
No Meu SUS Digital, acesse Perfil e selecione o ícone do cartão para consultar as informações do Cartão Nacional de Saúde. Ao virar o cartão na tela, é possível visualizar o número do CNS e o QR Code de identificação.
```

Resposta obtida na avaliação:

```text
CIDADÃO FÁCIL AI - ORIENTAÇÃO
Tema: Saúde
Pergunta: Como consultar informações do Cartão Nacional de Saúde?

Orientação:
No Meu SUS Digital, acesse Perfil e selecione o ícone do cartão para consultar as informações do Cartão Nacional de Saúde. Ao virar o cartão na tela, é possível visualizar o número do CNS e o QR Code de identificação.

Fonte: https://www.gov.br/saude/pt-br/composicao/seidigi/meususdigital/perguntas-e-respostas/cidadao/10-onde-encontro-o-numero
Data de verificação: 2026-11-09

AVISO:
Este assistente não representa um órgão público.
Confirme informações e requisitos na fonte oficial.
```

</details>

<details>
<summary>Teste 17: &#x27;Onde buscar atendimento de urgencia?&#x27; — SAU005 — Acerto</summary>

Esperado: **SAU005**. Obtido: **SAU005**. Tempo: **0.000555 s**.

Orientação/estado esperado:

```text
Em uma emergência de saúde, ligue 192 para o SAMU e siga as orientações da equipe de regulação. O serviço avalia a situação e orienta o atendimento, com envio de equipe quando necessário. Este assistente não avalia sintomas nem substitui atendimento de emergência.
```

Resposta obtida na avaliação:

```text
CIDADÃO FÁCIL AI - ORIENTAÇÃO
Tema: Saúde
Pergunta: Onde buscar atendimento de urgência?

Orientação:
Em uma emergência de saúde, ligue 192 para o SAMU e siga as orientações da equipe de regulação. O serviço avalia a situação e orienta o atendimento, com envio de equipe quando necessário. Este assistente não avalia sintomas nem substitui atendimento de emergência.

Fonte: https://www.gov.br/saude/pt-br/composicao/saes/samu-192
Data de verificação: 2026-11-09

AVISO:
Este assistente não representa um órgão público.
Confirme informações e requisitos na fonte oficial.
```

</details>

<details>
<summary>Teste 18: &#x27;Quero informacoes do Bolsa Familia&#x27; — BEN003 — Acerto</summary>

Esperado: **BEN003**. Obtido: **BEN003**. Tempo: **0.000574 s**.

Orientação/estado esperado:

```text
Consulte a página oficial do Bolsa Família para conhecer os critérios e as etapas do programa. Mantenha o Cadastro Único atualizado e procure o CRAS ou o setor municipal responsável para orientações. Este assistente não confirma elegibilidade nem garante a concessão do benefício.
```

Resposta obtida na avaliação:

```text
CIDADÃO FÁCIL AI - ORIENTAÇÃO
Tema: Benefícios
Pergunta: Como consultar informações sobre o Bolsa Família?

Orientação:
Consulte a página oficial do Bolsa Família para conhecer os critérios e as etapas do programa. Mantenha o Cadastro Único atualizado e procure o CRAS ou o setor municipal responsável para orientações. Este assistente não confirma elegibilidade nem garante a concessão do benefício.

Fonte: https://www.gov.br/pt-br/servicos/receber-o-bolsa-familia
Data de verificação: 2026-11-09

AVISO:
Este assistente não representa um órgão público.
Confirme informações e requisitos na fonte oficial.
```

</details>

<details>
<summary>Teste 19: &#x27;Onde consultar o BPC?&#x27; — BEN004 — Acerto</summary>

Esperado: **BEN004**. Obtido: **BEN004**. Tempo: **0.000462 s**.

Orientação/estado esperado:

```text
Consulte os canais oficiais do INSS para conhecer os critérios e o pedido do BPC. O CRAS pode orientar sobre o Cadastro Único e o acesso ao benefício. A concessão depende de análise oficial; este assistente não confirma o direito ao pagamento.
```

Resposta obtida na avaliação:

```text
CIDADÃO FÁCIL AI - ORIENTAÇÃO
Tema: Benefícios
Pergunta: Onde consultar informações sobre o BPC?

Orientação:
Consulte os canais oficiais do INSS para conhecer os critérios e o pedido do BPC. O CRAS pode orientar sobre o Cadastro Único e o acesso ao benefício. A concessão depende de análise oficial; este assistente não confirma o direito ao pagamento.

Fonte: https://www.gov.br/inss/pt-br/noticias/como-pedir-beneficio-de-prestacao-continuada-bpc
Data de verificação: 2026-11-09

AVISO:
Este assistente não representa um órgão público.
Confirme informações e requisitos na fonte oficial.
```

</details>

<details>
<summary>Teste 20: &#x27;Como obter desconto energia?&#x27; — BEN005 — Acerto</summary>

Esperado: **BEN005**. Obtido: **BEN005**. Tempo: **0.002159 s**.

Orientação/estado esperado:

```text
Consulte a página da ANEEL sobre a Tarifa Social e a distribuidora de energia para verificar os critérios e a aplicação do benefício. As regras diferenciam a energia consumida de outras cobranças da fatura; confirme os detalhes nos canais oficiais.
```

Resposta obtida na avaliação:

```text
CIDADÃO FÁCIL AI - ORIENTAÇÃO
Tema: Benefícios
Pergunta: Como consultar a Tarifa Social de Energia Elétrica?

Orientação:
Consulte a página da ANEEL sobre a Tarifa Social e a distribuidora de energia para verificar os critérios e a aplicação do benefício. As regras diferenciam a energia consumida de outras cobranças da fatura; confirme os detalhes nos canais oficiais.

Fonte: https://www.gov.br/aneel/pt-br/assuntos/tarifas/tarifa-social
Data de verificação: 2026-11-09

AVISO:
Este assistente não representa um órgão público.
Confirme informações e requisitos na fonte oficial.
```

</details>

<details>
<summary>Teste 21: &#x27;Receita de bolo de cenoura&#x27; — SEM_RESPOSTA — Acerto</summary>

Esperado: **SEM_RESPOSTA**. Obtido: **SEM_RESPOSTA**. Tempo: **0.000658 s**.

Orientação/estado esperado:

```text
SEM_RESPOSTA
```

Resposta obtida na avaliação:

```text
SEM_RESPOSTA
```

</details>

<details>
<summary>Teste 22: &#x27;   &#x27; — VAZIO — Acerto</summary>

Esperado: **VAZIO**. Obtido: **VAZIO**. Tempo: **0.000001 s**.

Orientação/estado esperado:

```text
VAZIO
```

Resposta obtida na avaliação:

```text
VAZIO
```

</details>

### Comparação completa dos modelos de instrução

Os estados de limitação são diagnósticos compartilhados pelos modelos; os textos de interação podem ser conferidos no roteiro e no código.

<details>
<summary>Comparação 1: &#x27;como tirar identidade&#x27;</summary>

Modelo A:

```text
Orientação:
Consulte a lista de institutos de identificação dos estados e do Distrito Federal na página oficial da CIN. Confira no órgão do seu estado o agendamento e os documentos exigidos para a emissão.
Fonte: https://www.gov.br/governodigital/pt-br/identidade/identificacao-do-cidadao-e-carteira-de-identidade-nacional/duvidas-frequentes-sobre-a-cin-campanha
```

Modelo B:

```text
CIDADÃO FÁCIL AI - ORIENTAÇÃO
Tema: Documentos
Pergunta: Como emitir a Carteira de Identidade Nacional?

Orientação:
Consulte a lista de institutos de identificação dos estados e do Distrito Federal na página oficial da CIN. Confira no órgão do seu estado o agendamento e os documentos exigidos para a emissão.

Fonte: https://www.gov.br/governodigital/pt-br/identidade/identificacao-do-cidadao-e-carteira-de-identidade-nacional/duvidas-frequentes-sobre-a-cin-campanha
Data de verificação: 2026-11-09

AVISO:
Este assistente não representa um órgão público.
Confirme informações e requisitos na fonte oficial.
```

Critérios: mesma_orientacao: sim; fonte_em_ambos: sim; data_em_B: sim; aviso_em_B: sim.

</details>

<details>
<summary>Comparação 2: &#x27;consultar cpf&#x27;</summary>

Modelo A:

```text
Orientação:
Acesse o serviço de Comprovante de Situação Cadastral no CPF da Receita Federal. Informe os dados solicitados somente no site oficial. O comprovante informa a situação cadastral e não comprova a situação financeira ou fiscal da pessoa.
Fonte: https://solucoes.receita.fazenda.gov.br/Servicos/cpf/ConsultaSituacao/ConsultaPublica.asp
```

Modelo B:

```text
CIDADÃO FÁCIL AI - ORIENTAÇÃO
Tema: Documentos
Pergunta: Como consultar a situação cadastral do CPF?

Orientação:
Acesse o serviço de Comprovante de Situação Cadastral no CPF da Receita Federal. Informe os dados solicitados somente no site oficial. O comprovante informa a situação cadastral e não comprova a situação financeira ou fiscal da pessoa.

Fonte: https://solucoes.receita.fazenda.gov.br/Servicos/cpf/ConsultaSituacao/ConsultaPublica.asp
Data de verificação: 2026-11-09

AVISO:
Este assistente não representa um órgão público.
Confirme informações e requisitos na fonte oficial.
```

Critérios: mesma_orientacao: sim; fonte_em_ambos: sim; data_em_B: sim; aviso_em_B: sim.

</details>

<details>
<summary>Comparação 3: &#x27;tirar titulo eleitor&#x27;</summary>

Modelo A:

```text
Orientação:
Consulte o Autoatendimento Eleitoral do TSE para solicitar o primeiro título e verificar a documentação. Confirme a disponibilidade do serviço, os prazos eleitorais e eventuais etapas presenciais com a zona eleitoral.
Fonte: https://www.tse.jus.br/servicos-eleitorais/titulo-eleitoral/autoatendimento-eleitoral
```

Modelo B:

```text
CIDADÃO FÁCIL AI - ORIENTAÇÃO
Tema: Documentos
Pergunta: Como tirar o título de eleitor?

Orientação:
Consulte o Autoatendimento Eleitoral do TSE para solicitar o primeiro título e verificar a documentação. Confirme a disponibilidade do serviço, os prazos eleitorais e eventuais etapas presenciais com a zona eleitoral.

Fonte: https://www.tse.jus.br/servicos-eleitorais/titulo-eleitoral/autoatendimento-eleitoral
Data de verificação: 2026-11-09

AVISO:
Este assistente não representa um órgão público.
Confirme informações e requisitos na fonte oficial.
```

Critérios: mesma_orientacao: sim; fonte_em_ambos: sim; data_em_B: sim; aviso_em_B: sim.

</details>

<details>
<summary>Comparação 4: &#x27;carteira trabalho digital&#x27;</summary>

Modelo A:

```text
Orientação:
A Carteira de Trabalho Digital pode ser acessada pelo aplicativo ou pela versão web indicada pelo Ministério do Trabalho e Emprego, com autenticação na conta gov.br do próprio interessado. Confira as orientações e os canais de suporte na página oficial.
Fonte: https://www.gov.br/trabalho-e-emprego/pt-br/servicos/trabalhador/carteira-de-trabalho/perguntas-frequentes-carteira-de-trabalho-digital
```

Modelo B:

```text
CIDADÃO FÁCIL AI - ORIENTAÇÃO
Tema: Documentos
Pergunta: Como acessar a Carteira de Trabalho Digital?

Orientação:
A Carteira de Trabalho Digital pode ser acessada pelo aplicativo ou pela versão web indicada pelo Ministério do Trabalho e Emprego, com autenticação na conta gov.br do próprio interessado. Confira as orientações e os canais de suporte na página oficial.

Fonte: https://www.gov.br/trabalho-e-emprego/pt-br/servicos/trabalhador/carteira-de-trabalho/perguntas-frequentes-carteira-de-trabalho-digital
Data de verificação: 2026-11-09

AVISO:
Este assistente não representa um órgão público.
Confirme informações e requisitos na fonte oficial.
```

Critérios: mesma_orientacao: sim; fonte_em_ambos: sim; data_em_B: sim; aviso_em_B: sim.

</details>

<details>
<summary>Comparação 5: &#x27;segunda via certidao&#x27;</summary>

Modelo A:

```text
Orientação:
Para obter segunda via de certidão de nascimento ou de óbito, consulte o cartório responsável ou o Portal do Registro Civil indicado pelo CNJ. Confira os dados necessários, os valores e as formas de entrega antes de solicitar.
Fonte: https://www.cnj.jus.br/2a-via-de-certidoes-de-nascimento-e-de-obito-podem-ser-solicitadas-via-internet/
```

Modelo B:

```text
CIDADÃO FÁCIL AI - ORIENTAÇÃO
Tema: Documentos
Pergunta: Como solicitar uma segunda via de certidão?

Orientação:
Para obter segunda via de certidão de nascimento ou de óbito, consulte o cartório responsável ou o Portal do Registro Civil indicado pelo CNJ. Confira os dados necessários, os valores e as formas de entrega antes de solicitar.

Fonte: https://www.cnj.jus.br/2a-via-de-certidoes-de-nascimento-e-de-obito-podem-ser-solicitadas-via-internet/
Data de verificação: 2026-11-09

AVISO:
Este assistente não representa um órgão público.
Confirme informações e requisitos na fonte oficial.
```

Critérios: mesma_orientacao: sim; fonte_em_ambos: sim; data_em_B: sim; aviso_em_B: sim.

</details>

<details>
<summary>Comparação 6: &#x27;encontrar ubs&#x27;</summary>

Modelo A:

```text
Orientação:
Procure a Secretaria Municipal de Saúde para localizar a UBS de referência e confirmar os serviços e horários locais. A página de referência descreve as UBS da cidade de São Paulo; em outros municípios, confirme os canais da prefeitura local.
Fonte: https://prefeitura.sp.gov.br/web/saude/w/unidades-basicas-de-saude-ubs
```

Modelo B:

```text
CIDADÃO FÁCIL AI - ORIENTAÇÃO
Tema: Saúde
Pergunta: Como encontrar uma Unidade Básica de Saúde?

Orientação:
Procure a Secretaria Municipal de Saúde para localizar a UBS de referência e confirmar os serviços e horários locais. A página de referência descreve as UBS da cidade de São Paulo; em outros municípios, confirme os canais da prefeitura local.

Fonte: https://prefeitura.sp.gov.br/web/saude/w/unidades-basicas-de-saude-ubs
Data de verificação: 2026-11-09

AVISO:
Este assistente não representa um órgão público.
Confirme informações e requisitos na fonte oficial.
```

Critérios: mesma_orientacao: sim; fonte_em_ambos: sim; data_em_B: sim; aviso_em_B: sim.

</details>

<details>
<summary>Comparação 7: &#x27;consultar vacinas&#x27;</summary>

Modelo A:

```text
Orientação:
Acesse o Meu SUS Digital com sua conta gov.br e consulte a área de vacinas. Os registros dependem do envio pelos serviços de saúde. Se uma dose não aparecer ou estiver incorreta, procure a unidade onde ela foi aplicada ou a Secretaria Municipal de Saúde.
Fonte: https://www.gov.br/saude/pt-br/assuntos/noticias/2026/outubro/quer-consultar-suas-vacinas-saiba-como-acessar-a-carteira-de-vacinacao-pelo-meu-sus-digital/
```

Modelo B:

```text
CIDADÃO FÁCIL AI - ORIENTAÇÃO
Tema: Saúde
Pergunta: Como consultar meu histórico de vacinação?

Orientação:
Acesse o Meu SUS Digital com sua conta gov.br e consulte a área de vacinas. Os registros dependem do envio pelos serviços de saúde. Se uma dose não aparecer ou estiver incorreta, procure a unidade onde ela foi aplicada ou a Secretaria Municipal de Saúde.

Fonte: https://www.gov.br/saude/pt-br/assuntos/noticias/2026/outubro/quer-consultar-suas-vacinas-saiba-como-acessar-a-carteira-de-vacinacao-pelo-meu-sus-digital/
Data de verificação: 2026-11-09

AVISO:
Este assistente não representa um órgão público.
Confirme informações e requisitos na fonte oficial.
```

Critérios: mesma_orientacao: sim; fonte_em_ambos: sim; data_em_B: sim; aviso_em_B: sim.

</details>

<details>
<summary>Comparação 8: &#x27;cadastro unico&#x27;</summary>

Modelo A:

```text
Orientação:
Procure o posto do Cadastro Único no município para consultar os critérios, os documentos e o atendimento de inscrição ou atualização. Se não souber onde ir, busque orientação no CRAS ou no setor responsável pelo Bolsa Família.
Fonte: https://www.gov.br/pt-br/servicos/inscrever-se-no-cadastro-unico-para-programas-sociais-do-governo-federal
```

Modelo B:

```text
CIDADÃO FÁCIL AI - ORIENTAÇÃO
Tema: Benefícios
Pergunta: Como fazer o Cadastro Único?

Orientação:
Procure o posto do Cadastro Único no município para consultar os critérios, os documentos e o atendimento de inscrição ou atualização. Se não souber onde ir, busque orientação no CRAS ou no setor responsável pelo Bolsa Família.

Fonte: https://www.gov.br/pt-br/servicos/inscrever-se-no-cadastro-unico-para-programas-sociais-do-governo-federal
Data de verificação: 2026-11-09

AVISO:
Este assistente não representa um órgão público.
Confirme informações e requisitos na fonte oficial.
```

Critérios: mesma_orientacao: sim; fonte_em_ambos: sim; data_em_B: sim; aviso_em_B: sim.

</details>

<details>
<summary>Comparação 9: &#x27;encontrar cras&#x27;</summary>

Modelo A:

```text
Orientação:
Consulte a prefeitura ou o localizador indicado na página oficial do serviço para encontrar o CRAS mais próximo. Confirme com a unidade os horários, a necessidade de agendamento e as formas de atendimento.
Fonte: https://www.gov.br/pt-br/servicos/acessar-o-cras-centro-de-referencia-da-assistencia-social
```

Modelo B:

```text
CIDADÃO FÁCIL AI - ORIENTAÇÃO
Tema: Benefícios
Pergunta: Como encontrar um CRAS?

Orientação:
Consulte a prefeitura ou o localizador indicado na página oficial do serviço para encontrar o CRAS mais próximo. Confirme com a unidade os horários, a necessidade de agendamento e as formas de atendimento.

Fonte: https://www.gov.br/pt-br/servicos/acessar-o-cras-centro-de-referencia-da-assistencia-social
Data de verificação: 2026-11-09

AVISO:
Este assistente não representa um órgão público.
Confirme informações e requisitos na fonte oficial.
```

Critérios: mesma_orientacao: sim; fonte_em_ambos: sim; data_em_B: sim; aviso_em_B: sim.

</details>

<details>
<summary>Comparação 10: &#x27;&#x27;</summary>

Modelo A:

```text
VAZIO
```

Modelo B:

```text
VAZIO
```

</details>

<details>
<summary>Comparação 11: &#x27;cadastro&#x27;</summary>

Modelo A:

```text
AMBIGUO
```

Modelo B:

```text
AMBIGUO
```

</details>

<details>
<summary>Comparação 12: &#x27;renovar passaporte estrangeiro&#x27;</summary>

Modelo A:

```text
SEM_RESPOSTA
```

Modelo B:

```text
SEM_RESPOSTA
```

</details>

<details>
<summary>Comparação 13: &#x27;DOC001&#x27;</summary>

Modelo A:

```text
Orientação:
Consulte a lista de institutos de identificação dos estados e do Distrito Federal na página oficial da CIN. Confira no órgão do seu estado o agendamento e os documentos exigidos para a emissão.
Fonte: https://www.gov.br/governodigital/pt-br/identidade/identificacao-do-cidadao-e-carteira-de-identidade-nacional/duvidas-frequentes-sobre-a-cin-campanha
```

Modelo B:

```text
CIDADÃO FÁCIL AI - ORIENTAÇÃO
Tema: Documentos
Pergunta: Como emitir a Carteira de Identidade Nacional?

Orientação:
Consulte a lista de institutos de identificação dos estados e do Distrito Federal na página oficial da CIN. Confira no órgão do seu estado o agendamento e os documentos exigidos para a emissão.

Fonte: https://www.gov.br/governodigital/pt-br/identidade/identificacao-do-cidadao-e-carteira-de-identidade-nacional/duvidas-frequentes-sobre-a-cin-campanha
Data de verificação: 2026-11-09

AVISO:
Este assistente não representa um órgão público.
Confirme informações e requisitos na fonte oficial.
```

Critérios: mesma_orientacao: sim; fonte_em_ambos: sim; data_em_B: sim; aviso_em_B: sim.

</details>

<details>
<summary>Comparação 14: &#x27;Como emitir a Carteira de Identidade Nacional?&#x27;</summary>

Modelo A:

```text
Orientação:
Consulte a lista de institutos de identificação dos estados e do Distrito Federal na página oficial da CIN. Confira no órgão do seu estado o agendamento e os documentos exigidos para a emissão.
Fonte: https://www.gov.br/governodigital/pt-br/identidade/identificacao-do-cidadao-e-carteira-de-identidade-nacional/duvidas-frequentes-sobre-a-cin-campanha
```

Modelo B:

```text
CIDADÃO FÁCIL AI - ORIENTAÇÃO
Tema: Documentos
Pergunta: Como emitir a Carteira de Identidade Nacional?

Orientação:
Consulte a lista de institutos de identificação dos estados e do Distrito Federal na página oficial da CIN. Confira no órgão do seu estado o agendamento e os documentos exigidos para a emissão.

Fonte: https://www.gov.br/governodigital/pt-br/identidade/identificacao-do-cidadao-e-carteira-de-identidade-nacional/duvidas-frequentes-sobre-a-cin-campanha
Data de verificação: 2026-11-09

AVISO:
Este assistente não representa um órgão público.
Confirme informações e requisitos na fonte oficial.
```

Critérios: mesma_orientacao: sim; fonte_em_ambos: sim; data_em_B: sim; aviso_em_B: sim.

</details>

<details>
<summary>Comparação 15: &#x27;Onde vejo as vacinas que tomei?&#x27;</summary>

Modelo A:

```text
Orientação:
Acesse o Meu SUS Digital com sua conta gov.br e consulte a área de vacinas. Os registros dependem do envio pelos serviços de saúde. Se uma dose não aparecer ou estiver incorreta, procure a unidade onde ela foi aplicada ou a Secretaria Municipal de Saúde.
Fonte: https://www.gov.br/saude/pt-br/assuntos/noticias/2026/outubro/quer-consultar-suas-vacinas-saiba-como-acessar-a-carteira-de-vacinacao-pelo-meu-sus-digital/
```

Modelo B:

```text
CIDADÃO FÁCIL AI - ORIENTAÇÃO
Tema: Saúde
Pergunta: Como consultar meu histórico de vacinação?

Orientação:
Acesse o Meu SUS Digital com sua conta gov.br e consulte a área de vacinas. Os registros dependem do envio pelos serviços de saúde. Se uma dose não aparecer ou estiver incorreta, procure a unidade onde ela foi aplicada ou a Secretaria Municipal de Saúde.

Fonte: https://www.gov.br/saude/pt-br/assuntos/noticias/2026/outubro/quer-consultar-suas-vacinas-saiba-como-acessar-a-carteira-de-vacinacao-pelo-meu-sus-digital/
Data de verificação: 2026-11-09

AVISO:
Este assistente não representa um órgão público.
Confirme informações e requisitos na fonte oficial.
```

Critérios: mesma_orientacao: sim; fonte_em_ambos: sim; data_em_B: sim; aviso_em_B: sim.

</details>

<details>
<summary>Comparação 16: &#x27;Como acessar meu cartao SUS?&#x27;</summary>

Modelo A:

```text
Orientação:
No Meu SUS Digital, acesse Perfil e selecione o ícone do cartão para consultar as informações do Cartão Nacional de Saúde. Ao virar o cartão na tela, é possível visualizar o número do CNS e o QR Code de identificação.
Fonte: https://www.gov.br/saude/pt-br/composicao/seidigi/meususdigital/perguntas-e-respostas/cidadao/10-onde-encontro-o-numero
```

Modelo B:

```text
CIDADÃO FÁCIL AI - ORIENTAÇÃO
Tema: Saúde
Pergunta: Como consultar informações do Cartão Nacional de Saúde?

Orientação:
No Meu SUS Digital, acesse Perfil e selecione o ícone do cartão para consultar as informações do Cartão Nacional de Saúde. Ao virar o cartão na tela, é possível visualizar o número do CNS e o QR Code de identificação.

Fonte: https://www.gov.br/saude/pt-br/composicao/seidigi/meususdigital/perguntas-e-respostas/cidadao/10-onde-encontro-o-numero
Data de verificação: 2026-11-09

AVISO:
Este assistente não representa um órgão público.
Confirme informações e requisitos na fonte oficial.
```

Critérios: mesma_orientacao: sim; fonte_em_ambos: sim; data_em_B: sim; aviso_em_B: sim.

</details>

<details>
<summary>Comparação 17: &#x27;Onde buscar atendimento de urgencia?&#x27;</summary>

Modelo A:

```text
Orientação:
Em uma emergência de saúde, ligue 192 para o SAMU e siga as orientações da equipe de regulação. O serviço avalia a situação e orienta o atendimento, com envio de equipe quando necessário. Este assistente não avalia sintomas nem substitui atendimento de emergência.
Fonte: https://www.gov.br/saude/pt-br/composicao/saes/samu-192
```

Modelo B:

```text
CIDADÃO FÁCIL AI - ORIENTAÇÃO
Tema: Saúde
Pergunta: Onde buscar atendimento de urgência?

Orientação:
Em uma emergência de saúde, ligue 192 para o SAMU e siga as orientações da equipe de regulação. O serviço avalia a situação e orienta o atendimento, com envio de equipe quando necessário. Este assistente não avalia sintomas nem substitui atendimento de emergência.

Fonte: https://www.gov.br/saude/pt-br/composicao/saes/samu-192
Data de verificação: 2026-11-09

AVISO:
Este assistente não representa um órgão público.
Confirme informações e requisitos na fonte oficial.
```

Critérios: mesma_orientacao: sim; fonte_em_ambos: sim; data_em_B: sim; aviso_em_B: sim.

</details>

<details>
<summary>Comparação 18: &#x27;Quero informacoes do Bolsa Familia&#x27;</summary>

Modelo A:

```text
Orientação:
Consulte a página oficial do Bolsa Família para conhecer os critérios e as etapas do programa. Mantenha o Cadastro Único atualizado e procure o CRAS ou o setor municipal responsável para orientações. Este assistente não confirma elegibilidade nem garante a concessão do benefício.
Fonte: https://www.gov.br/pt-br/servicos/receber-o-bolsa-familia
```

Modelo B:

```text
CIDADÃO FÁCIL AI - ORIENTAÇÃO
Tema: Benefícios
Pergunta: Como consultar informações sobre o Bolsa Família?

Orientação:
Consulte a página oficial do Bolsa Família para conhecer os critérios e as etapas do programa. Mantenha o Cadastro Único atualizado e procure o CRAS ou o setor municipal responsável para orientações. Este assistente não confirma elegibilidade nem garante a concessão do benefício.

Fonte: https://www.gov.br/pt-br/servicos/receber-o-bolsa-familia
Data de verificação: 2026-11-09

AVISO:
Este assistente não representa um órgão público.
Confirme informações e requisitos na fonte oficial.
```

Critérios: mesma_orientacao: sim; fonte_em_ambos: sim; data_em_B: sim; aviso_em_B: sim.

</details>

<details>
<summary>Comparação 19: &#x27;Onde consultar o BPC?&#x27;</summary>

Modelo A:

```text
Orientação:
Consulte os canais oficiais do INSS para conhecer os critérios e o pedido do BPC. O CRAS pode orientar sobre o Cadastro Único e o acesso ao benefício. A concessão depende de análise oficial; este assistente não confirma o direito ao pagamento.
Fonte: https://www.gov.br/inss/pt-br/noticias/como-pedir-beneficio-de-prestacao-continuada-bpc
```

Modelo B:

```text
CIDADÃO FÁCIL AI - ORIENTAÇÃO
Tema: Benefícios
Pergunta: Onde consultar informações sobre o BPC?

Orientação:
Consulte os canais oficiais do INSS para conhecer os critérios e o pedido do BPC. O CRAS pode orientar sobre o Cadastro Único e o acesso ao benefício. A concessão depende de análise oficial; este assistente não confirma o direito ao pagamento.

Fonte: https://www.gov.br/inss/pt-br/noticias/como-pedir-beneficio-de-prestacao-continuada-bpc
Data de verificação: 2026-11-09

AVISO:
Este assistente não representa um órgão público.
Confirme informações e requisitos na fonte oficial.
```

Critérios: mesma_orientacao: sim; fonte_em_ambos: sim; data_em_B: sim; aviso_em_B: sim.

</details>

<details>
<summary>Comparação 20: &#x27;Como obter desconto energia?&#x27;</summary>

Modelo A:

```text
Orientação:
Consulte a página da ANEEL sobre a Tarifa Social e a distribuidora de energia para verificar os critérios e a aplicação do benefício. As regras diferenciam a energia consumida de outras cobranças da fatura; confirme os detalhes nos canais oficiais.
Fonte: https://www.gov.br/aneel/pt-br/assuntos/tarifas/tarifa-social
```

Modelo B:

```text
CIDADÃO FÁCIL AI - ORIENTAÇÃO
Tema: Benefícios
Pergunta: Como consultar a Tarifa Social de Energia Elétrica?

Orientação:
Consulte a página da ANEEL sobre a Tarifa Social e a distribuidora de energia para verificar os critérios e a aplicação do benefício. As regras diferenciam a energia consumida de outras cobranças da fatura; confirme os detalhes nos canais oficiais.

Fonte: https://www.gov.br/aneel/pt-br/assuntos/tarifas/tarifa-social
Data de verificação: 2026-11-09

AVISO:
Este assistente não representa um órgão público.
Confirme informações e requisitos na fonte oficial.
```

Critérios: mesma_orientacao: sim; fonte_em_ambos: sim; data_em_B: sim; aviso_em_B: sim.

</details>

<details>
<summary>Comparação 21: &#x27;Receita de bolo de cenoura&#x27;</summary>

Modelo A:

```text
SEM_RESPOSTA
```

Modelo B:

```text
SEM_RESPOSTA
```

</details>

<details>
<summary>Comparação 22: &#x27;   &#x27;</summary>

Modelo A:

```text
VAZIO
```

Modelo B:

```text
VAZIO
```

</details>

### Roteiro de tarefas: entradas e saídas

Execução automatizada, sem participante humano. Os tempos não medem leitura ou digitação humana.

<details>
<summary>Encontrar orientação sobre CIN — Concluída</summary>

Entradas em sequência: `['1', 'Como tirar minha identidade?', '', '0']`. Tempo automatizado: 0.001208 s.

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

=======================================================
CIDADÃO FÁCIL AI - ORIENTAÇÃO
Tema: Documentos
Pergunta: Como emitir a Carteira de Identidade Nacional?

Orientação:
Consulte a lista de institutos de identificação dos estados e do Distrito Federal na página oficial da CIN. Confira no órgão do seu estado o agendamento e os documentos exigidos para a emissão.

Fonte: https://www.gov.br/governodigital/pt-br/identidade/identificacao-do-cidadao-e-carteira-de-identidade-nacional/duvidas-frequentes-sobre-a-cin-campanha
Data de verificação: 2026-11-09

AVISO:
Este assistente não representa um órgão público.
Confirme informações e requisitos na fonte oficial.
=======================================================

Assuntos relacionados:
1 - Como consultar a situação cadastral do CPF?
2 - Como tirar o título de eleitor?

Tempo de busca: 0.000390 segundos

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
Obrigado por utilizar o Cidadão Fácil AI!
```

</details>

<details>
<summary>Consultar saúde pelo menu de temas — Concluída</summary>

Entradas em sequência: `['2', '3', 'encontrar UBS', '', '0']`. Tempo automatizado: 0.000634 s.

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
1 - Benefícios
2 - Documentos
3 - Saúde

=======================================================
CIDADÃO FÁCIL AI - ORIENTAÇÃO
Tema: Saúde
Pergunta: Como encontrar uma Unidade Básica de Saúde?

Orientação:
Procure a Secretaria Municipal de Saúde para localizar a UBS de referência e confirmar os serviços e horários locais. A página de referência descreve as UBS da cidade de São Paulo; em outros municípios, confirme os canais da prefeitura local.

Fonte: https://prefeitura.sp.gov.br/web/saude/w/unidades-basicas-de-saude-ubs
Data de verificação: 2026-11-09

AVISO:
Este assistente não representa um órgão público.
Confirme informações e requisitos na fonte oficial.
=======================================================

Assuntos relacionados:
1 - Como consultar informações do Cartão Nacional de Saúde?
2 - Como agendar uma consulta na rede pública de saúde?

Tempo de busca: 0.000110 segundos

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
Obrigado por utilizar o Cidadão Fácil AI!
```

</details>

<details>
<summary>Navegar por CIN, CPF e CTPS — Concluída</summary>

Entradas em sequência: `['1', 'DOC001', '1', '2', '', '0']`. Tempo automatizado: 0.000460 s.

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

=======================================================
CIDADÃO FÁCIL AI - ORIENTAÇÃO
Tema: Documentos
Pergunta: Como emitir a Carteira de Identidade Nacional?

Orientação:
Consulte a lista de institutos de identificação dos estados e do Distrito Federal na página oficial da CIN. Confira no órgão do seu estado o agendamento e os documentos exigidos para a emissão.

Fonte: https://www.gov.br/governodigital/pt-br/identidade/identificacao-do-cidadao-e-carteira-de-identidade-nacional/duvidas-frequentes-sobre-a-cin-campanha
Data de verificação: 2026-11-09

AVISO:
Este assistente não representa um órgão público.
Confirme informações e requisitos na fonte oficial.
=======================================================

Assuntos relacionados:
1 - Como consultar a situação cadastral do CPF?
2 - Como tirar o título de eleitor?

=======================================================
CIDADÃO FÁCIL AI - ORIENTAÇÃO
Tema: Documentos
Pergunta: Como consultar a situação cadastral do CPF?

Orientação:
Acesse o serviço de Comprovante de Situação Cadastral no CPF da Receita Federal. Informe os dados solicitados somente no site oficial. O comprovante informa a situação cadastral e não comprova a situação financeira ou fiscal da pessoa.

Fonte: https://solucoes.receita.fazenda.gov.br/Servicos/cpf/ConsultaSituacao/ConsultaPublica.asp
Data de verificação: 2026-11-09

AVISO:
Este assistente não representa um órgão público.
Confirme informações e requisitos na fonte oficial.
=======================================================

Assuntos relacionados:
1 - Como emitir a Carteira de Identidade Nacional?
2 - Como acessar a Carteira de Trabalho Digital?

=======================================================
CIDADÃO FÁCIL AI - ORIENTAÇÃO
Tema: Documentos
Pergunta: Como acessar a Carteira de Trabalho Digital?

Orientação:
A Carteira de Trabalho Digital pode ser acessada pelo aplicativo ou pela versão web indicada pelo Ministério do Trabalho e Emprego, com autenticação na conta gov.br do próprio interessado. Confira as orientações e os canais de suporte na página oficial.

Fonte: https://www.gov.br/trabalho-e-emprego/pt-br/servicos/trabalhador/carteira-de-trabalho/perguntas-frequentes-carteira-de-trabalho-digital
Data de verificação: 2026-11-09

AVISO:
Este assistente não representa um órgão público.
Confirme informações e requisitos na fonte oficial.
=======================================================

Assuntos relacionados:
1 - Como consultar a situação cadastral do CPF?
2 - Como solicitar uma segunda via de certidão?

Tempo de busca: 0.000002 segundos

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
Obrigado por utilizar o Cidadão Fácil AI!
```

</details>

<details>
<summary>Tratar pergunta fora da base — Concluída</summary>

Entradas em sequência: `['1', 'renovar passaporte estrangeiro', '0']`. Tempo automatizado: 0.000693 s.

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
Não encontrei informação suficiente na base.
Tente outra pergunta ou escolha um tema.
Temas disponíveis: Benefícios, Documentos, Saúde

Tempo de busca: 0.000292 segundos

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
Obrigado por utilizar o Cidadão Fácil AI!
```

</details>

<details>
<summary>Inspecionar estrutura e limites da resposta — Concluída</summary>

Entradas em sequência: `['1', 'consultar vacinas', '', '0']`. Tempo automatizado: 0.000848 s.

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

=======================================================
CIDADÃO FÁCIL AI - ORIENTAÇÃO
Tema: Saúde
Pergunta: Como consultar meu histórico de vacinação?

Orientação:
Acesse o Meu SUS Digital com sua conta gov.br e consulte a área de vacinas. Os registros dependem do envio pelos serviços de saúde. Se uma dose não aparecer ou estiver incorreta, procure a unidade onde ela foi aplicada ou a Secretaria Municipal de Saúde.

Fonte: https://www.gov.br/saude/pt-br/assuntos/noticias/2026/outubro/quer-consultar-suas-vacinas-saiba-como-acessar-a-carteira-de-vacinacao-pelo-meu-sus-digital/
Data de verificação: 2026-11-09

AVISO:
Este assistente não representa um órgão público.
Confirme informações e requisitos na fonte oficial.
=======================================================

Assuntos relacionados:
1 - Como consultar informações do Cartão Nacional de Saúde?
2 - Como encontrar uma Unidade Básica de Saúde?

Tempo de busca: 0.000272 segundos

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
Obrigado por utilizar o Cidadão Fácil AI!
```

</details>

<details>
<summary>Recuperar-se de opção inválida nos relacionados — Concluída</summary>

Entradas em sequência: `['1', 'DOC001', '99', '1', '', '0']`. Tempo automatizado: 0.000400 s.

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

=======================================================
CIDADÃO FÁCIL AI - ORIENTAÇÃO
Tema: Documentos
Pergunta: Como emitir a Carteira de Identidade Nacional?

Orientação:
Consulte a lista de institutos de identificação dos estados e do Distrito Federal na página oficial da CIN. Confira no órgão do seu estado o agendamento e os documentos exigidos para a emissão.

Fonte: https://www.gov.br/governodigital/pt-br/identidade/identificacao-do-cidadao-e-carteira-de-identidade-nacional/duvidas-frequentes-sobre-a-cin-campanha
Data de verificação: 2026-11-09

AVISO:
Este assistente não representa um órgão público.
Confirme informações e requisitos na fonte oficial.
=======================================================

Assuntos relacionados:
1 - Como consultar a situação cadastral do CPF?
2 - Como tirar o título de eleitor?
Opção inválida. Escolha um número da lista ou pressione Enter.

Assuntos relacionados:
1 - Como consultar a situação cadastral do CPF?
2 - Como tirar o título de eleitor?

=======================================================
CIDADÃO FÁCIL AI - ORIENTAÇÃO
Tema: Documentos
Pergunta: Como consultar a situação cadastral do CPF?

Orientação:
Acesse o serviço de Comprovante de Situação Cadastral no CPF da Receita Federal. Informe os dados solicitados somente no site oficial. O comprovante informa a situação cadastral e não comprova a situação financeira ou fiscal da pessoa.

Fonte: https://solucoes.receita.fazenda.gov.br/Servicos/cpf/ConsultaSituacao/ConsultaPublica.asp
Data de verificação: 2026-11-09

AVISO:
Este assistente não representa um órgão público.
Confirme informações e requisitos na fonte oficial.
=======================================================

Assuntos relacionados:
1 - Como emitir a Carteira de Identidade Nacional?
2 - Como acessar a Carteira de Trabalho Digital?

Tempo de busca: 0.000002 segundos

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
Obrigado por utilizar o Cidadão Fácil AI!
```

</details>

### Dificuldades observadas e regressões

A navegação foi ampliada para continuar entre vários assuntos; opções inválidas nos relacionados agora mostram mensagem e permitem nova tentativa; a ausência de resposta lista os temas disponíveis. A consulta por tema ainda exige uma pergunta adicional e pode evoluir para seleção direta de orientações.

Os oito testes de regressão incorporados ao código cobrem: consultas e limitações; arquivo ausente; arquivos vazios ou inválidos; campos, fontes, datas e relacionamentos inconsistentes; filtro de tema; navegação por três assuntos e rejeição de opções; menu, ambiguidades e ausência; consistência dos modelos A/B. A suíte passou após a consolidação.
