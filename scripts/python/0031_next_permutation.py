class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
def main():
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    obj = Solution()
    obj.nextPermutation(nums)
    print(nums)

if __name__ == "__main__":
    main()


