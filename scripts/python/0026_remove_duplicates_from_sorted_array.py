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


def main():
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    obj = Solution()
    print(obj.removeDuplicates(nums))

if __name__ == "__main__":
    main()

