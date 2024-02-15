import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Lee archivo csv
df = pd.read_csv('results.csv')

#Información
print(df.head())
print("-----------------------------------------------------------------------")
print(df.shape)
print("-----------------------------------------------------------------------")
print(df.info())
print("-----------------------------------------------------------------------")
print(df.describe())

#Contar las victorias por equipo local
victorias_por_equipo = df[df['home_score'] > df['away_score']]['home_team'].value_counts()

#Tomar solo los 20 equipos con más victorias
top_20_equipos = victorias_por_equipo[:20]

#Gráfico de barras
plt.figure(figsize=(12, 6))
top_20_equipos.plot(kind='bar')
plt.xlabel('Equipo')
plt.ylabel('Cantidad de Victorias')
plt.title('Top 20 Equipos con Más Victorias')
plt.show()

#Crear una columna para el resultado (ganar, perder o empatar)
df['Resultado'] = df.apply(lambda row: 'Empate' if row['home_score'] == row['away_score']
                           else 'Victoria Local' if row['home_score'] > row['away_score']
                           else 'Victoria Visitante', axis=1)

#Gráfico de dispersión
plt.figure(figsize=(10, 6))
sns.scatterplot(x='home_score', y='away_score', hue='Resultado', data=df)
plt.xlabel('Goles Equipo Local')
plt.ylabel('Goles Equipo Visitante')
plt.title('Relación entre Goles y Resultados')
plt.show()