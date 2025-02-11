import streamlit as st
import pandas as pd
import sqlite3
import torch
from transformers import pipeline

# Carregar modelo BERT pré-treinado para análise de sentimentos
sentiment_pipeline = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

# Dicionário para mapear mensagens para soft skills
SOFT_SKILLS_MAP = {
    "colaboração": ["colaboração", "trabalho em equipe", "ajudar", "cooperação"],
    "liderança": ["liderança", "iniciativa", "tomar decisões", "orientar"],
    "resolução de problemas": ["resolver", "solução", "problema", "melhoria"],
    "gestão de tempo": ["prazo", "entrega", "urgente", "finalizar"],
    "comunicação": ["falar", "discutir", "explicar", "reunião"]
}


def classificar_soft_skill(texto):
    """Classifica a soft skill com base nas palavras-chave presentes na mensagem."""
    texto = texto.lower()
    for skill, keywords in SOFT_SKILLS_MAP.items():
        if any(word in texto for word in keywords):
            return skill.capitalize()
    return "Não Identificado"


def analisar_sentimento_bert(texto):
    """Usa BERT para classificar o sentimento da frase, com ajustes para mensagens curtas e neutras."""
    texto = texto.strip()

    # Se a mensagem for vazia ou muito curta, classificamos como Neutro
    if not texto or len(texto) < 10:
        return "Neutro"

    resultado = sentiment_pipeline(texto)[0]
    label = resultado["label"]

    if "1 star" in label:
        return "Muito Negativo"
    elif "2 stars" in label:
        return "Negativo"
    elif "3 stars" in label:
        return "Neutro"
    elif "4 stars" in label:
        return "Positivo"
    elif "5 stars" in label:
        return "Muito Positivo"

    return "Neutro"


# Conectar ao banco de dados
def conectar_bd():
    return sqlite3.connect("softskills.db")


# Criar a interface Streamlit
st.title("📊 Mapeamento de Soft Skills com BERT")
st.write("Este sistema agora usa **BERT** para análise de sentimentos e mapeamento de soft skills!")

# Selecionar se é um candidato ou colaborador
categoria = st.selectbox("📌 Selecione a categoria da interação", ["Candidato", "Colaborador"])

# Selecionar tipo de interação
tipo_interacao = st.selectbox("📌 Selecione o tipo de interação", ["Email", "Transcrição", "Outro"])

# Upload de arquivos CSV/TXT
uploaded_file = st.file_uploader("📂 Faça upload de um arquivo CSV ou TXT", type=["csv", "txt"])

if uploaded_file and tipo_interacao and categoria:
    if uploaded_file.name.endswith(".csv"):
        df_upload = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith(".txt"):
        df_upload = pd.DataFrame({"conteudo": uploaded_file.read().decode("utf-8").splitlines()})

    # Remover linhas vazias ou apenas com espaços
    df_upload = df_upload[df_upload["conteudo"].str.strip() != ""]
    df_upload = df_upload.dropna(subset=["conteudo"])  # Remove linhas com valores NaN

    # Adicionar a coluna do tipo de interação e categoria
    df_upload["tipo"] = tipo_interacao
    df_upload["categoria"] = categoria

    # Aplicar análise de sentimentos
    df_upload["Sentimento"] = df_upload["conteudo"].apply(analisar_sentimento_bert)

    # Classificar Soft Skills
    df_upload["Soft_Skill"] = df_upload["conteudo"].apply(classificar_soft_skill)

    con = conectar_bd()
    df_upload.to_sql("interacoes", con, if_exists="append", index=False)
    con.close()

    st.success("✅ Dados adicionados com sucesso!")

# Carregar interações do banco
con = conectar_bd()
df = pd.read_sql("SELECT * FROM interacoes", con)
con.close()

# Filtrar apenas candidatos e colaboradores conhecidos
df = df[df["categoria"].isin(["Candidato", "Colaborador"])]

# Remover linhas que tenham valores NaN na coluna "conteudo"
df = df.dropna(subset=["conteudo"])

# Aplicar análise de sentimentos e exibir tabela
if not df.empty:
    st.dataframe(df)

# Cálculo de Engajamento
st.subheader("📈 Índice de Engajamento dos Colaboradores")
if not df.empty:
    engajamento = df.groupby("categoria")["Sentimento"].count().reset_index()
    engajamento.columns = ["categoria", "interacoes"]
    engajamento["Engajamento"] = engajamento["interacoes"] * 10  # Exemplo de cálculo
    st.dataframe(engajamento)

# Relatórios de Sentimentos por Departamento
st.subheader("🏢 Relatórios de Sentimentos por Departamento")
if not df.empty:
    sentimento_departamento = df.groupby("tipo")["Sentimento"].value_counts().unstack().fillna(0)
    st.bar_chart(sentimento_departamento)
