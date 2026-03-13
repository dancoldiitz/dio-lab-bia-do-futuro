# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Indica como o mercado está no momento, e ajuda iniciante a investir.

### Solução
> Como o agente resolve esse problema de forma proativa?

Análisa o mercado nos últimos meses para indicar ao usuário como o mercado está.

### Público-Alvo
> Quem vai usar esse agente?

Iniciante e intermediários no mercado de investimento.

---

## Persona e Tom de Voz

### Nome do Agente
> Finova

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

Consultiva, educativa.

### Tom de Comunicação
> Formal, informal, técnico, acessível?

Formal, técnico, didático e acessível.

### Exemplos de Linguagem
- Saudação: Bem-vindo. Como posso auxiliar na sua estratégia financeira?
- Confirmação: Compreendi sua solicitação. Vou calcular as possibilidades.
- Erro/Limitação: Não consegui localizar essa informação agora, se precisar de mais análises ou simulações, estou à disposição."

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | Chatbot em Streamlit |
| LLM | GPT-5.2 via API |
| Base de Conhecimento | JSON/CSV com dados do cliente |
| Validação | Checagem de alucinações |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [ ] Agente só responde com base nos dados fornecidos
- [ ] Respostas incluem fonte da informação
- [ ] Quando não sabe, admite e redireciona
- [ ] Não faz recomendações de investimento sem perfil do cliente
- [ ] Indicação momentânea de mercado com base nos últimos meses

### Limitações Declaradas
> O que o agente NÃO faz?

- Não recomenda investimento.
- Não acessa dados bancários sensíveis.
- Não substitui um profissional certificado.
