import networkx as nx
import matplotlib.pyplot as plt

G = nx.karate_club_graph()
factions = nx.get_node_attributes(G, 'club')
sign_dict = {}

# Sign edges by faction: within = +1, cross = -1
for u, v in G.edges():
    sign_dict[(min(u, v), max(u, v))] = 1 if factions[u] == factions[v] else -1

def count_negatives(signs):
    """Count negative edges in a list of signs."""
    return sum(1 for s in signs if s == -1)

def get_edge_sign(u, v):
    """Get sign of edge (u, v) from sign_dict."""
    return sign_dict.get((min(u, v), max(u, v)), None)

def is_triangle_balanced(u, v, w):
    """Check if triangle is balanced (even number of negatives)."""
    edges = [(u, v), (u, w), (v, w)]
    signs = [get_edge_sign(a, b) for a, b in edges]
    if None in signs:  # Edge was removed
        return None
    neg_count = count_negatives(signs)
    return neg_count % 2 == 0

def count_balanced_triangles():
    """Count balanced and unbalanced triangles in G."""
    triangles = [c for c in nx.enumerate_all_cliques(G) if len(c) == 3]
    balanced = sum(1 for u, v, w in triangles if is_triangle_balanced(u, v, w))
    unbalanced = len(triangles) - balanced
    return balanced, unbalanced, len(triangles)

# 1. Count balanced vs unbalanced triangles (initial state)
balanced, unbalanced, total = count_balanced_triangles()
print(f"Initial state:")
print(f"  Balanced triangles: {balanced}")
print(f"  Unbalanced triangles: {unbalanced}")

# 2. Fraction balanced
fraction_balanced_0 = balanced / total if total > 0 else 0
print(f"  Fraction balanced: {fraction_balanced_0:.4f}")

# 3. Identify cross-faction edges and their participation in unbalanced triangles
triangles = [c for c in nx.enumerate_all_cliques(G) if len(c) == 3]
cross_faction_edges = {(min(u, v), max(u, v)): 0 for u, v in G.edges() 
                       if factions[u] != factions[v]}

# Count unbalanced triangles each cross-faction edge participates in
for u, v, w in triangles:
    if not is_triangle_balanced(u, v, w):
        # This is an unbalanced triangle
        edges_in_triangle = [(min(a, b), max(a, b)) for a, b in [(u, v), (u, w), (v, w)]]
        for edge in edges_in_triangle:
            if edge in cross_faction_edges:
                cross_faction_edges[edge] += 1

# 4. Remove top 5 cross-faction edges and track fraction-balanced
fraction_balanced_list = [fraction_balanced_0]
edges_removed_list = [0]

for i in range(5):
    if not cross_faction_edges:
        print("No more cross-faction edges to remove.")
        break
    
    # Find edge with most unbalanced triangle participation
    edge_to_remove = max(cross_faction_edges, key=cross_faction_edges.get)
    
    print(f"\nRemoving edge {edge_to_remove} (participates in {cross_faction_edges[edge_to_remove]} unbalanced triangles)")
    
    # Remove edge from graph and sign_dict
    G.remove_edge(*edge_to_remove)
    del sign_dict[edge_to_remove]
    del cross_faction_edges[edge_to_remove]
    
    # Recount balanced triangles
    balanced, unbalanced, total = count_balanced_triangles()
    fraction_balanced = balanced / total if total > 0 else 0
    
    print(f"  After removal: {balanced}/{total} balanced ({fraction_balanced:.4f})")
    
    fraction_balanced_list.append(fraction_balanced)
    edges_removed_list.append(i + 1)

# Plot fraction-balanced vs edges-removed
plt.figure(figsize=(10, 6))
plt.plot(edges_removed_list, fraction_balanced_list, marker='o', linewidth=2, markersize=8)
plt.xlabel('Number of cross-faction edges removed', fontsize=12)
plt.ylabel('Fraction of balanced triangles', fontsize=12)
plt.title('Effect of removing cross-faction edges on triangle balance\n(Karate Club Network)', fontsize=14)
plt.grid(True, alpha=0.3)
plt.xticks(edges_removed_list)
plt.ylim(0, 1)
plt.tight_layout()
plt.show()