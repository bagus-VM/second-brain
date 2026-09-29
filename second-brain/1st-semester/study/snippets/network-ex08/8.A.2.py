import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

G = nx.karate_club_graph()

#compute average clustering and average shortest path length
avg_clustering = nx.average_clustering(G)
try:
    avg_shortest_path_length = nx.average_shortest_path_length(G)
except nx.NetworkXError:
    avg_shortest_path_length = float('inf')  # Graph is not connected

print(f"Average clustering coefficient: {avg_clustering:.4f}")
print(f"Average shortest path length: {avg_shortest_path_length:.4f}")

# Generate a random graph with the same n and m. compute clustering_rand and shortest_path_length_rand
n = G.number_of_nodes()
m = G.number_of_edges()
random_graph = nx.gnm_random_graph(n, m)
clustering_rand = nx.average_clustering(random_graph)
try:
    shortest_path_length_rand = nx.average_shortest_path_length(random_graph)
except nx.NetworkXError:
    shortest_path_length_rand = float('inf')

print(f"Random graph average clustering coefficient: {clustering_rand:.4f}")
print(f"Random graph average shortest path length: {shortest_path_length_rand:.4f}")

# compute the small-world index C/C_rand and L/L_rand
small_world_index = (avg_clustering / clustering_rand) / (avg_shortest_path_length / shortest_path_length_rand) if shortest_path_length_rand != 0 else float('inf')
print(f"Small-world index: {small_world_index:.4f}")

#compare to a pure ring lattice and visualize the graph
ring_lattice = nx.watts_strogatz_graph(n, k=4, p=0)  # Pure ring lattice with k=4
clustering_ring = nx.average_clustering(ring_lattice)
try:
    shortest_path_length_ring = nx.average_shortest_path_length(ring_lattice)
except nx.NetworkXError:
    shortest_path_length_ring = float('inf')

print(f"Ring lattice average clustering coefficient: {clustering_ring:.4f}")
print(f"Ring lattice average shortest path length: {shortest_path_length_ring:.4f}")

#visualize the graphs
plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray')
plt.title("Zachary's Karate Club Graph")
plt.subplot(1, 3, 2)
nx.draw(random_graph, with_labels=True, node_color='lightgreen', edge_color='gray')
plt.title("Random Graph (G(n,m))")
plt.subplot(1, 3, 3)
nx.draw(ring_lattice, with_labels=True, node_color='lightcoral', edge_color='gray')
plt.title("Pure Ring Lattice")
plt.tight_layout()
plt.show()