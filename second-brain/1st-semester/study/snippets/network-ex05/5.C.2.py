import scipy as sp
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

#compute shortest path lengths between all pairs of nodes and use as distance matrix
G = nx.karate_club_graph()
shortest_paths = dict(nx.all_pairs_shortest_path_length(G))
n = len(G.nodes())
dist_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        dist_matrix[i, j] = shortest_paths[i][j]

from scipy.spatial.distance import squareform
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
from scipy.stats import mode

# convert the square distance matrix to condensed form and apply average linkage
d_cond = squareform(dist_matrix)
Z = linkage(d_cond, method='average')

# plot the dendrogram
plt.figure(figsize=(10, 8))
_dn = dendrogram(Z, labels=list(G.nodes()), leaf_rotation=90)
plt.title("Hierarchical Clustering Dendrogram of Karate Club Network")
plt.xlabel("Node")
plt.ylabel("Distance")
plt.show()

# cut to obtain exactly 2 clusters
clusters = fcluster(Z, t=2, criterion='maxclust')

# evaluate fraction matching known factions
faction = nx.get_node_attributes(G, 'club')
true = np.array([0 if faction[i] == "Mr. Hi" else 1 for i in G.nodes()])
pred = clusters - 1  # make 0/1 labels
# map each predicted cluster to the majority true label
map_ = {}
for c in np.unique(pred):
    vals = true[pred == c]
    if vals.size == 0:
        map_[c] = 0
    else:
        counts = np.bincount(vals.astype(int))
        map_[c] = int(np.argmax(counts))
acc = (np.array([map_[c] for c in pred]) == true).mean()
print("Fraction matching known factions:", acc)
