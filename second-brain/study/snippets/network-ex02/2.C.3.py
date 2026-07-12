import networkx as nx
import matplotlib.pyplot as plt

arpa = nx.Graph()
arpa.add_edges_from([
    ("UCLA", "SRI"), ("UCLA", "USCB"), ("UCLA", "UTAH"), 
    ("SRI", "UTAH"), ("SRI", "BBN"),
    ("USCB", "SRI"), ("UTAH","MIT"),
    ("BBN", "HARVARD"), ("BBN", "MIT"), ("MIT", "HARVARD"),
])

#2
path = nx.shortest_path(arpa, "UCLA", "HARVARD")
print(f"Shortest path: {path}")
print(f"Shortest path length: {len(path) - 1}")

#3
print(f"Diameter: {nx.diameter(arpa)}")
print(f"Radius: {nx.radius(arpa)}")
print(f"Eccentricity: {nx.eccentricity(arpa)}")

#4
print(f"Center: {nx.center(arpa)}")

#1
nx.draw_spring(arpa, with_labels=True)
plt.show()