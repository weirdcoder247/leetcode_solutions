from math import sqrt


class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        divs = []
        i = 0
        while(i <= sqrt(num)):
            i += 1
            if num % i == 0:
                divs.append(i)
                if num / i != i:
                    divs.append(num / i)
        divs.remove(num)
        return num == sum(set(divs))

def main():
    num = 28
    num = 496
    obj = Solution()
    return obj.checkPerfectNumber(num)

if __name__ == '__main__':
    print(main())
