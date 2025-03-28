import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


def run_conceitos_page():
    st.title("📊 Dashboard: Análise de Alzheimer")

    df = pd.read_excel('alzheirmer_data.xlsx')

    fatores = {
        "Histórico Familiar de Alzheimer": "FamilyHistoryAlzheimers",
        "Hipertensão": "Hypertension",
        "Diabetes": "Diabetes",
        "Doença Cardiovascular": "CardiovascularDisease",
        "Depressão": "Depression",
        "Tabagismo": "Smoking"
    }

    # Mapear os valores binários 0/1 para 'Não'/'Sim' e Diagnóstico 0/1 para 'Negativo'/'Positivo'
    for col in fatores.values():
        df[col] = df[col].map({0: 'Não', 1: 'Sim'})

    df['Diagnosis'] = df['Diagnosis'].map({0: 'Negativo', 1: 'Positivo'})#, 'Negativo': 'Negativo', 'Positivo': 'Positivo'})

    st.subheader("Análise Dinâmica de Fatores de Risco")

    fator_escolhido = st.selectbox(
        "Selecione o fator que deseja analisar em relação ao diagnóstico de Alzheimer:",
        list(fatores.keys()),
        key="fator_diagnostico_pizza"
    )

    if fator_escolhido:
        coluna = fatores[fator_escolhido]
        crosstab_result = pd.crosstab(df[coluna], df['Diagnosis'])


    # Ordem fixa: Azul escuro -> Azul claro -> Laranja escuro -> Laranja claro
    order = [
        ('Não', 'Negativo'),  # Azul escuro
        ('Sim', 'Negativo'),  # Azul claro
        ('Não', 'Positivo'),  # Laranja escuro
        ('Sim', 'Positivo')   # Laranja claro
    ]

    cores_plotly = ['#104E8B', '#63B8FF', '#FF7F50', '#FFA07A']

    plot_data = []
    for idx, (fator_valor, diag_valor) in enumerate(order):
        if fator_valor in crosstab_result.index and diag_valor in crosstab_result.columns:
            contagem = crosstab_result.at[fator_valor, diag_valor]
            plot_data.append({
                "Categoria": f"{'Sem Fator' if fator_valor == 'Não' else 'Com Fator'} | {'Negativo' if diag_valor == 'Negativo' else 'Positivo'}",
                "Contagem": contagem,
                "Cor": cores_plotly[idx]
            })

    df_plot = pd.DataFrame(plot_data)

    # Gráfico com Plotly Express
    fig = px.pie(
        df_plot,
        names='Categoria',
        values='Contagem',
        color='Categoria',
        color_discrete_sequence=cores_plotly,
        title=f"{fator_escolhido} vs Diagnóstico de Alzheimer"
    )

    fig.update_traces(
        textinfo='percent+label',
        textfont_size=12,
        pull=[0.03] * len(df_plot),
        sort=False  # Importante: manter a ordem manual (azul-azul-laranja-laranja)
    )

    fig.update_layout(title="Distribuição de Diagnósticos com e sem Fator")
    st.plotly_chart(fig, use_container_width=True)

    with st.expander("Ver dados da tabela"):
        st.dataframe(crosstab_result)
    
    st.subheader("📊 Diagnóstico de Alzheimer por Etnia")

    # Carregar dados
    df = pd.read_excel('alzheirmer_data.xlsx')

    # Filtrar apenas colunas necessárias
    df_hist = df[['Ethnicity', 'Diagnosis']]

    # Ajuste para garantir que o Diagnóstico está como string
    df_hist['Diagnosis'] = df_hist['Diagnosis'].map({0: 'Negativo', 1: 'Positivo', 'Negativo': 'Negativo', 'Positivo': 'Positivo'})

    # Gráfico de histograma com Plotly
    fig = px.histogram(
        df_hist,
        x='Ethnicity',
        color='Diagnosis',
        barmode='group',
        color_discrete_map={'Negativo': '#104E8B', 'Positivo': '#FF7F50'},
        title="Distribuição de Etnia por Diagnóstico de Alzheimer"
    )

    fig.update_layout(
        xaxis_title="Etnia",
        yaxis_title="Número de Pacientes",
        bargap=0.2,
        width=700,
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📊 Distribuição da Idade por Diagnóstico de Alzheimer")

    # Carregar os dados
    df = pd.read_excel('alzheirmer_data.xlsx')

    # Garantir que Diagnóstico está bem formatado
    df['Diagnosis'] = df['Diagnosis'].map({0: 'Negativo', 1: 'Positivo'})#, 'Negativo': 'Negativo', 'Positivo': 'Positivo'})

    # Histograma com Plotly
    fig = px.histogram(
        df,
        x='Age',
        color='Diagnosis',
        barmode='overlay',  # Barras sobrepostas para comparar
        color_discrete_map={'Negativo': '#104E8B', 'Positivo': '#FF7F50'},
        title="Distribuição da Idade por Diagnóstico de Alzheimer",
        nbins=20  # Número de bins (ajustável)
    )

    fig.update_traces(opacity=1)  # Deixar as sobreposições mais visíveis
    fig.update_layout(
        xaxis_title="Idade",
        yaxis_title="Número de Pacientes",
        width=700,
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)


