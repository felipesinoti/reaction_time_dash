import streamlit as st
import numpy as np
import pandas as pd
# import hydralit_components as hc
from machine_learning_algorithm import model
from funcoes import valores_categoricos, return_values
# Carregando os dados
df = pd.read_excel("alzheirmer_data - Copia.xlsx")
X = df.iloc[:,0:14]
y = df.iloc[:,14]
pd.get_dummies(X,columns=['Ethnicity',"Gender"], drop_first=False)
# Criando dummies para as colunas 'Etnia' e 'Gênero'
X_dum_etnia = pd.get_dummies(X['Ethnicity'], drop_first=False)
X_dum_genero = pd.get_dummies(X['Gender'],drop_first=False)


Etnia = valores_categoricos(X_dum_etnia)

Genero = valores_categoricos(X_dum_genero)

valores_sim_nao = {
    "Não":0,
    "Sim":1
}

def run_computacional_page():
    with st.form("Inputs1"):

        # Definindo as colunas para os inputs
        var1, var2 = st.columns(2)
        x5 = var1.selectbox("Etnia:", Etnia.keys())
        x2 = var2.text_input("Qualidade da Dieta:", help="Escala: 0 a 10")

        var3, var4 = st.columns(2)
        x1 = var3.text_input("Idade:", help="Unidade: Anos")
        x3 = var4.selectbox("Gênero:", Genero.keys())



        var7, var8 = st.columns(2)
        x7 = var7.text_input("Qualidade do Sono:", help="Escala: 0 a 10")
        x8 = var8.selectbox("Histórico Familiar de Alzheimer:", valores_sim_nao.keys())
        
        var9, var10 = st.columns(2)
        x9 = var9.text_input("Colesterol Total:", help="Unidade: mg/dL")
        x10 = var10.text_input("Colesterol HDL:", help="Unidade: mg/dL")

        var11, var12 = st.columns(2)
        x11 = var11.text_input("Triglicerídeos:", help="Unidade: mg/dL")
        x12 = var12.text_input("MMSE:", help="Mini-Mental State Examination, Escala (de pior cognição a melhor): 0 a 30")

        var13, var14 = st.columns(2)
        x13 = var13.text_input("Avaliação funcional:", help=" menor valor indica maior dependência, Escala: 0 a 10")
        x14 = var14.selectbox("Queixas de memória:", valores_sim_nao.keys())

        var15, var16 = st.columns(2)
        x15 = var15.selectbox("Problemas comportamentais:", valores_sim_nao.keys())
        x16 = var16.text_input("Atividades da vida diária:", help="Escala (0 a 10) - menor valor = maior limitação")





        var5, var6 = st.columns(2)
        var5.text(" ")
        var6.text(" ")  # Placeholder

        x5_value = Etnia[x5]
        x3_value = Genero[x3]

        # Função para criar um array com os valores descompactados
        def float_values():
            try:
                return np.array([[ 
                    float(x1),
                    *x3_value[0].tolist(),
                    *x5_value[0].tolist(),
                    float(x2), 
                    float(x7),
                    valores_sim_nao[x8],   # Histórico Familiar
                    float(x9),
                    float(x10),
                    float(x11),
                    float(x12),
                    float(x13),
                    valores_sim_nao[x14],  # Queixas de memória
                    valores_sim_nao[x15],  # Problemas comportamentais
                    float(x16)
                ]])
            except ValueError:
                st.error("Por favor, insira valores numéricos válidos!")

        # Botão de submissão
        submitted = st.form_submit_button("Predict")

        if submitted:
            float_inputs = float_values()

            if len(float_inputs) > 0:
                float_inputs_list = float_values()

                clf = model()
                float_prediction = clf.predict(float_inputs_list)

                # Mensagem clara
                if float_prediction[0] == 1:
                    st.error("😢 Diagnóstico Positivo")
                else:
                    st.success("😁 Diagnóstico Negativo")

                # Armazenando o estado
                st.session_state['predict_pg1_guide1'] = True

    st.image("images/classification-report.png", use_column_width = 'auto')
    
    st.image("images/matriz-confusao.png", use_column_width = 'auto')
