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


    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.previous_node = None
        self.new_root = TreeNode(0)
        self.new_root.right = root
        self.previous_node2 = self.new_root
        
        def convertToIncBST(curr_node):
            # Criteria for outer recursive call which always starts from new_root
            if curr_node and curr_node.left:
                # Save the curr node in a temp pointer called previous_node
                self.previous_node = curr_node
                self.previous_node2.right = curr_node.left
                self.previous_node.left = None
                # Recursive Function to replace while loop
                right_end = self.rightEndNode(self.previous_node2.right)
                if right_end is not None:
                    right_end.right = self.previous_node
                # Reset curr_node to new_root before recursive call
                curr_node = self.new_root
            elif curr_node is None:
                return
            self.previous_node2 = curr_node
            # Outer recursive call for recurring if criteria
            convertToIncBST(curr_node.right)
            
            return self.new_root
                        
        result = convertToIncBST(root)
        return result.right if result is not None else None

    def rightEndNode(self, curr_node):
        if curr_node is None:
            return None
        while curr_node.right is not None:
            curr_node = curr_node.right
        return curr_node


    def leftEndNode(self, curr_node):
        self.end_node = None
        if curr_node.left is not None:
            self.leftEndNode(curr_node.left)
        else:
            self.end_node = curr_node
        return self.end_node


    def kthSmallest(self, root, k):
        nodes = []
        self.solve(root, nodes)
        return nodes[k - 1]


    def solve(self, root, nodes):
        if root == None:
            return
        self.solve(root.left, nodes)
        nodes.append(root.val)
        print(nodes)
        self.prettyPrintTree(root)
        self.solve(root.right, nodes)                        

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        pass
                
def main():
    obj = Solution()
    root = input("Enter the binary tree in string format (e.g., [1,2,3,null,null,4,5]): ")
    node = obj.stringToTreeNode(root)
    obj.prettyPrintTree(node)

if __name__ == "__main__":
    main()

