li = [3, 5, 2, 9]


def quick_sort(li):
    if len(li) < 2:
        return li

    mid = li[len(li) // 2]
    li.remove(mid)
    left, right = [], []



    for item in li:

        if item < mid:
            left.append(item)
        else:
            right.append(item)

    return quick_sort(left) + [mid] + quick_sort(right)


print(quick_sort(li))
