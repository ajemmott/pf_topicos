import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans

df = pd.read_csv('../_assets/pokemon-data/pokemon.csv')
stats_estudiados = ['attack','defense','base_total','height_m','weight_kg','speed','sp_attack','sp_defense']
to_delete = []

for title in list(df.columns):
    if title not in stats_estudiados:
          to_delete.append(title)


df.drop(columns=to_delete)         
    

print(df.head())

#legend_df = df[df['is_legendary']==1]
#common_df = df[df['is_legendary']==0]

kmeans = KMeans(n_clusters= 4)
kmeans.fit(df)

labels = kmeans.predict(df)
centroids = kmeans.cluster_centers_

colmap = {1:'g', 2:'c', 3:'m', 4:'y'}
colors = map(lambda x: colmap[x+1], labels)

fig = plt.figure(figsize=(7,9.5))
ax = fig.add_subplot(111, projection='3d')

#ax.scatter(common_df['speed'], common_df['hp'], zs= common_df['base_total'], c=common_df['color'], alpha= 0.5)
#ax.scatter(legend_df['speed'], legend_df['hp'], zs= legend_df['base_total'], c=legend_df['color'], alpha= 0.5)


for idx, centroid in enumerate(centroids):
    ax.scatter(*centroid, c=colmap[idx +1])


ax.set_xlabel('Velocidad')
ax.set_ylabel('HP')
ax.set_zlabel('Total base')

plt.show()