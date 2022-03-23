class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        result = [0] * (n + 1)
        print(result)
        for i, j, k in bookings:
            result[i-1] += k
            result[j] -= k
        for i in range(1, n + 1):
            result[i] += result[i-1]
            print(result)
        result.pop()
        return result

def main():
    bookings = [[1,2,10],[2,3,20],[2,5,25]]
    n = 5
    # bookings = [[2,2,30],[2,2,45]]
    # n = 2
    obj = Solution()
    return obj.corpFlightBookings(bookings, n)

if __name__ == "__main__":
    print(main())
