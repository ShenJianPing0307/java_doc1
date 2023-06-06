"""
                                A

                               /

                    B      —— F

            /       |    \

        C    ——    D      E

"""
import random, copy
cover_vertex_arr = ['B', 'C', 'F']
all_vertex_arr = ['A', 'B', 'C', 'D', 'E', 'F']
vertex_arr = list(set(all_vertex_arr)-set(cover_vertex_arr))


def generate_cover_graph(cover_vertex_set):
    cover_graph = {}
    for index, vertex in enumerate(cover_vertex_set):
        try:
            cover_graph[vertex] = [cover_vertex_set[index + 1]]
        except Exception:
            cover_graph[vertex] = []
            continue
    return cover_graph

def generate_graph(vertex_arr, cover_graph):
    graph = copy.deepcopy(cover_graph)
    for _ in range(len(vertex_arr)):
        ele = vertex_arr.pop(random.randint(0,len(vertex_arr)-1))
        key = random.choice(list(cover_graph.keys()))
        graph[key].append(ele)
    return graph

if __name__ == '__main__':
    cover_graph = generate_cover_graph(cover_vertex_arr)
    graph = generate_graph(vertex_arr, cover_graph)
    print(graph)
