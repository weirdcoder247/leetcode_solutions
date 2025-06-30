from collections import Counter


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




def main():
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    obj = Solution()
    print(obj.removeDuplicates(nums))

if __name__ == "__main__":
    main()