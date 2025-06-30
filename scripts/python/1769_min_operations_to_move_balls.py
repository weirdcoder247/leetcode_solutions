class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        boxes = [int(x) for x in boxes]
        _iter = range(len(boxes))

        return [sum([abs(j - i) for j in _iter if boxes[j] == 1]) for i in _iter]

def main():
    obj = Solution()
    boxes = input("Enter boxes as a string of 0s and 1s: ")
    return obj.minOperations(boxes)

if __name__ == "__main__":
    print(main())
