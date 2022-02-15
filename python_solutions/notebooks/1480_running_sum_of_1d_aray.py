class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
        return nums


if __name__ == '__main__':
    nums = [1, 2, 3]
    obj = Solution()
    obj.runningSum(nums)
