# Uso de inteligência artificial

Global Solution 2026.2 — FIAP | Cidadão Fácil AI Plus

Lucas Sousa — RM 573029
Dayse Borges de Sousa — RM 573036

## Finalidade e contexto

Ferramentas de inteligência artificial da OpenAI foram utilizadas como suporte ao desenvolvimento, à revisão e à verificação/validação do projeto. O apoio abrangeu análise dos requisitos, discussão de alternativas de implementação, revisão de código e documentação, identificação de inconsistências e preparação e execução de avaliações.

O uso ocorreu em atividades de apoio ao longo do trabalho. Este registro descreve finalidades, critérios de revisão e evidências. Os dois modelos de resposta do assistente são formatos internos de apresentação.

## Atividades apoiadas

- Conferência dos requisitos e identificação de lacunas entre documentação e implementação.
- Discussão das estruturas de dados, da busca por palavras-chave e da navegação entre assuntos.
- Apoio à implementação e revisão de validações, tratamento de erros e instruções de resposta.
- Revisão de clareza, coerência e organização dos textos.
- Consulta a referências institucionais para confrontar as orientações da base com fontes identificáveis.
- Preparação de cenários e apoio à execução e interpretação dos testes de consulta, regressão e roteiro de tarefas.

## Verificação e validação

As sugestões de IA não foram consideradas prova de correção por si só. A verificação técnica usou execução real do Python e critérios explícitos de resultado esperado. A avaliação documental confrontou os resumos com páginas institucionais e registrou a data, o escopo e as restrições de acesso.

As evidências foram consolidadas no [relatório PDF](relatorio.pdf): registros de consultas com esperado, obtido e duração; comparação A/B; roteiro de tarefas; conferência das fontes e limites. Os procedimentos de avaliação e os oito testes de regressão estão incorporados a `src/sistema.py` e podem ser repetidos com os comandos documentados no README.

Os resultados indicam comportamento no conjunto avaliado. A comparação de modelos verifica estrutura e consistência; o roteiro verifica conclusão de tarefas. Essas evidências não comprovam compreensão humana, correção em todas as perguntas ou concessão de serviços públicos.

## Modelos de instrução do assistente

O protótipo utiliza dois formatos internos, implementados em Python:

**Modelo A:** apresentar a orientação resumida da base e sua fonte, sem acrescentar informações externas.

**Modelo B:** apresentar tema, pergunta, orientação, fonte, data de verificação e aviso de informação não oficial, recomendando confirmar os requisitos no canal responsável.

Em ambos, a ausência de base suficiente deve preservar o aviso de limitação. O Modelo B foi escolhido por explicitar mais elementos de transparência. Os modelos foram comparados nas perguntas do plano; sua maior extensão não prova maior compreensão.

O sistema não envia esses modelos a uma API e não depende de IA generativa durante as consultas.

## Limites e responsabilidade

A IA pode sugerir conteúdo impreciso, desatualizado ou inadequado ao contexto. A busca lexical também pode associar uma pergunta ao registro errado. Por isso, a equipe permanece responsável pela compreensão do código, revisão final, conferência das referências e interpretação dos indicadores.

A verificação das fontes não substitui atendimento oficial nem análise individual. A restrição de acesso direto à referência do CNJ está registrada. A avaliação automatizada não substitui testes com pessoas ou tecnologias assistivas.

O protótipo não envia as consultas a APIs de IA, mantém o histórico apenas na memória e exibe resultados de cenários fixos de teste no terminal. O relatório entregue registra somente esses cenários.

## Conclusão

A inteligência artificial apoiou o processo de desenvolvimento, revisão e verificação/validação. A justificativa técnica da solução se apoia no código, nas fontes documentadas e nas avaliações reproduzíveis, respeitando os limites das evidências disponíveis.
