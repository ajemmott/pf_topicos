#para manejar los datasets
import pandas as pd 
#Visualizaciones
from matplotlib import pyplot as plt
import seaborn as sns
import plotly
from plotly.subplots import make_subplots
import plotly.express as px
import plotly.graph_objects as go
#Solo para validaciones
import os.path
from PIL import Image

'''
EXPLORANDO LA DATA
'''
#Cargando el csv
datos = pd.read_csv('../_assets/pokemon-data/pokemon.csv')

#Cuantos datos son?
print(len(datos.index))

#explorando las columnas
print(datos.columns)

#explorando los datos
print(datos.head())

#Borrando el que parece innecesario
datos=datos.drop(['abilities','against_bug', 'against_dark','experience_growth','against_dragon', 'against_electric', 'against_fairy', 'against_fight', 'against_fire', 'against_flying',  'against_ghost', 'against_grass', 'against_ground', 'against_ice', 'against_normal', 'against_poison', 'against_psychic', 'against_rock', 'against_steel', 'against_water', 'base_egg_steps', 'base_happiness', 'capture_rate', 'japanese_name', 'percentage_male', 'pokedex_number'],axis=1)

#Viendo las nuevas dimensiones de los datos
print(datos.columns)
print(datos.head())

'''
VISUALIZACIONES
'''

#Viendo el ataque vs defensa por clasificación
if os.path.exists('../_assets/plots/porClasificación.png'):
    img = Image.open('../_assets/plots/porClasificación.png')
    img.show()
else:
    plot1= sns.lmplot(x='speed', y='defense', data=datos, fit_reg=False, hue='classfication')
    plot1.savefig("../_assets/plots/porClasificación.png")

#Viendo el ataque vs defensa por tipo
if os.path.exists('../_assets/plots/porTipo.png'):
    img = Image.open('../_assets/plots/porTipo.png')
    img.show()
else:
    plot2=sns.lmplot(x='speed', y='defense', data=datos, fit_reg=False, hue='type1')
    plot2.savefig("../_assets/plots/porTipo.png")

#Viendo el ataque vs defensa por legendario
if os.path.exists('../_assets/plots/porLegendario.png'):
    img = Image.open('../_assets/plots/porLegendario.png')
    img.show()
else:
    plot3=sns.lmplot(x='speed', y='defense', data=datos, fit_reg=False, hue='is_legendary')
    plot3.savefig("../_assets/plots/porLegendario.png")

'''
EXPLORANDO MÁS LOS DATOS
'''
#Se notan más datos que pueden no aportar mucho a la investigación, SE ELIMINAN
#Borrando lo innecesario
datos=datos.drop(['classfication','sp_attack','sp_defense','type1', 'type2'],axis=1)

#Viendo las nuevas dimensiones de los datos
print(datos.columns)
print(datos.dtypes)
print(datos.head())

'''
VIENDO CARACTERISTICAS DE LEGENDARIOS
'''
legendary_data = datos[datos['is_legendary']==1]
normal_data = datos[datos['is_legendary']==0]

legendarios = go.Scatter(
        x= legendary_data['height_m'], 
        y= legendary_data['weight_kg'], 
        mode='markers',
        hovertext=legendary_data['name'],
        name="Legendarios",
        )

normales = go.Scatter(
        x= normal_data['height_m'], 
        y= normal_data['weight_kg'], 
        mode='markers',
        hovertext=normal_data['name'],
        name="NOT Legendarios"
        )



fig2 = go.Data([legendarios, normales])

mLayout = go.Layout(
    title = "Altura vs Peso",
    xaxis = dict(title = 'Altura (m)'),
    yaxis = dict(title = 'Peso (kg)')
)

# Graficar y guardar HTML
plotly.offline.plot({"data": fig2, "layout":mLayout}, auto_open=True)

#Boxplot de valores extremos
bplot = make_subplots(rows=3, cols=1,shared_xaxes=True, vertical_spacing=0.02)

bplot.append_trace(go.Box(
        y=datos['attack'],
        #hover_data=["name"],
        x=datos['is_legendary'],
        name='Ataque',
        hovertext=datos['name']),
        row=1, col=1)

bplot.append_trace(go.Box(
        y=datos['defense'],
        x=datos['is_legendary'],
        name='Defensa',
        hovertext=datos['name']),
        row=2, col=1)

bplot.append_trace(go.Box(
        y=datos['speed'],
        x=datos['is_legendary'],
        name='Speed',
        hovertext=datos['name']),
        row=3, col=1)

bplot.update_layout(height=600, width=600,
                  title_text="Attack, Defense and Speed")

# Graficar y guardar HTML
plotly.offline.plot(bplot, auto_open=True)
'''
GUARDANDO CSV
'''
datos.to_csv('../_assets/pokemon-data/pokemon_seleccionados.csv')



