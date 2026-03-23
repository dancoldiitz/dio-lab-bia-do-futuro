# 💡 Finova — Agente Financeiro Inteligente com IA Generativa

> Consultora financeira didática, assertiva e acessível — desenvolvida como solução para o desafio [DIO · Bia do Futuro](https://github.com/digitalinnovationone/dio-lab-bia-do-futuro).

---

## Sobre o Projeto

A **Finova** resolve um problema real: a maioria dos brasileiros não sabe por onde começar a investir. Não por falta de dinheiro, mas por falta de orientação personalizada e acessível.

A Finova analisa o perfil real do cliente — renda, metas, gastos, tolerância a risco — e responde como uma consultora especialista, de forma didática e sem jargões. Ela **educa para a decisão**, mas nunca recomenda investimentos específicos.

---

## Funcionalidades

- 💬 **Chat com IA** contextualizado com dados reais do cliente
- 📊 **Análise de perfil** — patrimônio, reserva de emergência, metas e prazos
- 💸 **Diagnóstico de gastos** — categorias, taxa de poupança, transações
- 📦 **Catálogo de produtos** filtrado por perfil de risco
- 🌐 **Busca de mercado em tempo real** integrada às respostas
- 🛡️ **Guardrails de segurança** — sem alucinação, sem recomendação indevida

---

## Estrutura do Repositório

```
📁 dio-lab-bia-do-futuro/
├── 📁 data/
│   ├── perfil_investidor.json        # Perfis: João Silva (moderado) e Daniel Santos (arrojado)
│   ├── produtos_financeiros.json     # Tesouro Selic, CDB, LCI/LCA, Fundos
│   ├── transacoes.csv                # Histórico de transações (out/2025)
│   └── historico_atendimento.csv     # Histórico de atendimentos anteriores
│
├── 📁 docs/
│   ├── 01-documentacao-agente.md     # Caso de uso, persona, arquitetura e guardrails
│   ├── 02-base-conhecimento.md       # Estratégia de dados e injeção de contexto
│   ├── 03-prompts.md                 # System prompt + exemplos de interação + edge cases
│   ├── 04-metricas.md                # Métricas, bateria de testes e matriz de risco
│   └── 05-pitch.md                   # Roteiro cronometrado do pitch (3 minutos)
│
├── 📁 src/
│   ├── app.py                        # Aplicação Streamlit funcional
│   └── requirements.txt
│
└── 📁 assets/
    └── Finova_Pitch.pptx             # Slides do pitch (9 slides)
```

---

## Como Executar

```bash
# 1. Instalar dependências
pip install -r src/requirements.txt

# 2. Configurar a chave da API Anthropic
export ANTHROPIC_API_KEY=sk-...

# 3. Rodar a aplicação
streamlit run src/app.py
```

---

## Arquitetura

```
Interface (Streamlit / Widget)
        │
        ▼
Contexto injetado (JSON + CSV do cliente)
        │
        ▼
LLM — Claude Sonnet via API Anthropic
     + Web Search (mercado em tempo real)
        │
        ▼
Guardrails de validação
(sem alucinação · sem recomendação · admite limitações)
```

---

## Segurança e Limites Declarados

| O que a Finova FAZ | O que a Finova NÃO FAZ |
|---|---|
| Explica como produtos financeiros funcionam | Recomendar investimentos específicos |
| Analisa gastos e metas com dados reais | Acessar dados bancários sensíveis |
| Admite quando não tem uma informação | Inventar números ou rentabilidades |
| Redireciona para profissional quando necessário | Substituir um assessor certificado pela CVM |

---

## Tecnologias

- **LLM:** Claude Sonnet (Anthropic API)
- **Interface:** Streamlit · HTML/JS (Claude Artifacts)
- **Dados:** JSON + CSV mockados
- **Busca:** Web Search integrada via API

---

## Documentação

| Arquivo | Conteúdo |
|---|---|
| [`docs/01-documentacao-agente.md`](docs/01-documentacao-agente.md) | Caso de uso, persona, arquitetura |
| [`docs/02-base-conhecimento.md`](docs/02-base-conhecimento.md) | Estrutura dos dados e estratégia de contexto |
| [`docs/03-prompts.md`](docs/03-prompts.md) | System prompt e exemplos de interação |
| [`docs/04-metricas.md`](docs/04-metricas.md) | Métricas de qualidade e testes |
| [`docs/05-pitch.md`](docs/05-pitch.md) | Roteiro do pitch de 3 minutos |

---

*Desenvolvido por **Lucas Daniel de Oliveira Santos** · Desafio DIO — Bia do Futuro*
```
LinkedIn - https://www.linkedin.com/in/daniel-santos-b3425a2a5/
```
