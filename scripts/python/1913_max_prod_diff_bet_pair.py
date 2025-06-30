class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[-1] * nums[-2] -nums[0] * nums[1]

def main():
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    obj = Solution()
    return obj.maxProductDifference(nums)

if __name__ == '__main__':
    print(main())
