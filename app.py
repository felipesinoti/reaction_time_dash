# Para ativar a venv: .venv\Scripts\activate
import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import mpld3
import pandas as pd
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import numpy as np
from streamlit.components.v1 import html

st.set_page_config(
    page_title="Minha Aplicação",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Website's general configurations
arquivo = 'page.html'

# Leitura do conteúdo do arquivo HTML
with open(arquivo, 'r', encoding='utf-8') as f:
    conteudo_html = f.read()

# Exibição do conteúdo HTML no Streamlit
components.html(conteudo_html, height=5800, scrolling=True)#, unsafe_allow_html=True)#, scrolling=True)

# app_cluster.py
import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Carrega o pipeline já treinado
with open("cluster_pipeline.pkl", "rb") as f:
    saved = pickle.load(f)
pipeline      = saved["pipeline"]
features      = saved["features"]
label_mappings= saved["mappings"]

# 2) Dicionários de tradução para exibição
gender_display = {
    "Male":   "Masculino",
    "Female": "Feminino",
    "Other":  "Outro"
}
# preencha conforme as chaves reais do seu label_mappings["Diet_Type"]
diet_display = {
    "Non-Vegetarian":    "Não Vegetariano",
    "Vegetarian":  "Vegetariano",
    "Vegan":       "Vegano"
}

# Inverte para mapear de volta ao original na hora da codificação
inv_gender_display = {v:k for k,v in gender_display.items()}
inv_diet_display   = {v:k for k,v in diet_display.items()}

# Mapa de nomes amigáveis para cada cluster
cluster_names = {
    0: "Jovens Ocupados",
    1: "Veteranos com Tempo Livre",
    2: "Jovens Cafeinados",
    3: "Veteranos Ágeis"
}

st.title("🧠 Predição de Cluster K-Means")

with st.form("form_cluster"):

    # --- inputs numéricos ---
    Age             = st.number_input("Idade",                min_value= int(18), max_value=int(59), value=30)
    Sleep_Duration  = st.slider("Duração do Sono (h)",      min_value=4.0,  max_value=10.0, step=0.5, value=7.0)
    Stress_Level    = st.slider("Nível de Estresse",        min_value=0,    max_value=10,  step=1,   value=5)
    Daily_Screen_Time = st.slider("Tempo de Tela Diário (h)",min_value=0.0,  max_value=12.0, step=0.5, value=6.0)
    Caffeine_Intake = st.number_input("Consumo de Cafeína (mg/dia)", min_value=0, max_value=499, value=200)
    Memory_Test_Score = st.number_input("Pontuação no Teste de Memória", min_value=40, max_value=99, value=70)
    Reaction_Time = st.number_input("Pontuação no Teste de Tempo de Reação", min_value=200, max_value=600, value=300)

    # --- inputs categóricos ---
    gender_opts   = list(label_mappings["Gender"].keys())
    diet_opts     = list(label_mappings["Diet_Type"].keys())
    
    Gender_pt   = st.selectbox("Gênero", list(gender_display.values()))
    Diet_Type_pt= st.selectbox("Tipo de Dieta", list(diet_display.values()))

    # submitted = st.form_submit_button("📊 Predizer Cluster")

    # Gender        = st.selectbox("Gênero",    gender_opts)
    # Diet_Type     = st.selectbox("Tipo de Dieta", diet_opts)

    submitted = st.form_submit_button("📊 Predizer Cluster")

if submitted:
    # 1) Codifica categorias
    print(label_mappings["Gender"])
    if(Gender_pt == "Masculino"):
        Gender = "Male"
    elif(Gender_pt == "Feminino"):
        Gender = "Female"
    elif(Gender_pt == "Outro"):
        Gender = "Other"
        
    if(Diet_Type_pt == "Não Vegetariano"):
        Diet_Type = 'Non-Vegetarian'
    elif(Diet_Type_pt == "Vegetariano"):
        Diet_Type = 'Vegetarian'
    elif(Diet_Type_pt == "Vegano"):
        Diet_Type = 'Vegan'
    
    Gender_enc    = label_mappings["Gender"][Gender]
    Diet_Type_enc = label_mappings["Diet_Type"][Diet_Type]

    # 2) Monta vetor de entrada na ordem correta
    x_input = [
        Age,
        Sleep_Duration,
        Stress_Level,
        Daily_Screen_Time,
        Caffeine_Intake,
        Reaction_Time,
        # Note: Reaction_Time não deve fazer parte das features de entrada — omitimos aqui
        # Memory_Test_Score está no lugar de Reaction_Time no pipeline de clustering
        # Se você usou Reaction_Time como feature, inclua-a também aqui!
        Memory_Test_Score,
        Gender_enc,
        Diet_Type_enc
    ]

    # 3) Converte para array 2D e prediz
    x_arr = np.array(x_input).reshape(1, -1)
    cluster_label = pipeline.predict(x_arr)[0]
    nome = cluster_names.get(cluster_label, f"Cluster {cluster_label}")

    st.success(f"O indivíduo foi atribuído ao **{nome}** (cluster {cluster_label}).")

st.set_option('deprecation.showPyplotGlobalUse', False)