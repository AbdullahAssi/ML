from collections import deque

def bfs(graph, root):
    visited = set()
    queue = deque([root])

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

graph = {
    'A': ['B', 'D'],
    'B': ['U', 'L'],
    'D': ['L'],
    'U': [],
    'L': ['A'],
    'H': ['G'],
}

bfs(graph, 'B')
