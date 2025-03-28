import streamlit as st
from streamlit_option_menu import option_menu
import plotly.graph_objects as go
from io import BytesIO
import base64
import pandas as pd
import numpy as np

def run_aplicacoes_page():


    # Seção: Implementação Computacional e Aplicações
    st.title("Implementação Computacional e Aplicações")

    st.markdown(r"""
    Nesta seção, abordamos a modelagem e a solução de Problemas de Otimização Multiobjetivo utilizando os métodos da soma ponderada e $\epsilon$-restrito. Desenvolvemos códigos específicos para cada um dos métodos, além de algoritmos que permitem a variação dos parâmetros de cada técnica. Para mais detalhes sobre o funcionamento de cada código, consulte o capítulo 
    [Códigos](https://github.com/matheusic2023/Iniciacao_cientifica/tree/main/Algoritmos%20Oficiais).
    """, unsafe_allow_html=True)

    # Subseção: Problema do Transporte
    st.header("Problema do Transporte")
    st.markdown(r"""
    Na cidade de Campinas, uma empresa possui dois armazéns (Armazéns 1 e 2) responsáveis pelo transporte de produtos alimentícios para três mercados locais (Mercados A, B e C). O objetivo da empresa é minimizar os custos de transporte até os mercados, enquanto busca emitir a menor quantidade possível de CO2. Este exemplo reflete a necessidade de equilibrar eficiência logística e questões ambientais.
    """, unsafe_allow_html=True)

    st.subheader("Variáveis de Decisão")
    st.markdown(r"""
    As variáveis de decisão representam a quantidade de mercadorias transportadas de cada armazém para os mercados:

    """)
    st.latex(r"""
    \begin{align*}
    x_{1A} &: \text{quantidade de mercadorias transportadas do Armazém 1 para o Mercado A} \\
    x_{1B} &: \text{quantidade de mercadorias transportadas do Armazém 1 para o Mercado B} \\
    x_{1C} &: \text{quantidade de mercadorias transportadas do Armazém 1 para o Mercado C} \\
    x_{2A} &: \text{quantidade de mercadorias transportadas do Armazém 2 para o Mercado A} \\
    x_{2B} &: \text{quantidade de mercadorias transportadas do Armazém 2 para o Mercado B} \\
    x_{2C} &: \text{quantidade de mercadorias transportadas do Armazém 2 para o Mercado C} \\
    \end{align*}
    """)

    st.subheader("Funções Objetivo")
    st.markdown(r"""
    As funções objetivo incluem:

    1. **Minimizar o custo de transporte:** $z_1(x)$, representado pela equação:
    """)
    st.latex(r"""
    \min \, z_1(x) = 2x_{1A} + 4x_{1B} + 5x_{1C} + 3x_{2A} + 1x_{2B} + 2x_{2C} \quad \text{(Custo de transporte em R\$)}
    """)
    st.markdown("2. **Minimizar a emissão de CO2:** $z_2(x)$, representado pela equação:")
    st.latex(r"""
    \min \, z_2(x) = 9x_{1A} + 4x_{1B} + x_{1C} + 2x_{2A} + 5x_{2B} + 8x_{2C} \quad \text{(Emissão de CO2)}
    """)

    st.subheader("Restrições")
    st.markdown("As restrições do problema são as seguintes:")
    st.markdown(r"""
    * **Capacidade de armazenamento:** A quantidade total de produtos transportados de cada armazém para os mercados não pode exceder a capacidade do armazém:
    """)
    st.latex(r"""
    \begin{align*}
    x_{1A} + x_{1B} + x_{1C} &\leq 100 \quad \text{(Capacidade do Armazém 1)} \\
    x_{2A} + x_{2B} + x_{2C} &\leq 150 \quad \text{(Capacidade do Armazém 2)}
    \end{align*}
    """)

    st.markdown(r"""
    * **Demanda mínima:** Cada mercado possui uma demanda mínima que deve ser atendida:
    """)
    st.latex(r"""
    \begin{align*}
    x_{1A} + x_{2A} &\geq 80 \quad \text{(Demanda do Mercado A)} \\
    x_{1B} + x_{2B} &\geq 70 \quad \text{(Demanda do Mercado B)} \\
    x_{1C} + x_{2C} &\geq 100 \quad \text{(Demanda do Mercado C)}    
    \end{align*}
    """)

    st.subheader("Solução")
    st.markdown(r"""
    Aplicando o método do $\varepsilon$-restrito, variamos o valor de $\varepsilon$ no intervalo $[-500, 500]$ em mil passos, utilizando o algoritmo `percorrer_epsilon()`. Considerando a função custo como restrição ($z_1(x) \geq \varepsilon$) e aplicando o método do $\varepsilon$-restrito, obtivemos a mesma solução do problema ponderado, testado no algoritmo `varrer_lambda()` com mil passos.
    """, unsafe_allow_html=True)
    
    st.image('images/ex_min_min.png')
    st.markdown(r"""
    Neste exemplo, ao reduzir o custo de transporte, a quantidade de CO2 emitida aumenta. No entanto, no canto superior esquerdo do gráfico, uma das soluções obtidas pelo método da soma ponderada ($s_1(x) = (490; 1850)$) apresenta o mesmo custo que outra solução ($s_2(x) = (490; 1730)$), mas com maior emissão de CO2. Isso caracteriza $s_1(x)$ como uma solução fracamente eficiente.
    """, unsafe_allow_html=True)
    st.markdown("---")
    # Subseção: Emissão de CO2 e Lucro em Setores de Produção
    st.header("Emissão de CO2 e Lucro em Setores de Produção")
    st.markdown(r"""
    Uma empresa produz seis produtos $P_1$, $P_2$, $P_3$, $P_4$, $P_5$ e $P_6$, onde cada produto gera lucro e emite uma quantidade específica de CO2. O objetivo é determinar as quantidades de produção que maximizem o lucro e minimizem as emissões de CO2.
    """, unsafe_allow_html=True)

    st.subheader("Variáveis de Decisão")
    st.latex(r"""
    \begin{align*}
    x_1 &: \text{quantidade de } P_1 \text{ a ser produzida} \\
    x_2 &: \text{quantidade de } P_2 \text{ a ser produzida} \\
    x_3 &: \text{quantidade de } P_3 \text{ a ser produzida} \\
    x_4 &: \text{quantidade de } P_4 \text{ a ser produzida} \\
    x_5 &: \text{quantidade de } P_5 \text{ a ser produzida} \\
    x_6 &: \text{quantidade de } P_6 \text{ a ser produzida} \\
    \end{align*}
    """)

    st.subheader("Funções Objetivo")
    st.markdown(r"""
    As funções objetivo são:

    1. **Maximizar o lucro:** $z_1(x)$, representado pela equação:
    """)
    st.latex(r"""
    \max \, z_1(x) = 15x_1 + 20x_2 + 25x_3 + 30x_4 + 22x_5 + 18x_6 \quad \text{(Lucro em R\$)}
    """)
    st.markdown("2. **Minimizar a emissão de CO2:** $z_2(x)$, representado pela equação:")
    st.latex(r"""
    \min \, z_2(x) = 12x_1 + 10x_2 + 18x_3 + 22x_4 + 14x_5 + 16x_6 \quad \text{(Emissão de CO2 em kg)}
    """)

    st.subheader("Restrições")
    st.markdown(r"""
    As restrições incluem:

    * **Orçamento:** O custo total de produção não deve exceder o orçamento disponível:
    """)
    st.latex(r"""
    50x_1 + 70x_2 + 60x_3 + 80x_4 + 65x_5 + 55x_6 \leq 15,000 
    """)

    st.markdown(r"""
    * **Horas de trabalho:** O total de horas de trabalho necessárias para a produção não deve exceder as horas disponíveis:
    """)
    st.latex(r"""
    2x_1 + 3x_2 + 1x_3 + 4x_4 + 2.5x_5 + 1.5x_6 \leq 2,000 
    """)

    st.markdown(r"""
    * **Demanda mínima:** Cada produto deve atender a uma demanda mínima de mercado:
    """)
    st.latex(r"""
    x_i \geq 10 \quad \text{para } i = 1, \ldots, 6 
    """)

    st.subheader("Modelo Matemático Multiobjetivo")
    st.latex(r"""
    \begin{aligned}
    \max \,  z_1(x)& = 15x_1 + 20x_2 + 25x_3 + 30x_4 + 22x_5 + 18x_6 \\
    \min  \, z_2(x)&  = 12x_1 + 10x_2 + 18x_3 + 22x_4 + 14x_5 + 16x_6 \\
    \text{s.a:} 
    & \begin{cases}
    50x_1 + 70x_2 + 60x_3 + 80x_4 + 65x_5 + 55x_6 \leq 15,000 \\
    2x_1 + 3x_2 + 1x_3 + 4x_4 + 2.5x_5 + 1.5x_6 \leq 2,000 \\
    x_i \geq 10  \quad \text{para } i = 1, \ldots, 6 \\
    x_i \geq 0  \quad \text{para } i = 1, \ldots, 6
    \end{cases}
    \end{aligned}
    """)

    st.subheader("Solução")
    st.markdown(r"""
    Por meio dos métodos do $\varepsilon$-restrito e soma ponderada, obtemos a seguinte fronteira de Pareto:
    """)
    st.image('images/exemplo_co2.png')

    st.markdown(r"""
    Os resultados mostram que ao aumentar o lucro, a empresa inevitavelmente aumenta a emissão de CO2. Isso ocorre porque a maximização do lucro requer um aumento na produção, o que leva a maiores emissões de CO2.
    """, unsafe_allow_html=True)
    st.markdown("---")
    # Subseção: Problema da Dieta
    st.header("Problema da Dieta")
    st.markdown(r"""
    O objetivo deste modelo é obter uma dieta que minimize o custo diário de alimentos e maximize a quantidade de proteínas ingeridas. Para resolver esse problema, selecionamos uma lista de alimentos, suas informações nutricionais e a dose diária recomendada de nutrientes.
    """, unsafe_allow_html=True)

    st.markdown("**(Aqui vai a imagem 3: Tabela com os valores nutricionais dos alimentos.)**")

    st.subheader("Modelo Matemático Multiobjetivo")
    st.latex(r"""
    \begin{aligned}
        \min \, f_1(x) &= 0.8x_1 +0.9x_2 +2.7x_3 +4x_4 +6.5x_5 +2.8x_6 \quad (\text{Custo})\\
        \max \, f_2(x) &= 3x_1 +5x_2 +32x_3 +32x_4 +15x_5 +14x_6 \quad (\text{Proteína}) \\
        \text{s.a.} \quad &  
        \begin{cases}
        1800 \leq 216x_1 + 164x_2 +456x_3+ 516x_4+ 176x_5 +670x_6 \leq 2500 \quad (\text{Kcal}) \\
        100 \leq 28x_1 + 14x_2 + 0x_3+ 0x_4+5x_5 +0x_6 \leq 150 \quad (\text{Carboidrato})\\
        25 \leq 2x_1 + 8x_2 + 0x_3+ 0x_4+ 0x_5+ 0x_6 \leq 36 \quad (\text{Fibra}) \\
        1300 \leq 166x_1 + 167x_2 + 205x_3+ 209x_4+ 236x_5+ 228x_6 \leq 2300 \quad (\text{Sódio}) \\
        22 \leq 2x_1 + 2x_2 + 8x_3+ 12x_4+ 8x_5+ 13x_6 \leq 29 \quad (\text{Gordura Saturada}) \\
        x_i \geq 10 \quad \text{para } i = 1, \ldots, 6
        \end{cases}       
    \end{aligned}
    """)

    st.subheader("Solução")
    st.markdown(r"""
    Ao adaptar o modelo ao método da soma ponderada e ao $\varepsilon$-restrito, considerando a função de proteínas como uma restrição, obtemos os seguintes resultados:
    """)

    st.image('images/exemplo_dieta.png')
    
    st.markdown(r"""
    O resultado mostra que aumentar a quantidade de proteínas diárias inevitavelmente eleva o custo da refeição. As escolhas alimentares refletem um equilíbrio entre custo e quantidade de proteína, conforme as soluções apresentadas na tabela abaixo.
    """, unsafe_allow_html=True)
    

    # Melhorias na apresentação geral
    st.markdown("---")
   