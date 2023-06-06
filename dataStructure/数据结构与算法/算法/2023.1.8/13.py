from concurrent.futures import ThreadPoolExecutor


def merge(X, Y):
    Z = []
    while X and Y:
        if X[0] < Y[0]:
            Z.append(X[0])
            del X[0]
        else:
            Z.append(Y[0])
            del Y[0]
    if X:
        Z.extend(X)
    if Y:
        Z.extend(Y)
    return Z


def p_merge(X, Y):
    n1 = len(X)
    n2 = len(Y)
    if n1 < n2: return p_merge(Y, X)
    if n1 < 42: return merge(X, Y)
    r = n1 // 2 - 1
    pool = ThreadPoolExecutor(2)
    res1 = pool.submit(p_merge, X[0:n1 // 2], Y[0:r])
    res2 = pool.submit(p_merge, X[n1 // 2 + 1:n1], Y[r + 1:n2])
    pool.shutdown()
    z1 = res1.result()
    z2 = res2.result()
    return z1 + z2


if __name__ == '__main__':
    # X = [i for i in range(0, 200, 3)]
    # Y = [j for j in range(1, 300, 3)]
    X = [3, 4, 7, 9, 11]
    Y = [1, 2, 5, 8, 13, 20]
    Z = p_merge(X, Y)
    print('Z', Z)
