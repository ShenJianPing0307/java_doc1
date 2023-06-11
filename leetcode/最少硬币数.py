nums = [1, 2, 5]
amount = 8

result = []
tmp = []


def dfs(result, tmp, coins, remains, start):
    if remains < 0:
        return
    if remains == 0:
        result.append(tmp[:])
    else:
        for i in range(start, len(coins)):
            # if (coins[i] == coins[i - 1]):
            #     continue
            tmp.append(coins[i])
            dfs(result, tmp, coins, remains - coins[i], i+1)
            tmp.pop()


def comb(nums, t):
    result = []
    tmp = []
    nums.sort()
    dfs(result, tmp, nums, t, 0)
    print(result)


if __name__ == '__main__':
    comb(nums, amount)
