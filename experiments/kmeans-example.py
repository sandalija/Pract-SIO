from sklearn.cluster import KMeans
from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


""" 
# Creando un dataset de ejemplo
X, y = datasets.make_classification(1000)

# Importando el random forest
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier() # Creando el modelo
rf.fit(X, y) # Ajustando el modelo

# verificando la precisión
print (rf) """



clu = 7

grupos, pos_correcta = datasets.make_blobs(1000, centers=clu,
cluster_std=1.75)

print (grupos)
print (pos_correcta)

# importando KMeans
from sklearn.cluster import KMeans

# Creando el modelo
kmeans = KMeans(n_clusters=clu)
kmeans.fit(grupos) # Ajustando el modelo

print (kmeans.cluster_centers_)

f, ax = plt.subplots(figsize=(7, 5))
colores = ['r', 'g', 'b']

for i in range(clu):
    p = grupos[pos_correcta == i]
    ax.scatter(p[:,0], p[:,1], c=colores[i % len(colores)],
               label="Grupo {}".format(i))

ax.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], 
           s=100, color='black', label='Centros')

ax.set_title("Agrupamiento s/modelo")
ax.legend()

plt.show()  
