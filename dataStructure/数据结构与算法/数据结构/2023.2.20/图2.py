
dfs_searched = set()

def dfs(graph, start):
    print(start)
    if start not in dfs_searched:
        dfs_searched.add(start)

    for node in graph[start]:
        if node not in dfs_searched:
            dfs(graph, node)

if __name__ == '__main__':
    graph = {
        'A': ['B', 'F'],
        'B': ['C', 'I', 'G'],
        'C': ['B', 'I', 'D'],
        'D': ['C', 'I', 'G', 'H', 'E'],
        'E': ['D', 'H', 'F'],
        'F': ['A', 'G', 'E'],
        'G': ['B', 'F', 'H', 'D'],
        'H': ['G', 'D', 'E'],
        'I': ['B', 'C', 'D'],
    }
    dfs(graph,'A')