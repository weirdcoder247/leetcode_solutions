class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        while(num > 0):
            count += 1
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
        return count

if __name__ == '__main__':
    obj = Solution()
    num = 57
    obj.numberOfSteps(num)
