# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 10:17:41 2023

@author: Ulais
"""
# importar librerias
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score


#2 cargar set de datos
data = load_breast_cancer()
#3dividdir mi entrada y salida
X = data.data
y = data.target

#4dividir los datos en entrenamiento y prueba
X_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.20, random_state=42)

#5 crear una instancia del modelo del perceptron
model = Perceptron()

#6 entrenar el modelo con el set de datos de
# entrenamiento
model.fit(X_train,y_train)

#7 predicciones a partir del set de datos de prueba
y_pred = model.predict(X_test)

#8 Calcular la precision del modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Precision: {accuracy * 100:.2f}%')