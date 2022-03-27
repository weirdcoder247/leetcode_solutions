class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [sum([x < y for x in nums]) for y in nums]

if __name__ == '__main__':
    obj = Solution()
    nums = [8, 1, 2, 2, 3]
    obj.smallerNumbersThanCurrent(nums)
