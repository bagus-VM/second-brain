import os
import networkx as nx
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# --- Setup ---
G = nx.karate_club_graph()
faction_labels = nx.get_node_attributes(G, 'club')

# ============================================================
# 1. Girvan-Newman: extract the 2-community partition
# ============================================================
gn = nx.community.girvan_newman(G)
# next() yields the first split — 2 communities
gn_communities = tuple(sorted(c) for c in next(gn))
print(f"Girvan-Newman communities: {len(gn_communities)}")
print(f"  sizes: {[len(c) for c in gn_communities]}")

# ============================================================
# 2. Modularity of the Girvan-Newman partition
# ============================================================
gn_modularity = nx.community.modularity(G, gn_communities)
print(f"GN modularity:  {gn_modularity:.4f}")

# ============================================================
# 3. Faction recovery: majority-vote per community
# ============================================================
gn_node_community = {}
for i, comm in enumerate(gn_communities):
    for node in comm:
        gn_node_community[node] = i

gn_predicted = {}
for i, comm in enumerate(gn_communities):
    counts = {}
    for node in comm:
        f = faction_labels[node]
        counts[f] = counts.get(f, 0) + 1
    gn_predicted[i] = max(counts, key=lambda k: counts[k])
    print(f"  Community {i}: predicted={gn_predicted[i]}, breakdown={counts}")

gn_correct = sum(
    1 for n in G.nodes()
    if faction_labels[n] == gn_predicted[gn_node_community[n]]
)
gn_accuracy = gn_correct / len(G)
print(f"GN faction accuracy:  {gn_correct}/{len(G)} = {gn_accuracy:.4f}")

# ============================================================
# 4. Compare to greedy modularity (5.A.3)
# ============================================================
gm_communities = nx.community.greedy_modularity_communities(G)
gm_modularity = nx.community.modularity(G, gm_communities)

gm_node_community = {}
for i, comm in enumerate(gm_communities):
    for node in comm:
        gm_node_community[node] = i

gm_predicted = {}
for i, comm in enumerate(gm_communities):
    counts = {}
    for node in comm:
        f = faction_labels[node]
        counts[f] = counts.get(f, 0) + 1
    gm_predicted[i] = max(counts, key=lambda k: counts[k])

gm_correct = sum(
    1 for n in G.nodes()
    if faction_labels[n] == gm_predicted[gm_node_community[n]]
)
gm_accuracy = gm_correct / len(G)
print(f"\nGreedy modularity accuracy: {gm_correct}/{len(G)} = {gm_accuracy:.4f}")

# ============================================================
# 5. Edge betweenness: top-5 before and after 1 removal step
# ============================================================
eb_before = nx.edge_betweenness_centrality(G)
top5_before = sorted(eb_before.items(), key=lambda x: x[1], reverse=True)[:5]

# Remove the single highest-betweenness edge (first GN step)
top_edge = top5_before[0][0]
G_removed = G.copy()
G_removed.remove_edge(*top_edge)

eb_after = nx.edge_betweenness_centrality(G_removed)
top5_after = sorted(eb_after.items(), key=lambda x: x[1], reverse=True)[:5]

print(f"\nTop-5 edges by betweenness (original):")
for (u, v), score in top5_before:
    print(f"  ({u}-{v}): {score:.4f}")

print(f"Top-5 edges by betweenness (after removing {top_edge[0]}-{top_edge[1]}):")
for (u, v), score in top5_after:
    print(f"  ({u}-{v}): {score:.4f}")

# ============================================================
# 6. Plot: community network + edge betweenness bar chart
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# --- Left: graph with detected communities ---
ax0 = axes[0]
pos = nx.spring_layout(G, seed=42)
node_colors = [gn_node_community[n] for n in G.nodes()]
nx.draw_networkx(G, pos, ax=ax0, with_labels=True, node_size=300,
                 node_color=node_colors, edge_color='gray')
ax0.set_title(f"Girvan-Newman (2 communities)\nModularity={gn_modularity:.3f}, Accuracy={gn_accuracy:.2%}")

# --- Right: edge betweenness bar chart ---
ax1 = axes[1]
labels_before = [f"{u}-{v}" for (u, v), _ in top5_before]
scores_before = [s for _, s in top5_before]
scores_after = [s for _, s in top5_after]

x = range(len(labels_before))
bar_width = 0.35
ax1.bar([i - bar_width / 2 for i in x], scores_before, bar_width,
        label='Original', color='steelblue', alpha=0.8)
ax1.bar([i + bar_width / 2 for i in x], scores_after, bar_width,
        label='After 1 removal', color='coral', alpha=0.8)

ax1.set_xticks(list(x))
ax1.set_xticklabels(labels_before, rotation=45, ha='right')
ax1.set_ylabel("Edge Betweenness Centrality")
ax1.set_title("Top-5 Edge Betweenness: Before vs After 1 Removal")
ax1.legend()

plt.tight_layout()
plot_path = os.path.join(SCRIPT_DIR, "5.B.2_plot.png")
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
plt.close()
print(f"\nPlot saved to {plot_path}")
