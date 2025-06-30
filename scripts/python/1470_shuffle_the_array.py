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
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    n = int(len(nums)/2)
    obj = Solution()
    obj.shuffle(nums, n)
