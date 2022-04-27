from typing import Optional

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

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

    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.val == root.left.val + root.right.val

def main():
    obj = Solution()
    root = '[10,4,6]'
    root = obj.stringToTreeNode(root)
    return obj.checkTree(root)

if __name__ == "__main__":
    print(main())

