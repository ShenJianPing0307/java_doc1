li = [3, 2, 5, 9]


def quick(li, start, end):
    temp = li[start]

    while start < end:
        while start < end and li[end] >= temp:
            end -= 1
        li[start] = li[end]

        while start < end and li[start] <= temp:
            start += 1
        li[end] = li[start]

    li[start] = temp
    return start


def quick_sort(li, start, end):
    if start < end:
        mid = quick(li, start, end)
        quick(li, start, mid-1)
        quick(li, mid+1, end)
    print(li)


if __name__ == '__main__':
    quick_sort(li, 0, len(li) - 1)
