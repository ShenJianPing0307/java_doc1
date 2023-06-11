X = "babad"
Y = X[::-1]

m = n = len(X)

mx = [[0 for k in range(n + 1)] for l in range(m + 1)]
print(mx)


def longest_palindom_string(s):
    result = 0
    for i in range(m + 1):
        for j in range(n + 1):
            if (i == 0 or j == 0):
                mx[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                mx[i][j] = mx[i - 1][j - 1] + 1
                result = max(result, mx[i][j])
            else:
                mx[i][j] = max(mx[i - 1][j], mx[i][j - 1])
    return result

# longest_palindom_string(s)
