# add an edge in the tree
def addEdge(adj, x, y):
    adj[x].append(y)
    adj[y].append(x)


def dfs(adj, dp, src, par):
    for child in adj[src]:
        if (child != par):
            dfs(adj, dp, child, src)

    for child in adj[src]:
        if (child != par):
            # not including source in the vertex cover
            dp[src][0] += dp[child][1]
            # including source in the vertex cover
            dp[src][1] += min(dp[child][1], dp[child][0])


# find minimum size of vertex cover
def minSizeVertexCover(adj, N):
    dp = []
    for i in range(N + 1):
        dp.append([])

    for i in range(1, N + 1):
        # 0 denotes not included in vertex cover
        dp[i].append(0)
        # 1 denotes included in vertex cover
        dp[i].append(1)
    dfs(adj, dp, 1, -1)
    print(min(dp[1][0], dp[1][1]))


if __name__ == '__main__':
    """
                                 1
 
                            /            \
 
                        2                7
 
                /             \
 
                3                6
 
        /        |        \

    4          8          5
    """

    N = 8

    # adjacency list representation of the tree
    adj = []
    for i in range(N + 1):
        adj.append([])

    addEdge(adj, 1, 2)
    addEdge(adj, 1, 7)
    addEdge(adj, 2, 3)
    addEdge(adj, 2, 6)
    addEdge(adj, 3, 4)
    addEdge(adj, 3, 8)
    addEdge(adj, 3, 5)
    minSizeVertexCover(adj, N)
