from concurrent.futures import ThreadPoolExecutor
import time

"""
人 料
n m
3 3
- 1 - 2
+ 1 - 3
+ 2 - 3
1、因此每位客人都应该至少实现一个愿望
2、某人不可能两次许下相同的愿望（每个人必须选择两个不同的愿望）
3、也不会有人将同一成分命名两次（一次是正面的，一次是负面的）
4、也有可能两个人的愿望完全相同
"""
# n, m = [3, 3]
# tasks = [(1, +1, -2), (2, +1, -3), (3, +2, -3)]
# assign = {}
# d = {
#     -3: [2, 3],
#     -2: [1],
#     1: [1, 2],
#     2: [3]
# }
tasks = []
wish_to_customer_hash = {}
suit_customer = set()


def read_file():
    index = 0
    with open("file/3_3_1sat.in") as f:
        for line in f:
            yield index, line
            index += 1


def get_wish():
    n = m = 0
    wish_flag = True
    for idx, count_or_wish in read_file():
        if idx == 0:
            n, m = count_or_wish.split()
            continue
        op1, num1, op2, num2 = count_or_wish.split()
        wish1, wish2 = int("".join([op1, num1])), int("".join([op2, num2]))
        # 某人不可能两次许下相同的愿望（每个人必须选择两个不同的愿望）
        if wish1 == wish2:
            wish_flag = False
        # 也不会有人将同一成分命名两次（一次是正面的，一次是负面的）
        elif n + m == 0:
            wish_flag = False
        else:
            tasks.append((idx, wish1, wish2))
            wish_to_customer_hash.setdefault(wish1, [])
            wish_to_customer_hash.setdefault(wish2, [])
            wish_to_customer_hash[wish1].append(idx)
            wish_to_customer_hash[wish2].append(idx)
    return n, m, wish_flag


def handle_task(item_tuple):
    flag = True
    for idx, item in enumerate(item_tuple):
        if idx == 0:
            continue
        if abs(item) in wish_to_customer_hash and -abs(item) not in wish_to_customer_hash or \
                (abs(item) not in wish_to_customer_hash and -abs(item) in wish_to_customer_hash):
            flag = False
            break
    if not flag:
        suit_customer.add(item_tuple[0])


def cal_time(func):
    def inner():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"花费时间:{end_time - start_time}")

    return inner


@cal_time
def main():
    n, m, wish_flag = get_wish()
    if not wish_flag:
        print("notsat1")
        return
    pool = ThreadPoolExecutor()
    for task in tasks:
        pool.submit(handle_task, task)

    pool.shutdown()

    if len(suit_customer) == int(m):
        print("sat")
    else:
        print("notsat")


if __name__ == '__main__':
    main()
