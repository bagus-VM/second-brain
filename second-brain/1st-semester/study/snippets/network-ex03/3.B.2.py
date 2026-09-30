import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

G = nx.Graph()
G.add_edges_from([(1,2),(1,3),(2,3),(4,5),(4,6),(5,6),(7,8),(7,9),(8,9),(3,4),(6,7)])
bridges = list(nx.bridges(G))
# [(3,4), (6,7)]
ebc = nx.edge_betweenness_centrality(G)

print("Bridges:", bridges)
sorted_eb = sorted(ebc.items(), key=lambda kv: kv[1], reverse=True)
print("Edges ranked by edge betweenness:")
for edge, score in sorted_eb:
    print(f"{edge}: {score:.3f}")

plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G, seed=42)
# safe edge-width lookup (undirected edges may appear in either order)
edge_widths = [ebc.get(tuple(edge), ebc.get((edge[1], edge[0]), 0)) * 5 for edge in G.edges()]
# draw nodes and edges scaled by betweenness
nx.draw(G, pos, with_labels=True, width=edge_widths, node_color='lightblue', edgecolors='gray')
# draw bridges on top in red
nx.draw_networkx_edges(G, pos, edgelist=bridges, width=4, edge_color='red')


bridge_line = mlines.Line2D([], [], color='red', linewidth=4, label='Bridges')
plt.legend(handles=[bridge_line])
plt.title('Edge Betweenness Centrality (bridges highlighted)')
plt.show()