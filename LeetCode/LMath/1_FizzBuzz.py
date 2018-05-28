'''
 Fizz Buzz
写一个程序，输出从 1 到 n 数字的字符串表示。

1. 如果 n 是3的倍数，输出“Fizz”；

2. 如果 n 是5的倍数，输出“Buzz”；

3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。

示例：

n = 15,

返回:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
'''
class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = [str(x) for x in range(1,n+1)]
        i = 2
        while i < n:
            res[i] = 'Fizz'
            i += 3
        i = 4
        while i < n:
            res[i] = 'Buzz'
            i += 5
        i = 14
        while i < n:
            res[i] = 'FizzBuzz'
            i += 15
        return res