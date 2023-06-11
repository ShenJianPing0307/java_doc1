s = "bcabc"

def del_com_al_helper(res, lst, s, pos):
    res.append(lst[:])
    # if len(lst) >= 2 and (ord(lst[-2]) > ord(lst[-1])):
    #     res.remove(lst)
    #     return

    for i in range(pos, len(s)):
        # if ord(s[i]) < ord(s[i-1]):
        #     continue
        lst.append(s[i])
        del_com_al_helper(res, lst, s, i+1)
        lst.pop()


def del_com_al():
    res = []
    lst = []

    del_com_al_helper(res, lst, s, 0)

    print(res)

del_com_al()