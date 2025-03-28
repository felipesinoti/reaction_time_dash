import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_absolute_error
import numpy as np


def return_values(Matriz):
    linha = Matriz.shape[0]
    coluna = Matriz.shape[1]
    Matriz_aux = np.zeros([linha,coluna])
    lista = []
    for i in range(linha):
        for j in range(coluna):
            Matriz_aux[i,j] = Matriz[i,j]
            lista.append(Matriz[i,j])
    lista = np.array(lista)

    return lista

# va_dummy seria a 'dummização' de uma variável categórica, por exemplo, marca: X_dum_marcas = pd.get_dummies(X['Marca'])
def valores_categoricos(va_dummy):

    # Dicionário com as variáveis categóricas
    dicionario = dict( zip(va_dummy.columns,np.zeros(va_dummy.columns.size)))

    # Atribuição dos Valores
    for marca in dicionario:
        dicionario[marca] = va_dummy[va_dummy[marca] == True].head(1).values
    return dicionario