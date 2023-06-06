li = [2, 3, 5, 9]


def binary_search(li, target):
    start = 0
    end = len(li) - 1

    while start <= end:

        mid = (start + end) // 2

        if li[mid] < target:
            start = mid + 1
        elif li[mid] > target:
            end = mid - 1
        else:
            return mid
    return None


if __name__ == '__main__':
    res = binary_search(li, 3)
    print(res)
