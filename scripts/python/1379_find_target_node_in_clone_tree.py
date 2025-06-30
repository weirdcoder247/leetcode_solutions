from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x=0):
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

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        result = self.findTargetInClone(target, cloned)
        if result is None:
            raise ValueError("Target node not found in cloned tree")
        return result

    def findTargetInClone(self, target: TreeNode, root: TreeNode) -> Optional[TreeNode]:
        self.target_node = None
        def findTN(curr_node):
            if target.val == curr_node.val:
                self.target_node = curr_node
            if curr_node.left:
                findTN(curr_node.left)
            if curr_node.right:
                findTN(curr_node.right)
        findTN(root)
        if self.target_node is None:
            raise ValueError("Target node not found in tree")
        return self.target_node

    def findTargetNode(self, target: int, root: TreeNode) -> TreeNode:
        self.target_node = None
        def findTN(curr_node):
            if target == curr_node.val:
                self.target_node = curr_node
            if curr_node.left:
                findTN(curr_node.left)
            if curr_node.right:
                findTN(curr_node.right)
        findTN(root)
        if self.target_node is None:
            raise ValueError("Target node not found in tree")
        return self.target_node

def main():
    tree = input("Enter the binary tree in string format: ")
    target = int(input("Enter the target value: "))
    obj = Solution()
    original = obj.stringToTreeNode(tree)
    cloned = obj.stringToTreeNode(tree)
    target_node = obj.findTargetNode(target, original)
    return obj.getTargetCopy(original, cloned, target_node)

if __name__ == "__main__":
    print(main())

