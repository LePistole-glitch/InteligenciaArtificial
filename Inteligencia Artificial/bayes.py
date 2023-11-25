#Importamos librerias
#from google.colab import drive
import pandas as pd
import matplotlib.pyplot as plt
import numpy
from matplotlib import color_sequences
import seaborn as sb
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB
from sklearn.feature_selection import SelectKBest


dataframe = pd.read_csv(r"comprar_alquilar.csv")
dataframe.head(10)

print(dataframe)

print(dataframe.groupby('comprar').size())
dataframe.drop(['comprar'], axis=1).hist()
plt.show()

dataframe['gastos']=(dataframe['gastos_comunes']+dataframe['gastos_otros']+dataframe['pago_coche'])
dataframe['financiar']=dataframe['vivienda']-dataframe['ahorros']
dataframe.drop(['gastos_comunes', 'gastos_otros', 'pago_coche'], axis=1).head(10)

reduced = dataframe.drop(['gastos_comunes','gastos_otros','pago_coche'], axis=1)
reduced.describe()

X = dataframe.drop(['comprar'], axis=1) #entrada
y = dataframe['comprar'] #salida

best = SelectKBest(k=5)
X_new = best.fit_transform(X, y)
X_new.shape
selected = best.get_support(indices=True)
print(X.columns[selected])

used_features = X.columns[selected]
colormap = plt.cm.viridis
plt.figure(figsize=(12, 12))
plt.title('Person Correlation of Features', y=1.85, size=15)
sb.heatmap(dataframe[used_features].astype(float).corr(),linewidths=0.1,vmax=1.0, square=True, cmap=colormap, linecolor='white', annot=True)

