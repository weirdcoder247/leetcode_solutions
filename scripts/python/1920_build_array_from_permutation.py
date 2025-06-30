class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [nums[x] for x in nums]

if __name__ == '__main__':
    obj = Solution()
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    obj.buildArray(nums)
