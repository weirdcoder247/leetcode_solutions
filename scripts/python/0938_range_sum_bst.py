# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, x: int):
        self.val: int = x
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None


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

def main():
    obj = Solution()
    root_str = input("Enter the binary tree in string format: ")
    low = int(input("Enter the low value: "))
    high = int(input("Enter the high value: "))
    node = obj.stringToTreeNode(root_str)
    return obj.rangeSumBST(node, low, high)

if __name__ == "__main__":
    print(main())

