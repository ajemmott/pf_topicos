# Importar librerias

import pandas as pd

import plotly
import plotly.graph_objects as go


# importar datos desde csv
data = pd.read_csv("../_assets/pokemon-data/pokemon.csv")

# Crear figura con plotly
fig = go.Scatter3d(
    x= data['weight_kg'], 
    y= data['height_m'], 
    z=data['base_total'],
    mode="markers",
    marker= dict(
        size= 6,
        line=dict(
            color='rgba(127, 127, 127, 1)',
            width=0.5
            ),
        colorscale = "Tealrose",
        color=data["is_legendary"],
        )
    )

# Crear Layout
mylayout = go.Layout(xaxis= dict(title="Peso (kg)"), yaxis= dict(title= "Altura (m)"))

# Graficar y guardar HTML
plotly.offline.plot({"data": [fig], "layout": mylayout }, auto_open=True)
