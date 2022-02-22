class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        # Import Package
        import numpy as np

        arr = np.array(accounts)
        return arr.sum(axis = 1).max()


if __name__ == '__main__':
    accounts = [[1, 2, 6], [1, 2, 3]]
    obj = Solution()
    obj.maximumWealth(accounts)

