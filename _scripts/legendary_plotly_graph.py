# Importar librerias

import pandas as pd

import plotly
import plotly.graph_objects as go


# importar datos desde csv
data = pd.read_csv("../_assets/pokemon-data/pokemon.csv")
legendary_data = data[data['is_legendary']==1]


fig2 = go.Scatter3d(x= legendary_data['weight_kg'], 
    y= legendary_data['height_m'], 
    z= legendary_data['base_total'],
    mode="markers",
    marker= dict(size= 6,
        line=dict(
            color='rgba(127, 127, 127, 1)',
            width=0.5
        ),
        colorscale = "Magma",
        color=legendary_data["is_legendary"],
            
        )
    )

# Crear Layout
mylayout2 = go.Layout(xaxis= dict(title="Peso (kg)"), yaxis= dict(title= "Altura (m)"))

# Graficar y guardar HTML
plotly.offline.plot({"data": [fig2], "layout": mylayout2 }, auto_open=True)