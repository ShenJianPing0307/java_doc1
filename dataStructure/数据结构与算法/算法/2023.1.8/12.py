def get_pair_array(integer_array):
    length = len(integer_array)
    pair_array = []
    for i, v in enumerate(integer_array):
        j = i + 1
        while j <= length - 1:
            v2 = integer_array[j] - v
            pair_array.append(v2)
            j += 1
    return pair_array


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


from threading import Thread


def merge_sort(li, start, end):
    if start < end:
        mid = (start + end) // 2
        t1 = Thread(target=merge_sort, args=(li, start, mid))
        t2 = Thread(target=merge_sort, args=(li, mid + 1, end))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        merge(li, start, mid, end)


if __name__ == '__main__':
    integer_array = [0, 1, 2, 5, 6, 8, 9]
    pair_array = get_pair_array(integer_array)
    merge_sort(pair_array, 0, len(pair_array) - 1)
    max_value = pair_array[-1]
