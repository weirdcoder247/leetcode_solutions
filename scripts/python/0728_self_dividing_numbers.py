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
            flag = True
            for j in digits:
                if j == 0 or i % j != 0:
                    flag = False
                    break
            if flag:
                sdn_list.append(i)
        return sdn_list


def main():
    left = int(input("Enter left: "))
    right = int(input("Enter right: "))
    obj = Solution()
    return obj.selfDividingNumbers(left, right)

if __name__ == "__main__":
    print(main())
