class Solution(object):
    def minRemoveToMakeValid(self, S):
        """
        :type s: str
        :rtype: str
        """
        S, stack = list(S), []
        for i, c in enumerate(S):
            if c == ")":
                if stack: stack.pop()
                else: S[i] = ""
            elif c == "(": stack.append(i)
        for i in stack: S[i] = ""
        return "".join(S)
