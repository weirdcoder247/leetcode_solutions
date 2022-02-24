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
        jugaad_flag_2 = False
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

            if len(set(nums)) == 1:
                return 2

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
                    if j == (len(nums) - 1):
                        ra_c_total = ra_c_total + ra_c
                        jugaad_flag_2 = True
                        break
                    continue
                elif (nums[j] > nums[i]) and (ra_c > rep_allowance):
                    nums[i + rep_allowance] = nums[j]
                    i = i + rep_allowance
                    ra_c_total = ra_c_total + rep_allowance
                    ra_c = 1
                    if j == (len(nums) - 1):
                        ra_c_total = ra_c_total + ra_c
                        jugaad_flag_2 = True
                        break
                    continue
                elif (nums[j] == nums[i]):
                    nums[i + 1] = nums[j]
                    ra_c = ra_c + 1
                    if (i == len(nums)-2) and (j == len(nums)-1):
                        ra_c_total = ra_c_total + ra_c
                    if (j == len(nums) - 1):
                        if ra_c <= rep_allowance:
                            ra_c_total = ra_c_total + ra_c
                        else:
                            ra_c_total = ra_c_total + rep_allowance
                        jugaad_flag_2 = True
                        break
                    continue
                i = i + 1
            if jugaad_flag_2:
                break
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
nums = [1,2,2]
nums = [0,0,1,1,1,1,2,3,3]
nums = [1,2,2,2]
nums = [1,1,1,1,2,2,3]
nums = [0,0,0,0,3]
nums = [-50,-50,-49,-49,-48,-48,-48,-48,-47,-46,-46,-46,-45,-44,-44,-43,-43,-43,-42,-41,-39,-39,-38,-37,-37,-36,-35,-34,-33,-33,-33,-32,-30,-29,-29,-29,-28,-27,-26,-26,-25,-25,-25,-25,-25,-24,-23,-23,-22,-22,-22,-21,-21,-20,-18,-16,-15,-15,-14,-13,-12,-11,-10,-10,-10,-9,-7,-7,-7,-7,-7,-6,-5,-5,-5,-5,-4,-4,-2,-2,0,0,2,2,2,3,3,4,5,5,7,7,8,8,9,9,10,10,11,11,12,12,12,13,13,14,14,14,14,14,15,16,16,16,16,16,17,17,18,19,19,20,20,20,21,21,22,23,26,26,26,27,27,28,28,28,28,29,29,30,30,31,32,33,34,35,36,36,37,37,38,38,38,38,39,40,40,41,41,41,41,42,42,43,43,43,43,43,44,45,45,45,46,46,47,47,47,48,48,49,50]

obj = Solution()
obj.removeDuplicates(nums)