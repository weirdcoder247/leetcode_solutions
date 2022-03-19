class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        l = len(nums)
        for i in range(l):
            for j in range(i + 1, l):
                if abs(nums[i] - nums[j]) == k:
                    ans += 1
        return ans

def main():
    nums = [1,2,2,1]
    k = 0
    obj = Solution()
    print(obj.countKDifference(nums, k))

if __name__ == "__main__":
    print(main())
