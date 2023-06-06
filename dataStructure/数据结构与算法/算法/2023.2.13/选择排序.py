li = [3, 5, 2, 9]


def select_sort(li):
    for i in range(len(li)):

        min_position = i

        for j in range(i + 1, len(li)):

            if li[j] < li[min_position]:
                min_position = j
        li[i], li[min_position] = li[min_position], li[i]


select_sort(li)

print(li)
