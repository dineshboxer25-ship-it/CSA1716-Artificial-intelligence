
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dfs(node, visited):
    if node not in visited:
        visited.append(node)
        for neighbour in graph[node]:
            dfs(neighbour, visited)

visited = []
dfs('A', visited)

print("DFS traversal from A:", visited)

