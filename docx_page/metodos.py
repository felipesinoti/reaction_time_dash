import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

def run_metodos_page():
    st.title("📄 Base de Dados de Pacientes")

    # Carregar a base de dados
    df = pd.read_excel('alzheirmer_data.xlsx')

    # Dicionário para traduzir colunas
    colunas_traduzidas = {
        "PatientID": "ID do Paciente",
        "Age": "Idade",
        "Gender": "Gênero",
        "Ethnicity": "Etnia",
        "EducationLevel": "Escolaridade",
        "BMI": "IMC",
        "Smoking": "Tabagismo",
        "AlcoholConsumption": "Consumo de Álcool (semanal)",
        "PhysicalActivity": "Atividade Física (horas/semana)",
        "DietQuality": "Qualidade da Dieta",
        "SleepQuality": "Qualidade do Sono",
        "FamilyHistoryAlzheimers": "Histórico Familiar de Alzheimer",
        "CardiovascularDisease": "Doença Cardiovascular",
        "Diabetes": "Diabetes",
        "Depression": "Depressão",
        "HeadInjury": "Lesão na Cabeça",
        "Hypertension": "Hipertensão",
        "SystolicBP": "Pressão Sistólica (mmHg)",
        "DiastolicBP": "Pressão Diastólica (mmHg)",
        "CholesterolTotal": "Colesterol Total (mg/dL)",
        "CholesterolLDL": "Colesterol LDL (mg/dL)",
        "CholesterolHDL": "Colesterol HDL (mg/dL)",
        "CholesterolTriglycerides": "Triglicerídeos (mg/dL)",
        "MMSE": "Mini-Mental State Exam (MMSE)",
        "FunctionalAssessment": "Avaliação Funcional",
        "MemoryComplaints": "Queixas de Memória",
        "BehavioralProblems": "Problemas Comportamentais",
        "ADL": "Atividades da Vida Diária (ADL)",
        "Confusion": "Confusão",
        "Disorientation": "Desorientação",
        "PersonalityChanges": "Mudanças de Personalidade",
        "DifficultyCompletingTasks": "Dificuldade em Tarefas",
        "Forgetfulness": "Esquecimento",
        "Diagnosis": "Diagnóstico de Alzheimer",
        "DoctorInCharge": "Médico Responsável"
    }

    # Renomear colunas
    df.rename(columns=colunas_traduzidas, inplace=True)

    # Exibir DataFrame
    st.subheader("Visualização da Base de Dados (PT-BR)")
    st.dataframe(df)

    st.title("🔗 Matriz de Correlação com Diagnóstico de Alzheimer")

    # Carregar os dados
    df = pd.read_excel('alzheirmer_data.xlsx')

    # Seleção das variáveis
    df_corr = df[['BMI', 'AlcoholConsumption', 'Smoking', 'Ethnicity', 'Diagnosis']]

    # Aplicar One-Hot Encoding
    df_encoded = pd.get_dummies(df_corr, columns=['Smoking', 'Ethnicity'], drop_first=False)

    # Mapear Diagnóstico
    # df_encoded['Diagnosis'] = df_encoded['Diagnosis'].map({'Negativo': 0, 'Positivo': 1})
    df_encoded = df_encoded.drop(columns={'Smoking_0'})

    # Calcular correlação
    correlation = df_encoded.corr()

    # Criar máscara da diagonal principal
    mask = np.eye(len(correlation), dtype=bool)

    # Criar máscara adicional para remover correlação entre dummy exclusivas
    dummy_pairs = [
        ('Smoking_Não', 'Smoking_Sim'),
        ('Ethnicity_Caucasiano', 'Ethnicity_Afro-americano'),
        ('Ethnicity_Caucasiano', 'Ethnicity_Asiático'),
        ('Ethnicity_Caucasiano', 'Ethnicity_Outra'),
        ('Ethnicity_Afro-americano', 'Ethnicity_Asiático'),
        ('Ethnicity_Afro-americano', 'Ethnicity_Outra'),
        ('Ethnicity_Asiático', 'Ethnicity_Outra'),
        ('Ethnicity_Asiático', 'Ethnicity_Caucasiano'),
        ('Ethnicity_Outra', 'Ethnicity_Caucasiano'),
        ('Smoking_0', 'Smoking_1'),
        ('Smoking_1', 'Smoking_0')
    ]

    # Adicionando essas posições à máscara
    for (var1, var2) in dummy_pairs:
        if var1 in correlation.columns and var2 in correlation.columns:
            i = correlation.columns.get_loc(var1)
            j = correlation.columns.get_loc(var2)
            mask[i, j] = True
            mask[j, i] = True
    
    st.subheader("Correlação entre variáveis e Diagnóstico de Alzheimer")

    st.image("images/matriz_corr.png", use_column_width = 'auto')

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(
        correlation,
        mask=mask,
        annot=True,
        cmap='coolwarm',
        fmt=".2f",
        cbar=True,
        linewidths=0.5,
        ax=ax
    )

    # Inserir "-" na diagonal e nas dummy exclusivas
    for i in range(len(correlation)):
        ax.text(i + 0.5, i + 0.5, "-", color='gray', ha='center', va='center', fontsize=10, fontweight='bold')
    for (var1, var2) in dummy_pairs:
        if var1 in correlation.columns and var2 in correlation.columns:
            i = correlation.columns.get_loc(var1)
            j = correlation.columns.get_loc(var2)
            ax.text(j + 0.5, i + 0.5, "-", color='gray', ha='center', va='center', fontsize=10, fontweight='bold')
            ax.text(i + 0.5, j + 0.5, "-", color='gray', ha='center', va='center', fontsize=10, fontweight='bold')

    ax.set_title('Matriz de Correlação (One-Hot com exclusões)', fontsize=10)
    st.pyplot(fig)

    with st.expander("Ver dataframe com One-Hot Encoding"):
        st.dataframe(df_encoded)