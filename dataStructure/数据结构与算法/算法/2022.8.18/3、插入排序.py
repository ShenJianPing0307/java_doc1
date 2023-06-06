def insert_sort(li):
    """
    从第一个元素后面开始选择
    :param li:
    :return:
    """
    for i in range(1, len(li)):  # 对无序区的元素进行循环，i表示第一个元素的下标，因为有序区已经有一个元素了
        temp = li[i]  # 将无序区取出的元素进行保存
        j = i - 1  # 是有序区的最后一个位置下标
        while j >= 0 and li[j] > temp:  # j表示有序区的元素
            li[j + 1] = li[j]  # 将有序区的元素向后移动，因为从无序区已经取出一个元素，空了一个位置
            j -= 1  # 有序区的元素继续向前循环比较

        # 将无序区的元素插入到有序区
        li[j + 1] = temp
        # for i in range(1, len(li) - 1):
    #     temp = li[i]
    #     j = i - 1 # 有序区元素第一个位置
    #     while j > 0 and li[j] > temp:
    #         li[j], temp = temp, li[j]
    #         j -= 1
    #     li[j+1] = temp

li = [5, 1, 8, 0]

insert_sort(li)

print(li)

