def get_min_time(n, nums):
    target_pos = n
    pre_pos = 0
    current_pos = 0
    next_pos = 0
    max_pos = len(nums) - 1
    i = 1
    j = 0

    sum_time = 0
    val = 0
    while True:
        next_pos += i
        current_pos += j
        pre_pos = current_pos - j

        if next_pos > target_pos or next_pos > max_pos:
            val = sum_time + nums[pre_pos] + nums[target_pos]
            break

        if next_pos == target_pos:
            val = sum_time + nums[target_pos]
            break

        sum_time += nums[next_pos]
        i += 1
        j += 1
    return val


nums = [3, 2, 1, 5, 4]
res = get_min_time(3, nums)
print(res)
