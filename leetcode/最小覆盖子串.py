s = "ADOBECODEBANC"
t = "ABC"

def min_string():

    queue = []
    res = []
    val = 0

    for v, i in enumerate(s):
        queue.append(i)
        print(i, queue)
        if set(queue) & set(t) == set(t):
            left = True
            while left:
                val = queue.pop(0)
                if set(queue) & set(t) != set(t):
                    left = False
            res.append(f"{val}{''.join(queue)}")
    print(res)
min_string()








