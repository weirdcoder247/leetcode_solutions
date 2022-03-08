class Solution(object):
        def cellsInRange(self, s):
            """
            :type s: str
            :rtype: List[str]
            """
            s = s.split(":")
            return [
                chr(i) + str(j) \
                for i in range(ord(s[0][0]), ord(s[1][0]) + 1) \
                for j in range(int(s[0][1:]), int(s[1][1:]) + 1)
            ]

def main():
    obj = Solution()
    s = "A10:B12"
    return obj.cellsInRange(s)

if __name__ == "__main__":
    print(main())
