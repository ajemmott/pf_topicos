#Se importan las librerias requeridas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans

#Lectura de los datos .csv
df = pd.read_csv('../_assets/pokemon-data/pokemon.csv')

#Definicion de parametroa a evaluar en kmeans
stats_estudiados = ['attack','defense','base_total']
to_delete = []

for title in list(df.columns):
    if title not in stats_estudiados:
          to_delete.append(title)

df = df.drop(columns=to_delete)

print(df.head())

#Definicion de k
kmeans = KMeans(n_clusters= 4)
kmeans.fit(df)

#Captura de datos
labels = kmeans.predict(df)
centroids = kmeans.cluster_centers_
colmap = {1:'g', 2:'c', 3:'m', 4:'y'}
colors = map(lambda x: colmap[x+1], labels)

#Definicion de gráfica
fig = plt.figure(figsize=(7,9.5))
ax = fig.add_subplot(111, projection='3d')

for idx, centroid in enumerate(centroids):
    ax.scatter(*centroid, c=colmap[idx +1])
    
ax.scatter(df['attack'], df['defense'], zs= df['base_total'], c=list(colors), alpha= 0.3)

ax.set_xlabel('Ataque')
ax.set_ylabel('Defensa')
ax.set_zlabel('Total Base')

plt.show()