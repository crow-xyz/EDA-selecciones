import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Lee archivo csv
df = pd.read_csv('results.csv')

# Información
print(df.head())
print("-----------------------------------------------------------------------")
print(df.shape)
print("-----------------------------------------------------------------------")
print(df.info())
print("-----------------------------------------------------------------------")
print(df.describe())

# Contar las victorias por equipo local
victorias_por_equipo = df[df['home_score'] > df['away_score']]['home_team'].value_counts()

# Tomar solo los 20 selecciones con más victorias
top_20_selecciones = victorias_por_equipo[:20]

# Crear una columna para el resultado (ganar, perder o empatar)
df['Resultado'] = df.apply(lambda row: 'Empate' if row['home_score'] == row['away_score']
                           else 'Victoria Local' if row['home_score'] > row['away_score']
                           else 'Victoria Visitante', axis=1)

# Calcula la suma de goles totales por partido
df['Total_Goles'] = df['home_score'] + df['away_score']
max_goles = df['Total_Goles'].max()

# Crear subplots
fig, plots = plt.subplots(2, 2, figsize=(16, 12))

# Gráfico de barras de los top 20 selecciones con más victorias
top_20_selecciones.plot(kind='bar', ax=plots[0, 0])
plots[0, 0].set_xlabel('')
plots[0, 0].set_ylabel('Cantidad de victorias')
plots[0, 0].set_title('Top 20 selecciones con más victorias')

# Gráfico de dispersión de goles entre selecciones locales y visitantes
sns.scatterplot(x='home_score', y='away_score', hue='Resultado', data=df, ax=plots[0, 1])
plots[0, 1].set_xlabel('Goles equipo local')
plots[0, 1].set_ylabel('Goles equipo visitante')
plots[0, 1].set_title('Relación entre goles y resultados')

# Histograma de la distribución de goles totales por partido
histogram = plots[1, 0].hist(df['Total_Goles'], bins=max_goles, color='skyblue', edgecolor='black')
plots[1, 0].set_xticks([i + 0.5 for i in range(max_goles)])  
plots[1, 0].set_xticklabels(range(1, max_goles+1))
plots[1, 0].set_xlabel('Goles totales')
plots[1, 0].set_ylabel('Frecuencia')
plots[1, 0].set_title('Distribución de goles totales por partido')

# Anotaciones en cada columna para dar informacion mas detallada
max_height = plots[1, 0].get_ylim()[1] * 0.85  # 95% de la altura maxima para que no sobrepase el borde
for bar, freq in zip(histogram[2], histogram[0]):
    height = min(bar.get_height(), max_height)
    plots[1, 0].annotate('{}'.format(int(freq)),  # Convert to integer
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom', rotation=90, clip_on=True)

# Eliminar el subplot vacío
fig.delaxes(plots[1, 1])

# Ajustar el espacio vertical entre los subplots
plt.subplots_adjust(hspace=0.5)

# Mostrar los subplots
plt.tight_layout()
plt.show()