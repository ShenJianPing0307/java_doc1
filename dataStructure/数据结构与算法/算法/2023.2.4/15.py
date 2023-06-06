def vertexCover(edges, n, m):
    vis = [False] * n
    for i in range(n):
        if not vis[i]:
            for x in edges[i]:
                if not vis[x]:
                    vis[x] = True
                    vis[i] = True
                    break
    for i in range(n):
        if vis[i]:
            print(i, end=" ")
    print()