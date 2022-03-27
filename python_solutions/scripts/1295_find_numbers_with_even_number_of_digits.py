class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum([len(str(x)) % 2 == 0 for x in nums])

def main():
    nums = [12,1,2,445,1290]
    obj = Solution()
    return obj.findNumbers(nums)

if __name__ == "__main__":
    print(main())
