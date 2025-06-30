class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [sum([x < y for x in nums]) for y in nums]

if __name__ == '__main__':
    obj = Solution()
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    obj.smallerNumbersThanCurrent(nums)
