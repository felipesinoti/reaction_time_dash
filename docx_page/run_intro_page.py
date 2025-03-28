import streamlit as st
from streamlit_option_menu import option_menu
import streamlit as st
import plotly.graph_objects as go
from io import BytesIO
import base64
import pandas as pd
def run_intro_page():
    st.title("Introdução:")

    st.subheader('O que é este conjunto de dados?')
    st.write('Este conjunto de dados contém informações abrangentes de saúde de 2.149 pacientes, identificados de forma única por IDs que variam de 4751 a 6900. '
            'Inclui dados demográficos, fatores de estilo de vida, histórico médico, medições clínicas, avaliações cognitivas e funcionais, sintomas e diagnóstico da Doença de Alzheimer. '
            'É ideal para pesquisadores e cientistas de dados interessados em explorar fatores associados ao Alzheimer, desenvolver modelos preditivos e realizar análises estatísticas.')

    st.subheader('Quais são os tópicos abordados neste conjunto de dados?')
    st.markdown("<strong>1. Informações do Paciente:</strong> Inclui o ID do paciente e dados demográficos, como idade, gênero e etnia.", unsafe_allow_html=True)
    st.markdown("<strong>2. Fatores de Estilo de Vida:</strong> Informações sobre IMC, tabagismo, consumo de álcool, atividade física, qualidade da dieta e do sono.", unsafe_allow_html=True)
    st.markdown("<strong>3. Histórico Médico:</strong> Dados sobre doenças cardiovasculares, diabetes, depressão, histórico familiar de Alzheimer, entre outros.", unsafe_allow_html=True)
    st.markdown("<strong>4. Medições Clínicas:</strong> Pressão arterial, colesterol total, LDL, HDL, triglicerídeos, entre outros.", unsafe_allow_html=True)
    st.markdown("<strong>5. Avaliações Cognitivas e Funcionais:</strong> Pontuações de exames cognitivos e funcionais, como MMSE e ADL.", unsafe_allow_html=True)
    st.markdown("<strong>6. Sintomas:</strong> Presença de sintomas como confusão, desorientação, alterações de personalidade, entre outros.", unsafe_allow_html=True)
    st.markdown("<strong>7. Diagnóstico:</strong> Diagnóstico da Doença de Alzheimer.", unsafe_allow_html=True)
    st.markdown("<strong>8. Informação Confidencial:</strong> Dados sobre o médico responsável (anônimos).", unsafe_allow_html=True)

    st.title("Informações Detalhadas:")

    st.subheader("1) Informações do Paciente:")
    st.write("• ID do Paciente: Identificador único de cada paciente (4751 a 6900).")
    st.write("• Idade: Entre 60 e 90 anos.")
    st.write("• Gênero: 0 = Masculino | 1 = Feminino.")
    st.write("• Etnia: 0 = Caucasiano | 1 = Afro-Americano | 2 = Asiático | 3 = Outro.")
    st.write("• Escolaridade: 0 = Nenhuma | 1 = Ensino Médio | 2 = Bacharelado | 3 = Pós-graduação.")

    st.subheader("2) Fatores de Estilo de Vida:")
    st.write("• IMC: Índice de Massa Corporal entre 15 e 40.")
    st.write("• Tabagismo: 0 = Não | 1 = Sim.")
    st.write("• Consumo de Álcool: De 0 a 20 unidades por semana.")
    st.write("• Atividade Física: De 0 a 10 horas semanais.")
    st.write("• Qualidade da Dieta: Escore de 0 a 10.")
    st.write("• Qualidade do Sono: Escore de 4 a 10.")

    st.subheader("3) Histórico Médico:")
    st.write("• Histórico Familiar de Alzheimer, Doença Cardiovascular, Diabetes, Depressão, Lesão na Cabeça e Hipertensão: 0 = Não | 1 = Sim.")

    st.subheader("4) Medições Clínicas:")
    st.write("• Pressão Sistólica: 90 a 180 mmHg.")
    st.write("• Pressão Diastólica: 60 a 120 mmHg.")
    st.write("• Colesterol Total: 150 a 300 mg/dL.")
    st.write("• LDL: 50 a 200 mg/dL.")
    st.write("• HDL: 20 a 100 mg/dL.")
    st.write("• Triglicerídeos: 50 a 400 mg/dL.")

    st.subheader("5) Avaliações Cognitivas e Funcionais:")
    st.write("• MMSE: Pontuação de 0 a 30 (quanto menor, maior o comprometimento cognitivo).")
    st.write("• Avaliação Funcional: De 0 a 10 (quanto menor, maior o comprometimento).")
    st.write("• Queixas de Memória e Problemas Comportamentais: 0 = Não | 1 = Sim.")
    st.write("• ADL (Atividades da Vida Diária): De 0 a 10 (quanto menor, maior a dificuldade).")

    st.subheader("6) Sintomas:")
    st.write("• Confusão, Desorientação, Alterações de Personalidade, Dificuldade em Completar Tarefas, Esquecimento: 0 = Não | 1 = Sim.")

    st.subheader("7) Diagnóstico:")
    st.write("• Diagnóstico de Alzheimer: 0 = Não | 1 = Sim.")

    st.subheader("8) Informação Confidencial:")
    st.write("• Médico Responsável: Informação confidencial representada por 'XXXConfid'.")
   



