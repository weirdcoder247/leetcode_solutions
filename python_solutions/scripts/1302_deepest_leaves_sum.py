# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

    def create_list(self, root):
        """
        :type root: TreeNode
        :rtype: List[]
        """
        cur_node = root
        left = cur_node.left
        right = cur_node.left
        tree_list = [cur_node.val]
        level = 0
        while(type(left) is type(TreeNode()) or type(right) is type(TreeNode())):
            level += 1
            if left is None:
                tree_list.append(left)
            else:
                tree_list.append(left.val)
        return tree_list

    def tree_depth(self, root):
        """
        """
        cur_node = root
        if cur_node.left is None and cur_node.right is None:
            return 1
        else:
            return 1 + self.tree_depth(cur_node)




if __name__ == '__main__':
    obj = Solution()
    root = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(7)), TreeNode(5)), TreeNode(3, None, TreeNode(6, None, TreeNode(8))))
    # root = TreeNode(1, TreeNode(2), TreeNode(4))
    # root = TreeNode(1)
    # [1,2,3,4,5,null,6,7,null,null,null,null,8]
    obj.deepestLeavesSum(root)
    obj.create_list(root)