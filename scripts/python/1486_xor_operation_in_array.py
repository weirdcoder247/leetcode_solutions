class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        nums = []
        for i in range(n):
            nums.append(start + 2 * i)
        ans = 0
        for i in range(0, n):
            ans = ans ^ nums[i]
        return ans

if __name__ == '__main__':
    n = int(input("Enter n: "))
    start = int(input("Enter start: "))
    obj = Solution()
    obj.xorOperation(n, start)
