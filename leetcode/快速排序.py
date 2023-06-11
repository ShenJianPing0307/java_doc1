li = [8, 3, 11, 7, 10]


def quick(li, left, right):
    temp = li[left]

    while left < right:
        while left < right and li[left] <= temp:
            left += 1
        li[right] = li[left]

        while left < right and li[right] >= temp:
            right -= 1
        li[left] = li[right]

    li[left] = temp
    return left


def quick_sort(li, left, right):
    if left < right:
        mid = quick(li, left, right)
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid + 1, right)

"""
    if left < right:
        mid = quick(li, left, right)
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid + 1, right)
"""

if __name__ == '__main__':
    quick_sort(li, 0, len(li) - 1)
    print(li)
