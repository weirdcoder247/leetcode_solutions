class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        round_parantheses = 0
        box_parantheses = 0
        curly_parantheses = 0
        for i in s:
            if i == "(":
                round_parantheses += 1
            elif i == ")":
                round_parantheses -= 1
            elif i == "[":
                box_parantheses += 1
            elif i == "]":
                box_parantheses -= 1
            elif i == "{":
                curly_parantheses += 1
            else:
                curly_parantheses -= 1
        if round_parantheses == box_parantheses == curly_parantheses == 0:
            return True
        else:
            return False


def main():
    s = "(){}[]("
    obj = Solution()
    return obj.isValid(s)

if __name__ == "__main__":
    print(main())
