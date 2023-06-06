"""插入排序"""

li = [3, 5, 2, 9]


def insert_sort(li):
    for i in range(1, len(li)):

        for j in range(i, 0, -1):

            if li[j] > li[j - 1]:
                li[j], li[j - 1] = li[j - 1], li[j]


insert_sort(li)
print(li)
