# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x=0):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def stringToTreeNode(self, input):
        input = input.strip()
        input = input[1:-1]

        inputValues = [s.strip() for s in input.split(',')]
        root = TreeNode(int(inputValues[0]))
        nodeQueue = [root]
        front = 0
        index = 1
        while index < len(inputValues):
            node = nodeQueue[front]
            front = front + 1

            item = inputValues[index]
            index = index + 1
            if item != "null":
                leftNumber = int(item)
                node.left = TreeNode(leftNumber)
                nodeQueue.append(node.left)

            if index >= len(inputValues):
                break

            item = inputValues[index]
            index = index + 1
            if item != "null":
                rightNumber = int(item)
                node.right = TreeNode(rightNumber)
                nodeQueue.append(node.right)
        return root

    def treeNodeToString(self, root):
        if not root:
            return "[]"
        output = ""
        queue = [root]
        current = 0
        while current != len(queue):
            node = queue[current]
            current = current + 1

            if not node:
                output += "null, "
                continue

            output += str(node.val) + ", "
            queue.append(node.left)
            queue.append(node.right)
        return "[" + output[:-2] + "]"

    def prettyPrintTree(self, node, prefix="", isLeft=True):

        if not node:
            print("Empty Tree")
            return

        if node.right:
            self.prettyPrintTree(node.right, prefix + ("│   " if isLeft else "    "), False)

        print(prefix + ("└── " if isLeft else "┌── ") + str(node.val))

        if node.left:
            self.prettyPrintTree(node.left, prefix + ("    " if isLeft else "│   "), True)

    def deepestLeavesSum(self, root):
        sums = []
        def dfs(node, lvl):
            if lvl == len(sums):
                sums.append(node.val)
            else:
                sums[lvl] += node.val
            if node.left:
                dfs(node.left, lvl+1)
            if node.right:
                dfs(node.right, lvl+1)
        dfs(root, 0)
        return sums[-1]

    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = []
        ans.append(0)
        def xyz(curr_node, parent_even=False, grandparent_even=False):
            if grandparent_even:
                ans[0] += curr_node.val
            if curr_node.left:
                xyz(curr_node.left, curr_node.val % 2 == 0, parent_even)
            if curr_node.right:
                xyz(curr_node.right, curr_node.val % 2 == 0, parent_even)
        xyz(root)

        return ans[0]

    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        ans = []
        ans.append(0)
        def sumRangeBST(curr_node, low, high):
            if low <= curr_node.val <= high:
                ans[0] += curr_node.val
            if curr_node.left:
                sumRangeBST(curr_node.left, low, high)
            if curr_node.right:
                sumRangeBST(curr_node.right, low, high)
        sumRangeBST(root, low, high)
        return ans[0]

    def convertBST2(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        else:
            def greaterBST(ptr, greater_tree):
                greaterBSTSum(root, ptr, greater_tree)
                if ptr.left:
                    greater_tree.left = TreeNode(0)
                    greaterBST(ptr.left, greater_tree.left)
                if ptr.right:
                    greater_tree.right = TreeNode(0)
                    greaterBST(ptr.right, greater_tree.right)

            def greaterBSTSum(curr_node, ptr, greater_tree):
                if curr_node.val >= ptr.val:
                    greater_tree.val += curr_node.val
                if curr_node.left:
                    greaterBSTSum(curr_node.left, ptr, greater_tree)
                if curr_node.right:
                    greaterBSTSum(curr_node.right, ptr, greater_tree)

            greater_tree = TreeNode(0)
            greaterBST(root, greater_tree)

            return greater_tree

    def convertBST(self, root):
        self.addition = 0
        def convert(node):
            if node != None:
                convert(node.right)
                self.addition += node.val
                node.val = self.addition
                convert(node.left)
            return node
        return convert(root)

        
def main():
    obj = Solution()
    root = '[6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]'
    root = '[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]'
    node = obj.stringToTreeNode(root)
    obj.prettyPrintTree(node)
    node = obj.convertBST(node)
    obj.prettyPrintTree(node)
    return node


if __name__ == "__main__":
    main()
