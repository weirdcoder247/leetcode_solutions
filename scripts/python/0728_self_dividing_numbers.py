class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        sdn_list = []
        for i in range(left, right + 1):
            digits = [int(x) for x in list(str(i))]
            for j in digits:
                flag = True
                if j is 0 or i % j != 0:
                    flag = False
                    break
            if flag:
                sdn_list.append(i)
        return sdn_list


def main():
    left = 1
    right = 22
    left = 47
    right = 85
    obj = Solution()
    return obj.selfDividingNumbers(left, right)

if __name__ == "__main__":
    print(main())
