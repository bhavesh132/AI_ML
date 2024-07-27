graph = {
    '5': ['3','7'],
    '3': ['2','4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': [],
}

visited = []
queue = []

def bfs (visited, graph, entry_node):
    visited.append(entry_node)
    queue.append(entry_node)

    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)



# Driver
print("The following is the depth first search for the given graph")
bfs(visited, graph, '5')
