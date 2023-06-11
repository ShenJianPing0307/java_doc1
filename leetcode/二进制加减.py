"""
示例 1：
输入:a = "11", b = "1"
输出："100"

解题思路：该题可以从两种思路思考.
        其一模仿十进制加减法，按位相加，逢十进一；
        其二是将二进制转成十进制，使用十进制加减，然后转成二进制即可
"""


# 方法一
class Solution1:
    def addBinary(self, a: str, b: str) -> str:
        """使用归并排序的思想，进行双指针按位求和"""
        a = list(map(int, list(a)))
        b = list(map(int, list(b)))
        res = []  # 将每一位的结果保存在列表中
        t = 0  # 进位数
        i = len(a) - 1  # 二进制数 a 的指针
        j = len(b) - 1  # 二进制数 b 的指针

        while i >= 0 and j >= 0:
            x = a[i] + b[j] + t
            res.append(x % 2)  # 保存求和的结果
            t = x // 2  # 进位数
            i -= 1
            j -= 1
        while i >= 0:
            x = a[i] + t
            res.append(x % 2)
            t = x // 2
            i -= 1
        while j >= 0:
            x = b[j] + t
            res.append(x % 2)
            t = x // 2
            j -= 1
        if t == 1:
            res.append(1)
        res = ''.join(list(map(str, res[::-1])))
        return res


# 方法二
class Solution2:
    def addBinary(self, a: str, b: str) -> str:
        """通过 int 方法转成十进制相加，然后通过 bin 方法转成二进制"""
        res = bin(int(a, 2) + int(b, 2))[2:]
        return res


if __name__ == '__main__':
    a = "1010"
    b = "1011"
    solution1 = Solution1()
    solution2 = Solution2()

    print(solution1.addBinary(a, b))  # 10101
    print(solution2.addBinary(a, b))  # 10101
