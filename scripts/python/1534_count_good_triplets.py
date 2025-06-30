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
    arr = list(map(int, input("Enter the array (space-separated): ").split()))
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))
    obj = Solution()
    print(obj.countGoodTriplets(arr, a, b, c))

if __name__ == '__main__':
    main()
