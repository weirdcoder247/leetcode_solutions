class Solution:
    def deepestLeavesSum(self, root: TreeNode):
        sums = []
        def dfs(node: TreeNode, lvl: int):
            if lvl == len(sums): sums.append(node.val)
            else: sums[lvl] += node.val
            if node.left: dfs(node.left, lvl+1)
            if node.right: dfs(node.right, lvl+1)
        dfs(root, 0)
        return sums[-1]
