li = [3, 5, 2, 9]

def insert_sort(li):

    for i in range(1, len(li)):

        temp = li[i] # 无序区第一个元素
        j = i - 1 # 有序区第一个位置

        # 从后向前循环
        while j >= 0 and li[j] < temp:
            li[j+1] = li[j]
            j -= 1

