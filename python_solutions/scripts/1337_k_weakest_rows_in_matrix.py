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
    mat = [[1,1,0,0,0], [1,1,1,1,0], [1,0,0,0,0], [1,1,0,0,0], [1,1,1,1,1]]
    k = 3
    obj = Solution()
    return obj.kWeakestRows(mat, k)

if __name__ == '__main__':
    print(main())
