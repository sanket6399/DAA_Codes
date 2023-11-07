from collections import defaultdict

def topological_SortHelper(graph, u, visited, stack):
    visited[u] = True
    for v, _ in graph[u]:
        if not visited[v]:
            topological_SortHelper(graph, v, visited, stack)
    stack.append(u)

def getLongestDistance(graph, s, t):
    n = len(graph) 
    dp = [-float('inf')] * n  # Initialize dp array with negative infinty
    dp[s] = 0 

    # Code for topological sorting using DFS
    visited = [False] * n
    stack = []

    for u in range(n):
        if not visited[u]:
            topological_SortHelper(graph, u, visited, stack)

    # Using stack operations to check the vertices in topological order
    while stack:
        u = stack.pop()

        # Step 3: Update dp array
        for v, weight in graph[u]:
            dp[v] = max(dp[v], dp[u] + weight)

    # Return the longest path length from s to t
    return dp[t]

if __name__ == "__main__":
    # Define the graph as a dictionary
    graph = {
        0: [(1, 5), (2, 3)],
        1: [(3, 6)],
        2: [(3, -7), (4, 4)],
        3: [(4, 2)],
        4: []
    }
    
    s = 0  # Source vertex
    t = 4  # Target vertex
    
    longestPath = getLongestDistance(graph, s, t)
    print(f"Longest weighted simple path from {s} to {t}: {longestPath}")
