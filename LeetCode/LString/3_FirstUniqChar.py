'''
字符串中的第一个唯一字符
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:

s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.


注意事项：您可以假定该字符串只包含小写字母
'''

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return -1
        dic = dict((ch, [i, 0]) for i, ch in enumerate(list(s)))
        for ch in list(s):
            dic[ch][1] += 1
        for ch in s:
            if dic[ch][1] == 1:
                return dic[ch][0]
        return -1
        # letters = 'abcdefghijklmnopqrstuvwxyz'
        # L_index = [s.index(letter) for letter in letters if s.count(letter) == 1]
        # return min(L_index) if L_index else -1

if __name__ == '__main__':
    s = Solution()
    print(s.firstUniqChar("leetcode"))