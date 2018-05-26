'''
 加一
给定一个非负整数组成的非空数组，在该数的基础上加一，返回一个新的数组。

最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。
'''


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        res = 0
        for i in range(length):
            res += 10**(length-i-1) * digits[i]
        res += 1
        num = []
        while res != 0:
            num.insert(0,res%10)
            res //= 10
        return num

        # num = 0
        # for i in range(len(digits)):
        #     num = num * 10 + digits[i]
        # return [int(i) for i in str(num + 1)]

        # carry = 1
        # for i in range(len(digits) - 1, -1, -1):
        #     digits[i] += carry
        #     carry = 0
        #     if digits[i] >= 10:
        #         digits[i] %= 10
        #         carry = 1
        # if carry == 1:
        #     digits.insert(0, 1)
        # return digits

if __name__ == '__main__':
    s = Solution()
    dis = [9,9,9,9]
    print(s.plusOne(dis))
