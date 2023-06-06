def select_sort(li):
    for i in range(len(li) - 1):

        min_position = i

        for j in range(i + 1, len(li)):

            if li[j] < li[min_position]:
                min_position = j
        li[i], li[min_position] = li[min_position], li[i]

li = [5, 1, 8, 0]

select_sort(li)

print(li)