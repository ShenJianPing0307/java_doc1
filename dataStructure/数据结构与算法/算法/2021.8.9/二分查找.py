li = [2, 3, 5, 9]


def binary_search(li, target):
    start = 0
    end = len(li) - 1

    while start <= end:
        mid = (start + end) // 2
        if li[mid] < target:
            start = mid + 1
        elif li[mid] == target:
            return mid
        else:
            end = mid - 1
    return None


print(binary_search(li, 3))
