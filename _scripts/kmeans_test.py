# Inicializacion

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_csv('../_assets/pokemon-data/pokemon.csv')
legend_df = df[df['is_legendary']==1]
common_df = df[df['is_legendary']==0]

# asigna un seed para numeros random para garantizar consistencia?
np.random.seed(27)

#asigna un valor arbitrario a k
k = 4

centroids = {
    i+1: [np.random.randint(1,180), np.random.randint(1,255), np.random.randint(0,800)]
    for i in range(k)
}
print(centroids)

fig = plt.figure(figsize=(7,9.5))
ax = fig.add_subplot(111, projection='3d')


ax.scatter(common_df['speed'], common_df['hp'], zs= common_df['base_total'],c='b')
ax.scatter(legend_df['speed'], legend_df['hp'], zs= legend_df['base_total'],c='r')

colmap = {1:'g', 2:'c', 3:'m', 4:'y'}
for i in centroids.keys():
    ax.scatter(*centroids[i], c=colmap[i])


ax.set_xlabel('Velocidad')
ax.set_ylabel('HP')
ax.set_zlabel('Total base')

plt.show()


# Assignnme stage

def assign_centroids(df, centroids):
    for i in centroids.keys():
        df['distance_from_{}'.format(i)] = (
            np.sqrt(
                (df['speed'] - centroids[i][0]) ** 2
                + (df['hp'] - centroids[i][1]) ** 2
                + (df['base_total'] - centroids[i][2]) ** 2
            )
        )

    centroid_distance_cols = ['distance_from_{}'.format(i) for i in centroids.keys()]
    df['closest'] = df.loc[:, centroid_distance_cols].idxmin(axis=1)
    df['closest'] = df['closest'].map(lambda x: int(x. lstrip('distance_from_')))
    df['color'] =  df['closest'].map(lambda x: colmap[x])
    return df

legend_df = assign_centroids(legend_df, centroids)
print(legend_df.head())

common_df = assign_centroids(common_df, centroids)
print(legend_df.head())

fig = plt.figure(figsize=(7,9.5))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(common_df['speed'], common_df['hp'], zs= common_df['base_total'], c=common_df['color'], alpha= 0.5)
ax.scatter(legend_df['speed'], legend_df['hp'], zs= legend_df['base_total'], c=legend_df['color'], alpha= 0.5)


for i in centroids.keys():
    ax.scatter(*centroids[i], c=colmap[i])


ax.set_xlabel('Velocidad')
ax.set_ylabel('HP')
ax.set_zlabel('Total base')

plt.show()

