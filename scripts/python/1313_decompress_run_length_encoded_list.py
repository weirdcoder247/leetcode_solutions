class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = [nums[i] for i in range(len(nums)) if i % 2 == 0]
        val = [nums[i] for i in range(len(nums)) if i % 2 == 1]
        res = []
        i = 0
        while(i <= (len(val) - 1)):
            res += [val[i]] * freq[i]
            i += 1
        return res
        # return [res += [val[i]] * freq[i] for i in range(len(val) - 1)]


if __name__ == '__main__':
    obj = Solution()
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    obj.decompressRLElist(nums)
