import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

G = nx.karate_club_graph()

strengths, overlaps = [], []

#topological overlap function (accounts for the edge itself)
def topological_overlap(G, u, v):
    """Topological overlap T(u,v) = (|N(u) ∩ N(v)| + 1) / min(deg(u), deg(v)) for adjacent u,v."""
    neighbors_u = set(G.neighbors(u))
    neighbors_v = set(G.neighbors(v))
    intersection = len(neighbors_u & neighbors_v)
    denom = min(len(neighbors_u), len(neighbors_v))
    return (intersection + 1) / denom if denom > 0 else 0

#Compute strengths and overlaps
for u, v in G.edges():
    s = 0.8 if G.nodes[u]['club'] == G.nodes[v]['club'] else 0.2
    strengths.append(s)
    overlaps.append(topological_overlap(G, u, v))


#Correlation
r = np.corrcoef(strengths, overlaps)[0, 1]
print(f"Pearson correlation coefficient: {r:.3f}")