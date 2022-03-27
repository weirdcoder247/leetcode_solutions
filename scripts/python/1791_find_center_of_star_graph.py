class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        for i in range(2):
            for j in range(2):
                if edges[0][i] == edges[1][j]:
                    return edges[0][i]
