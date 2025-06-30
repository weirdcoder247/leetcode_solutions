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

def main():
    obj = Solution()
    n = int(input("Enter the number: "))
    print(obj.subtractProductAndSum(n))

if __name__ == '__main__':
    main()
