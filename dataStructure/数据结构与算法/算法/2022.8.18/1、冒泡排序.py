def bubble_sort(li):
    for i in range(len(li) - 1):

        for j in range(len(li) - i - 1):

            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]


li = [5, 1, 8, 0]

bubble_sort(li)

print(li)
