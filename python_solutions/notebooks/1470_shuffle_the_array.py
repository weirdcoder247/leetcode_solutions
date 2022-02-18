class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        for i in range(n - 1):
            nums.insert(2*i + 1, nums[n + i])
            nums.pop(n + i + 1)
        return nums

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = int(len(nums)/2)
    obj = Solution()
    obj.shuffle(nums, n)
