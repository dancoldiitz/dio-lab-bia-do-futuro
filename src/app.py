import os, json
import pandas as pd
import requests
import streamlit as st

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss:latest"
MAX_HISTORICO = 10
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@st.cache_data
def carregar_dados():
    with open(os.path.join(BASE_DIR, "data", "perfil_investidor.json"), encoding="utf-8") as f:
        perfil = json.load(f)
    transacoes = pd.read_csv(os.path.join(BASE_DIR, "data", "transacoes.csv"))
    historico  = pd.read_csv(os.path.join(BASE_DIR, "data", "historico_atendimento.csv"))
    with open(os.path.join(BASE_DIR, "data", "produtos_financeiros.json"), encoding="utf-8") as f:
        produtos = json.load(f)
    return perfil, transacoes, historico, produtos

try:
    perfil, transacoes, historico, produtos = carregar_dados()
except FileNotFoundError as e:
    st.error(f"Erro ao carregar arquivos: {e}")
    st.stop()

contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMONIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}
TRANSACOES:
{transacoes.to_string(index=False)}
ATENDIMENTOS:
{historico.to_string(index=False)}
PRODUTOS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

SYSTEM_PROMPT = f"""Voce eh a Finova, consultora e educadora financeira.
REGRAS:
- NUNCA recomende investimentos especificos, apenas explique como funcionam;
- JAMAIS responda fora do tema de financas pessoais;
- Use o contexto para exemplos personalizados;
- Linguagem simples e direta;
- Maximo 3 paragrafos;
- Sempre pergunte se o cliente entendeu.
CONTEXTO DO CLIENTE:
{contexto}"""

def formatar_historico(mensagens):
    linhas = []
    for msg in mensagens:
        papel = "Cliente" if msg["role"] == "user" else "Finova"
        linhas.append(f"{papel}: {msg['content']}")
    return "\n".join(linhas)

def perguntar(mensagem_atual, historico_conversa):
    historico_recente = historico_conversa[-(MAX_HISTORICO * 2):]
    historico_texto = formatar_historico(historico_recente)

    prompt = f"""{SYSTEM_PROMPT}

HISTORICO DA CONVERSA:
{historico_texto}

Cliente: {mensagem_atual}
Finova:"""

    try:
        r = requests.post(
            OLLAMA_URL,
            json={"model": MODELO, "prompt": prompt, "stream": False},
            timeout=120
        )
        r.raise_for_status()
        return r.json().get("response", "Erro ao gerar resposta.")
    except requests.exceptions.Timeout:
        return "O modelo demorou demais. Tente novamente."
    except requests.exceptions.ConnectionError:
        return "Nao foi possivel conectar ao Ollama. Verifique se esta rodando."
    except requests.exceptions.HTTPError as e:
        return f"Erro HTTP {e.response.status_code}: {e.response.text}"
    except Exception as e:
        return f"Erro: {e}"

if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

st.title("Finova - Consultora e Educadora Financeira")

for msg in st.session_state.mensagens:
    st.chat_message(msg["role"]).write(msg["content"])

if pergunta := st.chat_input("Sua duvida sobre financas..."):
    st.chat_message("user").write(pergunta)
    st.session_state.mensagens.append({"role": "user", "content": pergunta})
    with st.spinner("Pensando..."):
        resposta = perguntar(pergunta, st.session_state.mensagens[:-1])
    st.chat_message("assistant").write(resposta)
    st.session_state.mensagens.append({"role": "assistant", "content": resposta})



 # .venv\Scripts\pip.exe install streamlit pandas requests
 # .venv\Scripts\streamlit.exe run src/app.py
   
