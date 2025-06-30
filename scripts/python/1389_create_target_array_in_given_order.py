class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        target = []
        while(index != []):
            target.insert(index.pop(0), nums.pop(0))
        return target

def main():
    obj = Solution()
    nums = list(map(int, input("Enter nums separated by spaces: ").split()))
    index = list(map(int, input("Enter index separated by spaces: ").split()))
    return obj.createTargetArray(nums, index)

if __name__ == "__main__":
    print(main())
