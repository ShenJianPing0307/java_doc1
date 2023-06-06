nums = [3, 2, 1, 5, 4]


def can_jump(nums):
    right_most = 0
    n = len(nums)
    for i in range(n):
        right_most = max(right_most, i)

    if right_most >= n - 1:
        return True
    return False


res = can_jump(nums)
print(res)
