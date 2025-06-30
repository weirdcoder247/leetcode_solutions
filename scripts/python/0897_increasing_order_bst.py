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
#                # Temp pointer to find the end node on right tree from curr_node.left or new_root.right
#                r_end_ptr = self.previous_node2.right
#                # Inner recursive call to reach towards right end node and attach previous node to it's right
#                while(r_end_ptr != None):
#                    if r_end_ptr.right is None:
#                        break
#                    r_end_ptr = r_end_ptr.right
#                # Append previous_node
#                self.prettyPrintTree(r_end_ptr.right)
#                r_end_ptr.right = self.previous_node
#                # Recursive Function to replace while loop
                self.rightEndNode(self.previous_node2.right).right = self.previous_node               
                # Reset curr_node to new_root before recursive call
                curr_node = self.new_root
            elif curr_node is None:
                return
            self.previous_node2 = curr_node
            # Outer recursive call for recurring if criteria
            convertToIncBST(curr_node.right)
            
            return self.new_root
                        
        return convertToIncBST(root).right

    def rightEndNode(self, curr_node):
        self.end_node = None
        if curr_node.right is not None:
            self.rightEndNode(curr_node.right)
        else:
            self.end_node = curr_node
        return self.end_node


#------------------------------------------------------------------------------#
##        hardcoded approach for test usecase
#        # root in 1st interation (1st recursive call)
#        if root and root.left: # recursive until a right node is reached which has a left node != None
#            previous_node = root
#            new_root.right = root.left
#            previous_node.left = None
#            new_root.right.right.right = previous_node # recursive until a right node is reached which has a right node == None (use another pointer for operations on new_root ----> new_root_ptr)
#            self.prettyPrintTree(new_root)
#            self.prettyPrintTree(previous_node)
#        # root in 1st iteration becomes new_root.right in 2nd iteration (or 2nd recursive call)
#        if new_root.right and new_root.right.left:
#            previous_node = new_root.right
#            new_root.right = new_root.right.left
#            previous_node.left = None
#            new_root.right.right = previous_node
#            self.prettyPrintTree(new_root)
#            self.prettyPrintTree(previous_node)
#        # new_root.right from 2nd iteration becomes new_root.right in 3rd iteration (or 3rd recursive call)
#        if new_root.right and new_root.right.left:
#            previous_node = new_root.right
#            new_root.right = new_root.right.left
#            previous_node.left = None
#            new_root.right.right = previous_node
#            self.prettyPrintTree(new_root)
#            self.prettyPrintTree(previous_node)
#        # new_root.right from 3rd iteration becomes new_root.right...7times...right in 4th iteration (or 4th recursive call)
#        if new_root.right.right.right.right.right.right.right and new_root.right.right.right.right.right.right.right.left:
#            previous_node = new_root.right.right.right.right.right.right.right
#            new_root.right.right.right.right.right.right.right = new_root.right.right.right.right.right.right.right.left
#            previous_node.left = None
#            new_root.right.right.right.right.right.right.right.right = previous_node
#            self.prettyPrintTree(new_root)
#            self.prettyPrintTree(previous_node)
#        return new_root.right
        
def main():
    obj = Solution()
    root = input("Enter the binary tree in string format: ")
    root = obj.stringToTreeNode(root)
    root = obj.increasingBST(root)
    obj.prettyPrintTree(root)
    return root

if __name__ == "__main__":
    main()

