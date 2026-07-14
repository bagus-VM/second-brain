import networkx as nx

#affiliation attributes as the group label S1,S2,S3,S4 and C1,C2,C3 enrollment S1-C1, S1-C2, S2-C1, S3-C2, S3-C3, S4-C3
G = nx.Graph()
students = ['S1', 'S2', 'S3', 'S4']
courses = ['C1', 'C2', 'C3']
G.add_nodes_from(students, bipartite=0)
G.add_nodes_from(courses, bipartite=1)

G.add_edges_from([('S1', 'C1'), ('S1', 'C2'), ('S2', 'C1'), ('S3', 'C2'), ('S3', 'C3'), ('S4', 'C3')])

#weighted projection
from networkx.algorithms import bipartite
student_projected = bipartite.weighted_projected_graph(G, students)
print(student_projected.edges(data=True))