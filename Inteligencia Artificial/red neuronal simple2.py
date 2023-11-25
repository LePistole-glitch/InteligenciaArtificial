# importar librerias
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score

# cargar set de datos desde un archivo CSV
df = pd.read_csv('pokemons.csv')

# separar las características (X) y el objetivo (y)
features = ['hp/atk/def', 'spatk/spdef', 'L/M']
target = 'strenght'

X = df[features]
y = df[target]

# Convert categorical variables to numerical using one-hot encoding
X = pd.get_dummies(X)

# dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# crear una instancia del modelo Perceptron
model = Perceptron()

# entrenar el modelo con el set de datos de entrenamiento
model.fit(X_train, y_train)

# hacer predicciones a partir del set de datos de prueba
y_pred = model.predict(X_test)

# calcular la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Precisión: {accuracy * 100:.2f}%')
