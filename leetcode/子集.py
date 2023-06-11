nums = ['a', 'b', 'c']

def subsets(nums):
    result = [[]]
    for num in nums:

        for ele in result[:]:
            x = ele[:]
            x.append(num)
            result.append(x)
    return result
