class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        score = 0
        stack = []
        # stack = [s[0]]
        mult = 1
        temp = 0
        for i in s:
            if i == "(" and stack == []:
                stack.append(i)
            elif i == ")" and stack[-1] == "(":
                # Assign Constant 1
                temp = 1
                stack.append(i)
            elif i == ")" and stack[-1] == ")":
                # Change multiplier by 2x
                mult *= 2
                stack.append(i)
            elif i == "(" and stack[-1] == ")":
                # Update score and reset parameters
                score += temp * mult
                temp = 0
                mult = 1
                stack.append(i)
            elif i == "(" and stack[-1] == "(":
                pass
            else:
                # Update stack
                stack.append(i)
        return score + temp * mult

def main():
    s = input("Enter the parentheses string: ")
    obj = Solution()
    return obj.scoreOfParentheses(s)


if __name__ == '__main__':
    print(main())
