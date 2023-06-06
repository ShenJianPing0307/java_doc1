
def bfs(graph, start):
    queue = []
    searched_set = set()
    queue.append(start)

    while queue:
        cur_node = queue.pop(0)

        if cur_node not in searched_set:
            searched_set.add(cur_node)
            print(cur_node)

            for node in graph[cur_node]:
                queue.append(node)


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
    bfs(graph,'A')