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
    nums = [0,1,2,3,4]
    index = [0,1,2,2,1]
    return obj.createTargetArray(nums, index)

if __name__ == "__main__":
    print(main())
