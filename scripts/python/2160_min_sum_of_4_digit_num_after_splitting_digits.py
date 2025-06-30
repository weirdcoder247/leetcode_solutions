class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = list(str(num))
        min_sum = 9999
        for i in range(3):
            s1 = int(num[i] + num[i + 1]) + int(num[i - 2] + num[i - 1])
            s2 = int(num[i] + num[i + 1]) + int(num[i - 1] + num[i - 2])
            s3 = int(num[i + 1] + num[i]) + int(num[i - 2] + num[i - 1])
            s4 = int(num[i + 1] + num[i]) + int(num[i - 1] + num[i - 2])
            min_sum = min(min_sum, s1, s2, s3, s4)

        return min_sum



if __name__ == '__main__':
    obj = Solution()
    num = int(input("Enter a 4-digit number: "))
    obj.minimumSum(num)
