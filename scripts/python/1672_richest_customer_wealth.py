import numpy as np


class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        arr = np.array(accounts)
        return arr.sum(axis=1).max()


if __name__ == '__main__':
    import ast

    accounts = ast.literal_eval(input("Enter accounts as a list of lists: "))
    obj = Solution()
    obj.maximumWealth(accounts)

