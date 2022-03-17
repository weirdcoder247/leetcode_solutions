class Solution(object):
    def scoreOfParentheses(self, s):
        pwr, ans = 0, 0
        for i in range(1, len(s)):
            if s[i] == "(": pwr += 1
            elif s[i-1] == "(":
                ans += 1 << pwr
                pwr -= 1
            else: pwr -= 1
        return ans


def main():
    # s = "(((())))"
    # s = "()()(())()"
    s = "(()(()))"
    obj = Solution()
    return obj.scoreOfParentheses(s)


if __name__ == '__main__':
    print(main())
