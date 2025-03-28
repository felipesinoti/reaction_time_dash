import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_absolute_error
import numpy as np
import pickle

def model():
    return pickle.load(open('ml_trained_model2.sav', 'rb'))

def dataframe():
    return pd.read_excel("alzheirmer_data.xlsx")

def train_model():
    # Preparando o dataset

    df = dataframe()

    # Removendo colunas não úteis para a previsão como PatientID e DoctorInCharge
    df.drop(['PatientID', 'DoctorInCharge'], axis=1, inplace=True)
    escolaridade_ordem = [
        "Não Possui",
        "Ensino Médio",
        "Graduação",
        "Pós-graduação"
    ]

    X = df.iloc[:,0:32]

    # Converte a coluna EducationLevel usando pd.Categorical
    X['EducationLevel'] = pd.Categorical(X['EducationLevel'], categories=escolaridade_ordem, ordered=True)
    X['EducationLevel'] = X['EducationLevel'].cat.codes
    X = pd.get_dummies(X, columns=['Ethnicity',"Gender"], drop_first=False)
    y = df.iloc[:,32]
    modelo = RandomForestClassifier(n_estimators=100, random_state=0)
    modelo.fit(X, y)
    pickle.dump(modelo, open('ml_trained_model.sav', 'wb'))
    new_model = open('ml_trained_model.sav', 'rb')
    return X,y,new_model

def train_model2():
    data = pd.read_excel("alzheirmer_data - Copia.xlsx")
    df = data.copy()
    X = df.iloc[:,0:14]
    X = pd.get_dummies(X,columns=['Ethnicity',"Gender"], drop_first=False)
    y = df.iloc[:,14]
    modelo = RandomForestClassifier(n_estimators=100, random_state=0)
    modelo.fit(X, y)
    pickle.dump(modelo, open('ml_trained_model2.sav', 'wb'))
    new_model = open('ml_trained_model2.sav', 'rb')
    return X,y,new_model

X, y, new_model    = train_model()
X2, y2, new_model2 = train_model2()