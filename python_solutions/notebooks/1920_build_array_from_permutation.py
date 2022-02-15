class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [nums[x] for x in nums]

if __name__ == '__main__':
    obj = Solution()
    obj.buildArray(nums = [2,1,0,4,3])
