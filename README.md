Finova: Agente Financeiro Inteligente
A Finova é um agente proativo de inteligência financeira desenvolvido para transformar dados brutos em consultoria estratégica. Ao contrário de assistentes reativos, a Finova analisa históricos de transações e perfis de investimento para antecipar necessidades, sugerir metas e garantir decisões seguras baseadas em dados reais.

Este projeto é a minha solução para o desafio BIA do Futuro (DIO).

🎯 O que a Finova faz?
A solução foi desenhada para atuar em três pilares principais:

Antecipação: Identifica padrões de gastos e alerta sobre desvios antes que o orçamento seja comprometido.

Personalização: Cruza o histórico de transações com o perfil do investidor para oferecer produtos financeiros adequados.

Segurança (Anti-alucinação): Utiliza uma base de conhecimento fechada (RAG-ready) para garantir que nenhuma recomendação financeira seja inventada.

📂 Estrutura do Projeto
O desenvolvimento foi dividido em camadas para garantir escalabilidade e organização:

1. Documentação e Estratégia (/docs)
Caso de Uso & Arquitetura: Definição da persona, fluxo de dados e como a Finova resolve problemas reais.

Base de Conhecimento: Estratégia de consumo dos dados (CSV/JSON).

Engenharia de Prompts: System prompts detalhados e tratamento de casos críticos.

Métricas de Avaliação: Como medimos a assertividade e segurança das respostas.

Pitch de Negócio: Roteiro da apresentação da solução.

2. Base de Dados (/data)
Utilização de dados mockados para simular um ambiente real:

transacoes.csv: Histórico financeiro detalhado.

perfil_investidor.json: Tolerância de acordo com objetivo e restrições do cliente.

produtos_financeiros.json: Catálogo de investimentos disponíveis.

3. Implementação Técnica (/src)
Integração com LLM: Uso da API do gpt-oss para processamento de linguagem natural.

Lógica de Dados: Scripts em Python para leitura e filtragem de contexto financeiro.

Interface: Protótipo funcional desenvolvido para interação em tempo real.

🛠️ Tecnologias Utilizadas
Linguagem: Python

IA Generativa: Chat GTP 5.2 API

Análise de Dados: Pandas & Numpy

Ambiente: Ollama / VSCode

Documentação: Markdown & Mermaid.js (Diagramas)

🚀 Como visualizar a solução
Navegue até a pasta /docs para entender a base teórica e de segurança.

Acesse a pasta /src para revisar o código fonte da aplicação e a lógica de integração com a IA.

Confira os exemplos de interação documentados em Prompts.

Desenvolvido por Lucas Daniel de Oliveira Santos
Junior Data Analyst | Certificado Google Data Analytics
LinkedIn - https://www.linkedin.com/in/daniel-santos-b3425a2a5/
