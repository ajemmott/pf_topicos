#importar librerias

import pandas as pd
import numpy as np

from sklearn.cluster import KMeans

import plotly
import plotly.graph_objects as go
import plotly.io as pio
from plotly.subplots import make_subplots

raw_df = pd.read_csv('../_assets/pokemon-data/pokemon.csv')

#Definicion de parametroa a evaluar en kmeans
stats_estudiados = ['attack','defense','base_total','sp_defense','sp_attack','speed','hp']
to_delete = []

for title in list(raw_df.columns):
    if title not in stats_estudiados:
          to_delete.append(title)

df = pd.read_csv('../_assets/pokemon-data/stats_normal.csv', sep= ';')

#Definicion de k
kmeans = KMeans(n_clusters= 3, random_state=25)
kmeans.fit(df)

#Captura de datos
np.random.seed(0)
labels = kmeans.predict(df)
centroids = kmeans.cluster_centers_
markermap = {0:'circle',1:'x'}

markers = map(lambda x: markermap[x], raw_df['is_legendary'])

print(kmeans)

fig = go.Figure()

for poke in range(801):
    if raw_df['is_legendary'][poke]==1  and labels[poke]==1:
        fig.add_trace(
            go.Scatter3d(
                x= [df['attack'][poke]],
                y= [df['defense'][poke]],
                z= [df['base_total'][poke]],
                    mode= 'markers',
                    marker= dict(
                        size= 3,
                      
                        color= ['purple'],
                        opacity = 0.4,
                        symbol=['circle']
                    ),
                hovertext=[raw_df['name'][poke]],
            )
        )
    elif labels[poke] == 1 and raw_df['is_legendary'][poke] == 0:
        fig.add_trace(
            go.Scatter3d(
                x= [df['attack'][poke]],
                y= [df['defense'][poke]],
                z= [df['base_total'][poke]],
                    mode= 'markers',
                    marker= dict(
                        size= 4,
                       
                        color= ['purple'],
                        opacity = 1,
                        symbol=['x']   
                    ),
                hovertext=[raw_df['name'][poke]],
            )
        )
    elif labels[poke] == 0:
        fig.add_trace(
            go.Scatter3d(
                x= [df['attack'][poke]],
                y= [df['defense'][poke]],
                z= [df['base_total'][poke]],
                    mode= 'markers',
                    marker= dict(
                        size= 3,
                        
                        color= ['green'],
                        opacity = 0.3,
                        symbol=['circle']   
                    ),
                hovertext=[raw_df['name'][poke]],
            )
        )
    elif labels[poke] == 2:
        fig.add_trace(
            go.Scatter3d(
                x= [df['attack'][poke]],
                y= [df['defense'][poke]],
                z= [df['base_total'][poke]],
                    mode= 'markers',
                    marker= dict(
                        size= 3,
                        color= ['red'],
                        opacity = 0.3,
                        symbol=['diamond']   
                    ),
                hovertext=[raw_df['name'][poke]],
            )
        )
    

# Crear Layout
fig.update_layout(
    showlegend= False,
    title= "Grupos de Pokemones Según sus Estadísticas (Kmeans para k=3)",
    xaxis_title= 'Ataque',
    yaxis_title= 'Defensa')

# Graficar y guardar HTML
pio.write_html(fig, file="k=3_interactiva.html", auto_open= True)



