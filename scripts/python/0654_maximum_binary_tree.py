from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x=0):
        self.val = x
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

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        self.new_root = TreeNode()
        def construct(nums: List[int], node: TreeNode):
            max_val = max(nums)
            left_sub = []
            right_sub = []
            val = nums[0]
            while(val != max_val):
                left_sub.append(nums.pop(0))
                val = nums[0]
            node.val = nums.pop(0)
            while(nums != []):
                right_sub.append(nums.pop(0))
            if left_sub != []:
                # recursive call with new_root.left and left_sub passed as arguments
                node.left = TreeNode()
                construct(left_sub, node.left)
            if right_sub != []:
                # recursive call with new_root.right and right_sub passed as arguments
                node.right = TreeNode()
                construct(right_sub, node.right)
        # Outer call to the recursive function with the new_root and original nums list passed
        construct(nums, self.new_root)
        self.prettyPrintTree(self.new_root)
        return self.new_root
            

def main():
    obj = Solution()
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    return obj.constructMaximumBinaryTree(nums)
    

if __name__ == "__main__":
    print(main())

