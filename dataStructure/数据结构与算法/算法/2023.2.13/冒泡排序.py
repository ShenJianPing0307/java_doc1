li = [3, 2, 5, 9]


def bubble_sort(li):
    for i in range(len(li)-1):

        for j in range(i, len(li)-1):

            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]


bubble_sort(li)
print(li)
