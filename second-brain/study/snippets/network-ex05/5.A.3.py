import networkx as nx
import matplotlib.pyplot as plt

G = nx.karate_club_graph()

#greedy modularity communities
communities = nx.community.greedy_modularity_communities(G)

#compute modularity scores
modularity_score = nx.community.modularity(G, communities)
print(f"Modularity score: {modularity_score:.4f}")

#compare to the known faction labels. What fraction of nodes are correctly classified?
# Get the known faction labels from the graph
faction_labels = nx.get_node_attributes(G, 'club')
# Create a mapping from faction labels to community indices
faction_to_community = {}
for i, community in enumerate(communities):
    for node in community:
        faction_to_community[node] = i

# For each detected community, find the majority faction → assign as predicted label
community_predicted_faction = {}
for i, community in enumerate(communities):
    faction_counts = {}
    for node in community:
        f = faction_labels[node]
        faction_counts[f] = faction_counts.get(f, 0) + 1
    community_predicted_faction[i] = max(faction_counts, key=lambda k: faction_counts[k])

# Count how many nodes match their community's predicted faction
correct = 0
total = len(G.nodes())
for node in G.nodes():
    if faction_labels[node] == community_predicted_faction[faction_to_community[node]]:
        correct += 1

print(f"Fraction of nodes correctly classified: {correct/total:.4f}")

# Visualize the communities
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, seed=42)
node_colors = [faction_to_community[node] for node in G.nodes()]
nx.draw_networkx(G, pos, with_labels=True, node_size=300, cmap=plt.cm.Set3, 
                node_color=node_colors, edge_color='gray')
plt.title("Karate Club Network: Community Detection vs Known Factions")
plt.show()