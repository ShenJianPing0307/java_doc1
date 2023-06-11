nums = [3, 30, 34, 5, 9]

num_str = list(map(str, nums))

def lager_num():


    for i in range(len(nums)-1):

        for j in range(i+1, len(nums)):
            if int(num_str[i]+num_str[j]) < int(num_str[j]+num_str[i]):
                num_str[i], num_str[j] = num_str[j], num_str[i]

lager_num()
print(num_str)