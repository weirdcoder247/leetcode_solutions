from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x=0, left=None, right=None):
        self.val: int = x
        self.left: Optional['TreeNode'] = left
        self.right: Optional['TreeNode'] = right

class Solution:
    def trimBST(self, root, low, high):
        return "This is trimBST"


def main():
	low = int(input("Enter low: "))
	high = int(input("Enter high: "))
	root_str = input("Enter the binary tree in string format: ")
	# You may want to implement a stringToTreeNode function for real BSTs
	# For now, just create a dummy root as before if you don't have one
	root = TreeNode(0, 1, 2)  # Replace with actual parsing if available
	obj = Solution()
	return obj.trimBST(root, low, high)
	

if __name__ == "__main__":
	print(main())

