'''
两数之和
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_i = index_j = 0
        for index_i in range(len(nums)):
            if (target - nums[index_i]) in nums:
                index_j = index_i + 1
                while index_j < len(nums):
                    if nums[index_j] == (target - nums[index_i]):
                        return [index_i,index_j]
                    index_j += 1

if __name__ == '__main__':
    s = Solution()
    nums = [3,2,4]
    target = 6
    print(s.twoSum(nums,target))
