li = [3, 5, 2, 9]


# li = [2, 4, 7, 9, 3, 5, 6, 8]


def merge(li, start, mid, end):
    i = start
    j = mid + 1
    temp = []

    while i <= mid and j <= end:

        if li[i] < li[j]:
            temp.append(li[i])
            i += 1
        else:
            temp.append(li[j])
            j += 1

    while i <= mid:
        temp.append(li[i])
        i += 1

    while j <= end:
        temp.append(li[j])
        j += 1
    li[start:end + 1] = temp


def merge_sort(li, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(li, start, mid)
        merge_sort(li, mid + 1, end)
        merge(li, start, mid, end)


merge_sort(li, 0, len(li) - 1)
print(li)
