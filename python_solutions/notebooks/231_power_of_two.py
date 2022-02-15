class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0 or n>=2**31:
            return False
        n10 = floor(log(n,2)*10**10)/10**10
        if n10.is_integer() or n==1:
            return True
        else:
            return False
