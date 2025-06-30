from typing import List

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_coords = list(set([x[0] for x in points]))
        x_coords.sort()
        area = [x_coords[i]-x_coords[i-1] for i in range(1, len(x_coords))]
        return max(area)

def main():
    import ast
    points = ast.literal_eval(input("Enter points as a list of lists: "))
    obj = Solution()
    return obj.maxWidthOfVerticalArea(points)
    
if __name__ == "__main__":
    print(main())

