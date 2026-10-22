
colors = ['Red', 'Green', 'Blue']

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

color = {}

def solve(node):
    if node == len(graph):
        return True

    region = list(graph.keys())[node]

    for c in colors:
        if all(color.get(n) != c for n in graph[region]):
            color[region] = c

            if solve(node + 1):
                return True

            del color[region]

    return False

if solve(0):
    print("Map Coloring:")
    print(color)
else:
    print("No solution")

