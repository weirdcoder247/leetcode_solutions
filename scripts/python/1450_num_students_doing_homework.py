class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        student_count = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                student_count += 1
        return student_count

def main():
    startTime = list(map(int, input("Enter start times separated by spaces: ").split()))
    endTime = list(map(int, input("Enter end times separated by spaces: ").split()))
    queryTime = int(input("Enter query time: "))
    obj = Solution()
    return obj.busyStudent(startTime, endTime, queryTime)

if __name__ == '__main__':
    print(main())
