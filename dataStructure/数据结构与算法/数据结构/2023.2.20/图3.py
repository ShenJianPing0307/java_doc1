def dfs(graph, start):
    stack = []
    searched_set = set()
    stack.append(start)

    while stack:
        cur_node = stack.pop()
        if cur_node not in searched_set:
            print(cur_node)
            searched_set.add(cur_node)

            for node in reversed(graph[cur_node]):
                stack.append(node)

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
