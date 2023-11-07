import math
def longest_distance(vertex, target, adj, stack):
    # Base Case
    if vertex == target:
        return 0
    
    # Check if the longest path is there already
    if stack[vertex] != -math.inf:
        return stack[vertex]

    lPath = -math.inf

    for neighbor, weight in adj[vertex]:
        pLength = weight + longest_distance(neighbor, target, adj, stack)
        lPath = max(lPath, pLength)

    # Memoize the computed path.
    stack[vertex] = lPath
    return lPath

# Defining the graph in the form of a list of adjacency lists
adj = [
    [(1, 5), (2, 3)],
    [(3, 6)],
    [(3, -7), (4, 4)],
    [(4, 2)],
    []
]

s = 0  # Source vertex
t = 4  # Target vertex

stack = [-math.inf] * len(adj)  # Initialize the memoization stack

longestPath = longest_distance(s, t, adj, stack)

if longestPath != -math.inf:
    print(f"Longest Path from source {s} to target {t} is: {longestPath}")
else:
    print(f"No path from {s} to {t}.")
