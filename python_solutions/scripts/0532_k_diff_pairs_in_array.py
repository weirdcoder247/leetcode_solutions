class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0: return 0
        result, lookup = set(), set()
        for num in nums:
            if num-k in lookup:
                result.add(num-k)
            if num+k in lookup:
                result.add(num)
            lookup.add(num)
        return len(result)

def main():
    nums = [3,1,4,1,5]
    k = 2
    obj = Solution()
    print(obj.findPairs(nums, k))

if __name__ == "__main__":
    print(main())
