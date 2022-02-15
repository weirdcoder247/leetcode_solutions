class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        def reverse(s):
            if len(s) == 0:
                return s
            else:
                return reverse(s[1:]) + s[0]

        if x > 2**31 or x < -2**31:
            return False
        else:
            y = reverse(str(x))
            print(type(y))
            if y[-1] != '-':
                if int(y) == x:
                    return True
                else:
                    return False
            else:
                return False