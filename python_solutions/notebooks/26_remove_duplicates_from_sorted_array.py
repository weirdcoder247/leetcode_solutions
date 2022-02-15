class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Find length of input array
        nums_len = len(nums)

        # Boolean flag for termination of loops
        flag = False

        # Algorithm
        for i in range(len(nums)):
            if i == len(set(nums)):
                break
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    nums[i+1] = nums[j]
                    break
                else:
                    continue
            if flag:
                break
        return len(set(nums)), nums



# nums = [1,1,2]
# nums = [1,1,1,2,2,2]
nums = [0,0,1,1,1,2,2,3,3,4]
len(set(nums))
obj = Solution()
obj.removeDuplicates(nums)