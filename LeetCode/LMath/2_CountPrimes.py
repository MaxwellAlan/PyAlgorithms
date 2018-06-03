'''
计数质数
统计所有小于非负数整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
'''
import math

class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        num = [True]*(n-1)
        num[0] = False
        limit = int(math.sqrt(n))
        res = 0
        for i in range(2,limit+1,1):
            if num[i-1]:
                for j in range(i*i,n,i):
                    num[j-1] = False

        for j in range(0,n-1,1):
            if num[j] :
                res+=1
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.countPrimes(11))