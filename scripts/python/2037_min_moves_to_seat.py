class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        seats.sort()
        students.sort()
        min_moves = 0
        for i in range(len(seats)):
            min_moves += abs(seats[i] - students[i])
        return min_moves

def main():
    seats = list(map(int, input("Enter seats separated by spaces: ").split()))
    students = list(map(int, input("Enter students separated by spaces: ").split()))
    obj = Solution()
    return obj.minMovesToSeat(seats, students)

if __name__ == '__main__':
    print(main())
