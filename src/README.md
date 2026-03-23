# Passo a Passo de Execução


Esta pasta contém o código do seu agente financeiro.

## Estrutura Sugerida

```
src/
├── app.py              # Aplicação principal (Streamlit)
```
## Setup do Ollama

```
# 1. Instalar o Ollama (ollama.com)
# 2. Baixar um modelo leve
ollama pull gpt-oss
# 3. Testar se funciona
ollama run gpt-oss "Oi!"
```

## Código Completo 

```
Todo o código fonte está no arquivo "app.py".
```

## Como Rodar

```bash
# Instalar dependências
 .venv\Scripts\pip.exe install streamlit pandas requests

# Rodar a aplicação
 .venv\Scripts\streamlit.exe run src/app.py
```
