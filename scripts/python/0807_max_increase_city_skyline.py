import numpy as np


class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
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
    import ast
    grid = ast.literal_eval(input("Enter grid as a list of lists: "))
    obj = Solution()
    return obj.maxIncreaseKeepingSkyline(grid)


if __name__ == "__main__":
    print(main())
