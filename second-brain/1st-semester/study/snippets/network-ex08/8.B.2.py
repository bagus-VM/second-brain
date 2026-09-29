import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

G = nx.watts_strogatz_graph(n=100, k=6, p=0)

#for p from 0.001 to 1.0, compute normalized average clustering and average shortest path length
p_values = np.logspace(-3, 0, num=20)
normalized_clustering = []
normalized_shortest_path_length = []

for p in p_values:
    G = nx.watts_strogatz_graph(n=100, k=6, p=p, seed=42)
    normalized_clustering.append(nx.average_clustering(G) / 0.5)  # Normalized by ring lattice value (k/2n)
    normalized_shortest_path_length.append(nx.average_shortest_path_length(G) / 10.0)  # Normalized by ring lattice value

# Plot both of the results against log(p)
plt.figure(figsize=(10, 6))
plt.plot(np.log10(p_values), normalized_clustering, marker='o', label='Normalized Clustering Coefficient')
plt.plot(np.log10(p_values), normalized_shortest_path_length, marker='s', label='Normalized Average Shortest Path Length')
plt.xlabel('log10(p)')
plt.ylabel('Normalized Values')
plt.title('Normalized Clustering Coefficient and Average Shortest Path Length vs log10(p)')
plt.legend()
plt.grid()
plt.show()

#identify the small-world regime where normalized clustering is high and normalized shortest path length is low
small_world_regime = [(p, C, L) for p, C, L in zip(p_values, normalized_clustering, normalized_shortest_path_length) if C > 0.5 and L < 1.5]
print("Small-world regime (p, normalized clustering, normalized shortest path length):")
for p, C, L in small_world_regime:
    print(f"p: {p:.4f}, Normalized Clustering: {C:.4f}, Normalized Shortest Path Length: {L:.4f}")  
