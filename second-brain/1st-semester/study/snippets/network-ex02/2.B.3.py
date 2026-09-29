import networkx as nx
import matplotlib.pyplot as plt

G=nx.karate_club_graph()
nodes = sorted(G.nodes())

#1
print(f'Number of nodes: {G.number_of_nodes()}, Number of edges: {G.number_of_edges()}')

#2
avg_deg = 2 * G.number_of_edges() / G.number_of_nodes()
print(f'Average degree: {avg_deg:.2f}')

#3
isolated_nodes = [node for node, degree in G.degree() if degree == 0]
print(f'Isolated nodes: {isolated_nodes}')

#4
nx.draw_spring(G, with_labels=True)
plt.show()