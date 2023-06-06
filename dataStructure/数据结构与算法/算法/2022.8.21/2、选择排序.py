li = [3, 5, 2, 9]


def select_sort(li):
    for i in range(len(li) - 1):

        min_pos = i

        for j in range(i + 1, len(li)):

            if li[j] < li[min_pos]:
                min_pos = j

        li[i], li[min_pos] = li[min_pos], li[i]

select_sort(li)

print(li)