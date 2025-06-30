class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        good_pair_counter = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    good_pair_counter = good_pair_counter + 1
        return good_pair_counter


if __name__ == '__main__':
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    obj = Solution()
    obj.numIdenticalPairs(nums)