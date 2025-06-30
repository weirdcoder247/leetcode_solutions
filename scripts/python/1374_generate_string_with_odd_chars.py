from random import randint

class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n % 2 == 1:
            return "a" * n
        else:
            return "a" * (n - 1) + "b"

def main():
    n = int(input("Enter n: "))
    obj = Solution()
    return obj.generateTheString(n)

if __name__ == '__main__':
    print(main())
