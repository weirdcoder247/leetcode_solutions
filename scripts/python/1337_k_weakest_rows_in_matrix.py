import scipy.stats as ss

class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        mat = list(ss.rankdata([sum(x) for x in mat]))
        mat = [[mat[i], i] for i in range(len(mat))]
        mat.sort()
        return mat

def main():
    import ast
    mat = ast.literal_eval(input("Enter matrix as a list of lists: "))
    k = int(input("Enter k: "))
    obj = Solution()
    return obj.kWeakestRows(mat, k)

if __name__ == '__main__':
    print(main())
