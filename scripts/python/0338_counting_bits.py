class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = []
        for i in range(n + 1):
            ans.append(sum([int(x) for x in list(bin(i)[2:])]))
        return ans


def main():
    obj = Solution()
    n = int(input("Enter n: "))
    return obj.countBits(n)

if __name__ == "__main__":
    print(main())
