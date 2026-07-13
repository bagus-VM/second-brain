from collections import deque
import networkx as nx

#1
def bfs_distances(graph, source):
    dist = {source: 0}
    queue = deque([source])
    while queue:
        node = queue.popleft()
        for neighbor in graph.get(node, []):
            if neighbor not in dist:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
    return dist
G = nx.karate_club_graph()
adj = {node: list(G.neighbors(node)) for node in G.nodes()}

#2 & 4
d0 = bfs_distances(adj, 0)
d33 = bfs_distances(adj, 33)

print(f"Eccentricity of node 0: {max(d0.values())}, Eccentricity of node 33: {max(d33.values())}")