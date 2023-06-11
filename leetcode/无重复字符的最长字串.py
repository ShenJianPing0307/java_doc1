s = "abcabcbb"

def large_string():

    window = []
    res = 0
    for i in s:
        if i not in window:
            window.append(i)
            res = max(res, len(window))
        else:
            index = window.index(i)
            window = window[index+1:]
            window.append(i)
            res = max(res, len(window))
    print(res)

large_string()