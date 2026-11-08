import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (4, 5), (4, 6), (5, 6), (3, 7), (4, 7)])

#betweeness centrality of all nodes
bc = nx.betweenness_centrality(G)
print("Betweenness centrality:")
for node, score in bc.items():
    print(f"{node}: {score:.3f}")

# Visualize with node sizes proportional to betweenness
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G, seed=42)
node_sizes = [v * 3000 for v in bc.values()]
nx.draw_networkx(G, pos, with_labels=True, node_size=node_sizes, node_color='skyblue', edge_color='gray')
plt.title("Network with Node Sizes Proportional to Betweenness Centrality")
plt.show()



G = nx.karate_club_graph()
#sort nodes top 3 by betweenness centrality (highest) but lowest clustering coefficient first
bc = nx.betweenness_centrality(G)
cc = nx.clustering(G)
sorted_nodes = sorted(G.nodes(), key=lambda n: (bc[n], -cc[n]), reverse=True)[:3]
print("\nNodes sorted by betweenness centrality (highest first) and clustering coefficient:")
for node in sorted_nodes:
    print(f"Node {node}: Betweenness={bc[node]:.3f}, Clustering={cc[node]:.3f}")

# Visualize the Karate Club graph with node sizes proportional to betweenness centrality
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, seed=42)
node_sizes = [bc[n] * 3000 for n in G.nodes()]
nx.draw_networkx(G, pos, with_labels=True, node_size=node_sizes, node_color='skyblue', edge_color='gray')
plt.title("Karate Club Network: Node Sizes Proportional to Betweenness Centrality")
plt.show()