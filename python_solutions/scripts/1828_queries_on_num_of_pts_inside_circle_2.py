class Solution(object):
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        num_queries = len(queries)
        num_pts = len(points)
        res = []
        count = 0
        for i in range(num_queries):
            for j in range(num_pts):
                count += self.pt_inside_circle(points[j], queries[i])
            res.append(count)
            count = 0
        return res



    def pt_inside_circle(self, pt, circle):
        """
        :rtype: Bool
        """
        if (pow(pt[0] - circle[0], 2) + pow(pt[1] - circle[1], 2)) <= pow(circle[2], 2):
            return True
        else:
            return False


if __name__ == '__main__':
    points = [[1,1],[2,2],[3,3],[4,4],[5,5]]
    queries = [[1,2,2],[2,2,2],[4,3,2],[4,3,3]]
    obj = Solution()
    obj.countPoints(points, queries)
