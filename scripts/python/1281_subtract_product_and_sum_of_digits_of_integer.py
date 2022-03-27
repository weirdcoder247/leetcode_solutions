class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        prod = 1
        n = [int(x) for x in list(str(n))]
        for i in n:
            prod *= i
        return prod - sum(n)


if __name__ == '__main__':
    obj = Solution()
    n = 10
    obj.subtractProductAndSum(n)
