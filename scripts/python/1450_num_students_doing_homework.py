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
    startTime = [1, 2, 3]
    endTime = [3, 2, 7]
    queryTime = 4
    obj = Solution()
    return obj.busyStudent(startTime, endTime, queryTime)

if __name__ == '__main__':
    print(main())
