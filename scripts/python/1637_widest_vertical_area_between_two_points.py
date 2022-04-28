from typing import List

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_coords = list(set([x[0] for x in points]))
        x_coords.sort()
        area = [x_coords[i]-x_coords[i-1] for i in range(1, len(x_coords))]
        return max(area)

def main():
    points = [[8,7],[9,9],[7,4],[9,7]]
    points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
    obj = Solution()
    return obj.maxWidthOfVerticalArea(points)
    
if __name__ == "__main__":
    print(main())

