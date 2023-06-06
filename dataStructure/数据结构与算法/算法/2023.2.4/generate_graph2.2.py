def gen_subsets(set_, k):
    curr_subset = []
    vertex_res = []
    generate_subsets(set_, curr_subset, vertex_res, k, 0)
    return vertex_res


def generate_subsets(set_, curr_subset, subsets_, k, next_index):
    if len(curr_subset) == int(k):
        subsets_.append(curr_subset)
        return
    if next_index + 1 <= len(set_):
        curr_subset_exclude = curr_subset.copy()
        curr_subset.append(set_[next_index])
        generate_subsets(set_, curr_subset, subsets_, k, next_index + 1)
        generate_subsets(set_, curr_subset_exclude, subsets_, k, next_index + 1)


def gen_subsets_graph_set(graph, subsets):
    entire_sets = []
    for item in subsets:
        each_subset_graph = {}
        for ele in item:
            each_subset_graph.setdefault(ele, graph.get(ele, []))
        entire_sets.append(each_subset_graph)
    return entire_sets


def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            if (node, neighbour) and (neighbour, node) not in edges:
                edges.append((node, neighbour))
    return edges


def verify_vertex_cover(cover, edges):
    # check that atleast one vertice from each edge appears in cover
    for edge in edges:
        in_cover = False
        for vertex in cover:
            if edge[0] == vertex or edge[1] == vertex:
                in_cover = True
        # stop processing as soon as one edge found not in cover
        if in_cover == False:
            return False
    # return true if all edges have atleast one endpoint in cover
    return True


def vertex_cover_brute(graph, res):
    vertices = list(dict(graph).keys())
    k = len(vertices)
    edges = generate_edges(graph)
    for i in range(1, k):
        subsets_ = gen_subsets(vertices, i)
        for s in subsets_:
            if verify_vertex_cover(s, edges) == True:
                res.append(s)
                return


if __name__ == '__main__':
    graph = {1: [2, 3],
             2: [3, 1],
             3: [2, 4, 5],
             4: [3, 5, 6, 7]
             }
    vertices = list(dict(graph).keys())
    subsets = gen_subsets(vertices, 3)

    subsets_graph = gen_subsets_graph_set(graph, subsets)

    res = []
    for s in subsets_graph:
        vertex_cover_brute(s, res)
    print("vertex cover set num is {}".format(len(res)))
