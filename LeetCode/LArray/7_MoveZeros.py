'''
移动零
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
'''


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index = 0
        zeros = 0
        while index < len(nums):
            while index < len(nums) and nums[index] == 0:
                zeros += 1
                nums.pop(index)
            index += 1
        return nums+[0]*zeros

    # i = j = 0
    #
    # while j < len(nums):
    #
    #     if nums[j] == 0:
    #         j += 1
    #     elif nums[i] == 0:
    #         nums[i], nums[j] = nums[j], nums[i]
    #         i += 1
    #         j += 1
    #     else:
    #         i += 1
    #         j += 1

    # j = 0
    # for i in range(len(nums)):
    #     if nums[i] != 0:
    #         nums[j], nums[i] = nums[i], nums[j]
    #         j += 1

if __name__ == '__main__':
    s = Solution()
    nums = [1,0]
    print(s.moveZeroes(nums))
