import networkx as nx
import matplotlib.pyplot as plt

G = nx.karate_club_graph()

#centralities
centralities = [nx.eigenvector_centrality(G), nx.degree_centrality(G), nx.betweenness_centrality(G), nx.closeness_centrality(G)]
print ("Centralities:")
print(f"Eigenvector Centrality : {centralities[0]}")
print(f"Degree Centrality : {centralities[1]}")
print(f"Betweenness Centrality : {centralities[2]}")
print(f"Closeness Centrality : {centralities[3]}")

#top-3 nodes for each centrality
top_nodes = [sorted(centrality.items(), key=lambda x: x[1], reverse=True)[:3] for centrality in centralities]
print("\nTop-3 nodes for each centrality:")
centrality_names = ["Eigenvector Centrality", "Degree Centrality", "Betweenness Centrality", "Closeness Centrality"]
for name, nodes in zip(centrality_names, top_nodes):
    print(f"{name}: {nodes}")

#plot four subplots, each showing the network with node sizes proportional to one centrality measure.
plt.figure(figsize=(12, 10))
for i, (centrality, name) in enumerate(zip(centralities, centrality_names)):
    plt.subplot(2, 2, i + 1)
    node_sizes = [v * 1000 for v in centrality.values()]
    nx.draw(G, with_labels=True, node_size=node_sizes, node_color='lightblue', font_size=8)
    plt.title(name)  
plt.tight_layout()
plt.show()  

#Find a node that ranks very differently across measures
print("\nNodes with varying rankings across centrality measures:")
for node in G.nodes():
    eigen_rank = sorted(centralities[0].items(), key=lambda x: x[1], reverse=True).index((node, centralities[0][node])) + 1
    degree_rank = sorted(centralities[1].items(), key=lambda x: x[1], reverse=True).index((node, centralities[1][node])) + 1
    betweenness_rank = sorted(centralities[2].items(), key=lambda x: x[1], reverse=True).index((node, centralities[2][node])) + 1
    closeness_rank = sorted(centralities[3].items(), key=lambda x: x[1], reverse=True).index((node, centralities[3][node])) + 1
    rank_diff = max(eigen_rank, degree_rank, betweenness_rank, closeness_rank) - min(eigen_rank, degree_rank, betweenness_rank, closeness_rank)
    if rank_diff >= 3:
        print(f"Node {node}: Eigen={eigen_rank}, Degree={degree_rank}, Betweenness={betweenness_rank}, Closeness={closeness_rank} (Diff={rank_diff})")