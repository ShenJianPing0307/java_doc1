# 合并两个有序列表
l1 = [2, 3, 5, 9]
l2 = [1, 3, 6, 7, 10]


def merge(l1, l2):
    l1_start = 0
    l1_end = len(l1) - 1

    l2_start = 0
    l2_end = len(l2) - 1

    i = l1_start
    j = l2_start
    temp = []
    while i <= l1_end and j <= l2_end:
        if l1[i] >= l2[j]:
            temp.append(l2[j])
            j += 1
        else:
            temp.append(l1[i])
            i += 1

    while i <= l1_end:
        temp.append(l1[i])
        i += 1

    while j <= l2_end:
        temp.append(l2[j])
        j += 1

    return temp


res = merge(l1, l2)
print(res)
