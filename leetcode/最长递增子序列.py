"""
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度
"""
import bisect
nums = [10, 9, 2, 5, 3, 7, 101, 18]

def get_num():

    if len(nums) == 1:
        return len(nums)

    start = nums[0]
    res = [start]

    for item in nums[1:]:
        if res[-1] <= item:
            res.append(item)
        else:
            index = bisect.bisect_left(res, item)
            res[index] = item

        print(res)

print(get_num())
