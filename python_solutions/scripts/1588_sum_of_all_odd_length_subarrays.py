class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        sum_subarr = 0
        l = len(arr)
        odd_arr_len = 1 # to be increased by 2 after every iteration until equal to or less than l
        while(odd_arr_len <= l):
            i = 0
            while(i + odd_arr_len < l + 1):
                sum_subarr += sum(arr[i: i + odd_arr_len])
                i += 1
            odd_arr_len += 2
        return sum_subarr


def main():
    arr = [1,4,2,5,3]
    # arr = [10,11,12]
    # arr = [1,2]
    obj = Solution()
    return obj.sumOddLengthSubarrays(arr)

if __name__ == '__main__':
    print(main())
