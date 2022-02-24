class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [sum([nums[i] > x for x in nums[i + 1:]]) for i in range(len(nums))]

if __name__ == '__main__':
    obj = Solution()
    # nums = [8, 1, 2, 2, 3]
    # nums = [5, 2, 6, 1]
    nums = [-1]
    obj.countSmaller(nums)



