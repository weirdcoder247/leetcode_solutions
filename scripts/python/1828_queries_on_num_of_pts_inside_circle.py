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
        # for i in range(num_queries):
        #     count = 0
        #     for j in range(num_pts):
        #         if self.pt_inside_circle(points[j], [queries[i][0], queries[i][1]], queries[i][2]):
        #             count += 1
        #     res.append(count)
        for i in range(num_queries):
            for j in range(num_pts):
                count += self.pt_inside_circle(points[j], [queries[i][0], queries[i][1]], queries[i][2])
            res.append(count)
            count = 0
        return res



    def pt_inside_circle(self, pt, circle_center, radius):
        """
        :rtype: Bool
        """
        if (pow(pt[0] - circle_center[0], 2) + pow(pt[1] - circle_center[1], 2)) <= pow(radius, 2):
            return True
        else:
            return False


if __name__ == '__main__':
    points = [[1,1],[2,2],[3,3],[4,4],[5,5]]
    queries = [[1,2,2],[2,2,2],[4,3,2],[4,3,3]]
    obj = Solution()
    obj.countPoints(points, queries)
