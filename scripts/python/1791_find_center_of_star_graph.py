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

def main():
    import ast
    edges = ast.literal_eval(input("Enter edges as a list of lists (e.g., [[1,2],[2,3]]): "))
    obj = Solution()
    print(obj.findCenter(edges))

if __name__ == "__main__":
    main()
