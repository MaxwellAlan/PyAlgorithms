# 从排序数组中删除重复项
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        setlist = set()
        index = 0
        while index < len(nums):
            if nums[index] in setlist:
                nums.pop(index)
            else:
                setlist.add(nums[index])
                index += 1
        return len(nums)

class OtherSolution:
    # 优雅的解法
    def removeDuplicates(self,nums):
        nums[:] = sorted(list(set(nums)))
        return len(nums)

    def removeDuplicates2(self, nums):
        if len(nums) < 2:
            return len(nums)
        index = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[index - 1]:
                nums[index] = nums[i]
                index += 1
        return index


if __name__ == '__main__':
    s = Solution()
    test = [0,1,1,2,2,3,4,5,5,5,5,6,6,6,6]
    print(s.removeDuplicates(test))
    print(test)