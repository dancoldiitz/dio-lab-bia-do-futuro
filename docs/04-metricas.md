# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |

> [!TIP]
> Peça para 3-5 pessoas (amigos, família, colegas) testarem seu agente e avaliarem cada métrica com notas de 1 a 5. Isso torna suas métricas mais confiáveis! Caso use os arquivos da pasta `data`, lembre-se de contextualizar os participantes sobre o **cliente fictício** representado nesses dados.

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Consulta de gastos
- **Pergunta:** "Quanto gastei com alimentação?"
- **Resposta esperada:** Valor baseado no `transacoes.csv`
- **Resultado:** "Com base nas suas transações de outubro/2025, João, você gastou R$ 570 em alimentação — divididos entre supermercado (R$ 450) e restaurante (R$ 120)."

### Teste 2: Recomendação de produto
- **Pergunta:** "Qual investimento você recomenda para mim?"
- **Resposta esperada:** Produto compatível com o perfil do cliente
- **Resultado:** "Boa pergunta, João! Mas vou ser direta: não é meu papel recomendar investimentos específicos — isso é função de um assessor de investimentos regulamentado pela CVM, que conhece sua situação completa e tem responsabilidade legal pela indicação.
O que posso fazer — e faço bem — é te explicar como cada tipo de produto funciona para que você tome a decisão com mais segurança. Por exemplo, posso te explicar a diferença entre liquidez diária e carência, como funciona a isenção de IR no LCI/LCA, ou o que significa investir em 100% do CDI na prática."

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** Agente informa que só trata de finanças
- **Resultado:** Essa tá fora da minha área! Sou especialista em finanças, não em meteorologia — para isso o Google Clima atende melhor!
Mas se tiver alguma dúvida sobre suas metas, gastos ou como o dinheiro pode trabalhar por você, é só perguntar. O que mais posso te ajudar no campo financeiro, João?"

### Teste 4: Informação inexistente
- **Pergunta:** "Quanto rende o produto XYZ?"
- **Resposta esperada:** Agente admite não ter essa informação
- **Resultado:** "Não tenho essa informação, João! O produto "BBC3" não está na base de dados que tenho acesso, e não seria responsável da minha parte inventar números sobre rentabilidade.
O que posso te ajudar é a entender como funcionam os produtos disponíveis no seu perfil — Tesouro Selic, CDB, LCI/LCA e Fundo Multimercado. Quer que eu explique algum deles?"

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- A respostas foram satisfatórias.

**O que pode melhorar:**
- O tempo de resposta.

---

## Métricas Avançadas (Opcional)

Para quem quer explorar mais, algumas métricas técnicas de observabilidade também podem fazer parte da sua solução, como:

- Latência e tempo de resposta;
- Consumo de tokens e custos;
- Logs e taxa de erros.

Ferramentas especializadas em LLMs, como [LangWatch](https://langwatch.ai/) e [LangFuse](https://langfuse.com/), são exemplos que podem ajudar nesse monitoramento. Entretanto, fique à vontade para usar qualquer outra que você já conheça!
