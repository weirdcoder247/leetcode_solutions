class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rep_allowance = 2
        ra_c = 0
        ra_c_total = 0

        # jugaad
        jugaad_flag = False
        from collections import Counter
        if Counter(nums)[max(nums)] == 1:
            jugaad_flag = True
        else:
            jugaad_flag = False

        # for i in range(len(nums)):
        i = 0
        while(i <= (len(nums) - 1)):
            ra_c = 1
            if (i > 0) and (i < (len(nums) - 1)):
                ra_c_total = ra_c_total + ra_c
            elif (i >= (len(nums) - 1)) and jugaad_flag:
                ra_c_total = ra_c_total + 1
                break
            if len(nums) <= 2:
                return len(nums)

            for j in range(i + 1, len(nums)):
                print("nums:", nums, i, j)
                print("ra_c:", ra_c)
                print("ra_c_total:", ra_c_total)
                # print(ra_c_total)
                if (nums[j] > nums[i]) and (ra_c <= rep_allowance):
                    nums[i + ra_c] = nums[j]
                    i = i + ra_c
                    if (i == (len(nums) - 1)) and (j == (len(nums) - 1)):
                        i = i - 1
                    ra_c_total = ra_c_total + ra_c
                    ra_c = 1
                    continue
                elif (nums[j] > nums[i]) and (ra_c > rep_allowance):
                    nums[i + rep_allowance] = nums[j]
                    i = i + rep_allowance
                    ra_c_total = ra_c_total + rep_allowance
                    ra_c = 1
                    continue
                elif (nums[j] == nums[i]):
                    nums[i + 1] = nums[j]
                    ra_c = ra_c + 1
                    continue
                i = i + 1
            i = i + 1
        return ra_c_total, nums




nums = [1,1,2] # correct
nums = [1,1,1,2,2,2] # correct
nums = [0,0,1,1,1,2,2,3,3,4] # correct
nums = [0,0,1,1,1,2,2,3,3,3] # correct
nums = [0,0,1,1,1,1,2,3,3] # correct
nums = [1,1,1,2,2,3] # correct
nums = [1,1]
nums = [1,1,1]

obj = Solution()
obj.removeDuplicates(nums)