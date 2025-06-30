class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        return max(set(list(n)))


if __name__ == '__main__':
    n = input("Enter the number as a string: ")
    obj = Solution()
    obj.minPartitions(n)
