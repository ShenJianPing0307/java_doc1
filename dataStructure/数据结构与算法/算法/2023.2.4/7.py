def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            if (node,neighbour) and (neighbour, node) not in edges:
                edges.append((node,neighbour))
    return edges

def gen_subsets(set_, k):
    curr_subset = []
    res = []
    generate_subsets(set_, curr_subset, res, k, 0)
    return res

def generate_subsets(set_, curr_subset, subsets_, k, next_index):
    if len(curr_subset) == int(k):
        subsets_.append(curr_subset)
        return
    if next_index + 1 <= len(set_):
        curr_subset_exclude = curr_subset.copy()
        curr_subset.append(set_[next_index])
        generate_subsets(set_, curr_subset, subsets_, k, next_index+1)
        generate_subsets(set_, curr_subset_exclude, subsets_, k, next_index+1)


