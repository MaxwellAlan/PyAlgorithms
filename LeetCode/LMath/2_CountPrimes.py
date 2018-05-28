'''
计数质数
统计所有小于非负数整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
'''


class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 2
        if n < 2:
            return 0
        elif n == 2:
            return 1
        else:
            for i in range(2,n):
                for j in range(2,i):
                    if i % j == 0:
                        count += 1
                        break
        return n-count

if __name__ == '__main__':
    s = Solution()
    print(s.countPrimes(5))