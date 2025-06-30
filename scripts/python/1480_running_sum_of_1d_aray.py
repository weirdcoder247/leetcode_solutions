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
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    obj = Solution()
    obj.runningSum(nums)
