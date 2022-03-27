class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        import numpy as np
        arr = np.array(grid)
        row_max = arr.max(axis=1)
        col_max = arr.max(axis=0)
        n = len(grid)
        m = max([len(x) for x in grid])
        res = 0
        for i in range(n):
            for j in range(m):
                res += (min(row_max[i], col_max[j]) - grid[i][j])

        return res


def main():
    obj = Solution()
    grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]

    return obj.maxIncreaseKeepingSkyline(grid)

if __name__ == "__main__":
    print(main())
