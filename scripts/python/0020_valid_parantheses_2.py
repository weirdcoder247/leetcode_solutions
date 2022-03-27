class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open = "([{"
        close = ")]}"
        stack = []
        valid_check = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for i in s:
            if i in open:
                stack.append(i)
            elif i in close and stack != []:
                if stack.pop() != valid_check[i]:
                    return False
            else:
                return False
        if stack == []:
            return True
        else:
            return False

def main():
    s = "([])"
    obj = Solution()
    return obj.isValid(s)

if __name__ == "__main__":
    print(main())
