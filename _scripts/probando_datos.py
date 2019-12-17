#para manejar los datasets
import pandas as pd 
#Visualizaciones
from matplotlib import pyplot as plt
import seaborn as sns

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
plot1= sns.lmplot(x='attack', y='defense', data=datos, fit_reg=False, hue='classfication')
plot1.savefig("../_assets/plots/porClasificación.png")

#Viendo el ataque vs defensa por legendario
plot2=sns.lmplot(x='attack', y='defense', data=datos, fit_reg=False, hue='is_legendary')
plot2.savefig("../_assets/plots/porLegendario.png")


#Aun así se puede observar las habilidades de pokemones con base total

