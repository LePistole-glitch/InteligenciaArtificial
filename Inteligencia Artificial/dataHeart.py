import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"HeartDisease.csv") #Leer el archivo que tengo
#df = pd.read_csv(r"C:\Users\chave\OneDrive\Escritorio\9no Semestre\Inteligencia Artificial\archive\pokemons.csv")
print(df.columns) #Imprimir la forma del cs ---- > dataFrame
#(462, 5) ---> (registro, atributos)
#Como acceder a una sola columna de mi dataframe 
imc = df['obesity']
corona = df['chd']
presion = df['sbp']

#plt.scatter(range(len(corona)), presion)
# agregar etiquetas al eje X e Y
#plt.xlabel('SBP')
#plt.ylabel('Numero de instancias o registros')
# agregar un titulo al grafico
#plt.show()
#df.plot.scatter(x = 'chd', y = 'sbp', s='obesity', c='red')
print(df.info())
print(df['obesity'].mean())
print(df['age'].mean())
print(df['sbp'].mean())
#sns.countplot(x="age",hue="famhist",data=df)
#grafica de barras con matplotlib
plt.bar(df['famhist'], df['famhist'] )
plt.xlabel(' ')
plt.ylabel(' ')
plt.show()

plt.pie(df['famhist'], labels= df['age'])
plt.show()