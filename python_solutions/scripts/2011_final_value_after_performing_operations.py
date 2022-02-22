class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        x = 0
        for i in operations:
            if i == "X++":
                x = x + 1
            elif i == "++X":
                x =  x + 1
            elif i == "X--":
                x = x - 1
            elif i == "--X":
                x = x - 1
        return x

if __name__ == '__main__':
    operations = ["X++", "X++", "--X"]
    obj = Solution()
    obj.finalValueAfterOperations(operations)
