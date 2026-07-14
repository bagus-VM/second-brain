import networkx as nx
import numpy as np

G = nx.karate_club_graph()

#club attributes as the group label
faction = nx.get_node_attributes(G, 'club')

#count within faction and cross faction edges
within_edges = 0
cross_edges = 0
for u, v in G.edges():
    if faction[u] == faction[v]:
        within_edges += 1
    else:
        cross_edges += 1

print(f"Within-faction edges: {within_edges}")
print(f"Cross-faction edges: {cross_edges}")

#compute E-I index for faction
E_I_index = (cross_edges - within_edges) / (cross_edges + within_edges)
print(f"E-I Index: {E_I_index:.3f}")

#Compute the expected cross-faction edge fraction under random mixing
n = len(G.nodes())
n1 = list(faction.values()).count('Mr. Hi')
n2 = n - n1
expected_cross_fraction = (2 * n1 * n2) / (n * (n - 1))
print(f"Expected cross-faction fraction: {expected_cross_fraction:.3f}")

