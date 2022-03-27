class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        arr_len = len(arr)
        counter = 0
        for i in range(0, arr_len - 2):
            for j in range(i + 1, arr_len - 1):
                for k in range(j + 1, arr_len):
                    if abs(arr[i] - arr[j]) <= a\
                        and abs(arr[j] - arr[k]) <= b\
                            and abs(arr[i] - arr[k]) <= c:
                        counter += 1
        return counter


def main():
    arr = [3, 0, 1, 1, 9, 7]
    a = 7
    b = 2
    c = 3
    # arr = [1, 1, 2, 2, 3]
    # a = 0
    # b = 0
    # c = 1
    obj = Solution()
    return obj.countGoodTriplets(arr, a, b, c)

if __name__ == '__main__':
    print(main())
