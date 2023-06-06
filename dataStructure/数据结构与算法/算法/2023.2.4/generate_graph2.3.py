import time
sorted_vertices = []
k = 0
start_time = time.time()
TIME_MAX = 30



class UndirectedGraph:

    def __init__(self, V, E):

        """
        Initialize the Graph class. Accepts a set of vertices V and edges E as input.
        V is implemented as a set
        E is implemented as an adjacency list in the form of a dictionary.
        """

        self.V = V
        self.E = E

    def __str__(self):

        graph_str = ''

        for start in self.E.keys():
            for stop in self.E[start]:
                graph_str += start + ' ' + stop + '\n'

        return graph_str


def check_vertex_cover(G, S):
    """
    Returns True if set S is a vertex cover of the edge set E,
    False otherwise.
    S is implemented as a set
    E is implemented as an adjacency list mapping a vertex to a list
    of edges
    """

    for start in G.E.keys():
        if start in S:
            # vertex start is already in the cover
            # so we needn't check its corresponding edges
            continue
        for end in G.E[start]:
            if not (end in S):
                return False
    return True

def param_vc_wrapper(G, S, next_vertex_count):
    """
    S is the subset selected so far
    Other parameters are as below
    """

    current_time = time.time()

    if len(S) > k:
        # this VC has exceeded the budget
        return (None, current_time - start_time)

    if check_vertex_cover(G, S):
        return (S, current_time - start_time)

    if len(S) == k:
        return (None, current_time - start_time)

    # now we choose between the vertex that comes next in degree
    # or its neighbours

    new_vc = S.copy()
    new_vc.add(sorted_vertices[next_vertex_count])

    # check branch 1 (pick that vertex)
    current_time = time.time()
    if current_time - start_time > TIME_MAX:
        return (None, TIME_MAX)
    branch1, branch1_time = param_vc_wrapper(G, new_vc, next_vertex_count + 1)
    if branch1 != None:
        return (branch1, current_time - start_time)
    current_time = time.time()
    if current_time - start_time > TIME_MAX:
        # no time to check second branch
        return (None, TIME_MAX)

    # check branch 2 (pick the vertex's neighbours)
    current_time = time.time()
    if current_time - start_time > TIME_MAX:
        return (None, TIME_MAX)
    branch2, branch2_time = param_vc_wrapper(G, S.union(G.E[sorted_vertices[next_vertex_count]]), next_vertex_count + 1)
    if branch2 != None:
        return (branch2, current_time - start_time)

    current_time = time.time()
    return (None, current_time - start_time)


def parameterized_vc(G, k_val):
    """
    Runs the branching algorithm on the input instance
    """

    global sorted_vertices
    global k
    global start_time

    k = k_val
    sorted_vertices = sorted(G.E, key=lambda k: len(G.E[k]), reverse=True)
    start_time = time.time()
    return param_vc_wrapper(G, set([]), 0)

if __name__ == '__main__':
    pass
    # G is an object of type UndirectedGraph
    # k is an integer (parameter)
    # parameterized_vc(G, k)