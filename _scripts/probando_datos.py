import pandas as pd

data = pd.read_csv('Pictures\Pokemon_original.csv')

#Cuantos datos son?
print(len(data.index))

#explorando las columnas
print(data.columns)

#explorando los datos
print(data.head())

#Borrando el que parece innecesario
data=data.drop(['abilities','against_bug', 'against_dark','experience_growth','against_dragon', 'against_electric', 'against_fairy', 'against_fight', 'against_fire', 'against_flying',  'against_ghost', 'against_grass', 'against_ground', 'against_ice', 'against_normal', 'against_poison', 'against_psychic', 'against_rock', 'against_steel', 'against_water', 'base_egg_steps', 'base_happiness', 'capture_rate', 'japanese_name', 'percentage_male', 'pokedex_number'],axis=1)

#Viendo las nuevas dimensiones de los datos
print(data.columns)
print(data.head())