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
    import ast
    bookings = ast.literal_eval(input("Enter bookings as a list of lists: "))
    n = int(input("Enter n: "))
    obj = Solution()
    return obj.corpFlightBookings(bookings, n)

if __name__ == "__main__":
    print(main())
