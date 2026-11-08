import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

G = nx.karate_club_graph()

def neighbour_overlap(G, u, v):
    """Compute the neighbour overlap between nodes u and v in graph G."""
    neighbors_u = set(G.neighbors(u))
    neighbors_v = set(G.neighbors(v))
    intersection = len(neighbors_u & neighbors_v)
    union = len(neighbors_u | neighbors_v)
    if union == 0:
        return 0
    return intersection / union

#compare within and accross factions

within = [neighbour_overlap(G, u, v) for u, v in G.edges() 
          if G.nodes[u]['club'] == G.nodes[v]['club']]
across = [neighbour_overlap(G, u, v) for u, v in G.edges() 
          if G.nodes[u]['club'] != G.nodes[v]['club']]

print(f"Within-faction overlap: {np.mean(within):.3f}")
print(f"Across-faction overlap: {np.mean(across):.3f}")
