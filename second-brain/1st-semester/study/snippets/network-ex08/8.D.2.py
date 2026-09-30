import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

G.add_edges_from([("A", "B"), ("B", "C"), ("C", "A"),
                  ("D", "A"), ("E", "B"),
                  ("C", "F"), ("B", "G"),
                  ("D", "H")])

G.add_node("I")

sccs = list(nx.strongly_connected_components(G))
C = nx.condensation(G, scc=sccs)
giant = max(range(len(sccs)), key=lambda i: len(sccs[i]))

reachable_from_giant = nx.descendants(C, giant) | {giant}
can_reach_giant = nx.ancestors(C, giant) | {giant}

# Visualize the condensation graph showing reachability from the giant SCC
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(C)
nx.draw(C, pos, with_labels=True, node_color='lightblue', edge_color='gray')
nx.draw_networkx_nodes(C, pos, nodelist=list(reachable_from_giant), node_color='green', alpha=0.7, label='Reachable from Giant')
nx.draw_networkx_nodes(C, pos, nodelist=list(can_reach_giant), node_color='red', alpha=0.7, label='Can Reach Giant')
plt.legend()
plt.title('Condensation Graph with Giant SCC Reachability')
plt.show()