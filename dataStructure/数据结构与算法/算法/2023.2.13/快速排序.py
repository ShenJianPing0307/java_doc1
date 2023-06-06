def partition(li,left,right):
    temp=li[left]#表示从左边取出的第一个元素
    while left<right:
        while left < right and li[right]>=temp: #从右边开始循环，寻找比归位元素小的元素放到左边空的位置
            right-=1
        li[left]=li[right]
        while left<right and li[left] <= temp:#从左边开始循环，寻找比归位元素大的元素放到右边空的位置
            left+=1
        li[right]=li[left]
    li[left]=temp #跳出循环说明左右两个位置重合了left=right，此时放temp元素
    return left

def quickSort(li,left,right):

    if left<right:#至少两个元素才能进行快排
        mid=partition(li,left,right) #返回归位元素的位置
        quickSort(li,left,mid-1) #左边元素进行排序
        quickSort(li,mid+1,right) #右边元素进行排序

li=[2,9,5,7,6,12,25,48,36]
quickSort(li,0,len(li)-1)
print(li)#[2, 5, 6, 7, 9, 12, 25, 36, 48]