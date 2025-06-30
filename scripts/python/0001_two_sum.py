class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if (nums[i] + nums[j]) == target:
                    result = [i,j]
                    return result

def main():
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    obj = Solution()
    print(obj.twoSum(nums, int(input("Enter target: "))))

if __name__ == "__main__":
    main()
