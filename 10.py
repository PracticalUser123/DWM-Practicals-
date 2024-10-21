import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add edges to the graph
G.add_edges_from([
    ('A', 'D'), ('B', 'C'), ('B', 'E'), ('C', 'A'),
    ('D', 'C'), ('E', 'D'), ('E', 'B'), ('E', 'F'),
    ('E', 'C'), ('F', 'C'), ('F', 'H'), ('G', 'A'),
    ('G', 'C'), ('H', 'A')
])

# Draw the graph
plt.figure(figsize=(10, 10))
nx.draw_networkx(G, with_labels=True)
plt.show()  # Display the graph

# Calculate HITS hub and authority scores
hubs, authorities = nx.hits(G, max_iter=50, normalized=True)

# Print the scores
print("Hub Scores: ", hubs)
print("Authority Scores: ", authorities)

