import networkx as nx
from itertools import combinations

G = nx.Graph()
G.add_edges_from([("france","russia"),("france","britain"),("britain","russia"),("hungary","austria"),("germany","austria"),("germany","hungary")], sign=1)
G.add_edges_from([("france","germany"),("france","austria"),("france","hungary"),("russia","germany"),("russia","austria"),("russia","hungary"),("britain","germany"),("britain","austria"),("britain","hungary")], sign=-1)

def triangle_sign(G, t):
    a, b, c = t
    return G[a][b]["sign"] * G[b][c]["sign"] * G[a][c]["sign"]

triangles = [t for t in combinations(G.nodes, 3)
             if all(G.has_edge(u, v) for u, v in combinations(t, 2))]
balanced = sum(1 for t in triangles if triangle_sign(G, t) > 0)

#which triangles are balanced and which are not
balanced_triangles = [t for t in triangles if triangle_sign(G, t) > 0]
unbalanced_triangles = [t for t in triangles if triangle_sign(G, t) < 0]

print(f"Balanced triangles: {balanced_triangles}")
print(f"Unbalanced triangles: {unbalanced_triangles}")

#which are the two camps partitions based on weak balance
partition = nx.algorithms.community.kernighan_lin_bisection(G, max_iter=100)
print(f"Camp 1: {partition[0]}")
print(f"Camp 2: {partition[1]}")