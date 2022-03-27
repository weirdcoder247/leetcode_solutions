class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        ans = []
        while(popped != []):
            if ans != [] and popped[0] == ans[-1]:
                ans.pop()
                popped.pop(0)
            elif pushed != []:
                ans.append(pushed.pop(0))
            else:
                return False
        if ans == []:
            return True
        else:
            return False

