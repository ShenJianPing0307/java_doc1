def dt(n, nums):
    """
    :param n: 能到达的方格
    :param nums: 每一个方格的时间
    :return:
    """
    if n <= 1:
        return nums[1]
    return dt(n - 1, nums) + nums[0] + nums[n]


def get_nums():
    with open("1.csv") as f:
        res = f.readlines()
        lnums = [int(num.strip("\n")) for num in res]
    return lnums[0], lnums[1:]


n, nums = get_nums()
print(n, nums)
res = dt(n - 1, nums)
print(res)
