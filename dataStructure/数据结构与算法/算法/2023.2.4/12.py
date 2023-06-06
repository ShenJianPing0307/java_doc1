import itertools
import time

TIME_MAX = 30


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


def brute_force_VC(G):
    """
    Return the vertex cover of edges E as a set, None otherwise.
    """

    start_time = time.time()
    current_time = start_time
    for k in range(1, len(G.V) + 1):
        'Checking subsets of size', str(k) + '...'
        # iterate over k sized subsets
        # check if each of those subsets is a vertex cover
        for subset in itertools.combinations(G.V, k):
            current_time = time.time()
            # set(subset) is needed for O(1) checking of membership
            # otherwise subset is generated as a list and might take
            # upto O(n) time
            if check_vertex_cover(G, set(subset)):
                return (set(subset), current_time - start_time)
            if current_time - start_time > TIME_MAX:
                # timeout
                return (None, TIME_MAX)

    return (None, current_time - start_time)
