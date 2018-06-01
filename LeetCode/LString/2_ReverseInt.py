'''
颠倒整数
给定一个 32 位有符号整数，将整数中的数字进行反转。
'''
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = False
        tmp = 0
        if x < 0:
            flag = True
            x = - x
        while x != 0:
            tmp = tmp * 10
            tmp += x % 10
            x = x // 10

        if flag:
            if -x < -2 ** 31 or -tmp < -2 ** 31:
                return 0
            else:
                return -tmp
        else:
            if x > 2 ** 31 - 1 or tmp > 2 ** 31 - 1:
                return 0
            else:
                return tmp


if __name__ == '__main__':
    s = Solution()
    # print(s.reverse(1534236469))
    print(s.reverse(1563847412))