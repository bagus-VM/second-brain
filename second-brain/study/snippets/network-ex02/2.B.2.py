import matplotlib.pyplot as plt
import networkx as nx
G = nx.Graph()
G.add_edges_from([("A", "B"), ("A", "C"), ("B", "C"), ("B", "D"),("D","E")])
nodes = sorted(G.nodes())

#1
print("Adjacency matrix:\n", nx.to_numpy_array(G, nodelist=nodes))

#2
print("Degrees:", dict(G.degree()))

#3
print(f"Density: {nx.density(G):.3f}")

#4 Directed version
DG = nx.DiGraph()
DG.add_edges_from([("A", "B"), ("A", "C"), ("B", "C"), ("B", "D"), ("D", "E")])
print(f"In-degree of B: {DG.in_degree('B')}, Out-degree of B: {DG.out_degree('B')}")
print(f"In-degree of D: {DG.in_degree('D')}, Out-degree of D: {DG.out_degree('D')}")

#5 Plot both graphs side by side
pos = nx.spring_layout(G, seed=42)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
nx.draw(G, pos, with_labels=True, ax=ax1)
ax1.set_title("Undirected G")
nx.draw(DG, pos, with_labels=True, ax=ax2, arrows=True)
ax2.set_title("Directed DG")
plt.tight_layout()
plt.show()