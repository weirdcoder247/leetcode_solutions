class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [sum([nums[i] > x for x in nums[i + 1:]]) for i in range(len(nums))]

if __name__ == '__main__':
    obj = Solution()
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    obj.countSmaller(nums)



