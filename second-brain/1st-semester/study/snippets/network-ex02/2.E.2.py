import networkx as nx
import matplotlib.pyplot as plt
import random

G = nx.karate_club_graph()

def giant_fraction(G):
    if G.number_of_nodes() == 0:
        return 0
    return len (max(nx.connected_components(G), key=len)) / G.number_of_nodes()

def simulate(G0,strategy) :
    G = G0.copy()
    sizes = [giant_fraction(G)]
    while G.number_of_nodes() > 0:
        if strategy == "random":
            node = random.choice(list(G.nodes()))
        else:
            node = max(G.nodes(), key=lambda n: G.degree(n))
        G.remove_node(node)
        sizes.append(giant_fraction(G))
    return sizes

sizes_random = simulate(G, "random")
sizes_targeted = simulate(G, "targeted")

sizes_random = simulate(G, "random")
sizes_targeted = simulate(G, "targeted")

import matplotlib.pyplot as plt
plt.plot(sizes_random, label="Random")
plt.plot(sizes_targeted, label="Targeted (degree)")
plt.xlabel("Nodes removed")
plt.ylabel("Giant component fraction")
plt.legend()
plt.show()