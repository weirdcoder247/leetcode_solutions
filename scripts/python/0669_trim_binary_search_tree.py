# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def trimBST(self, root, low, high):
        return "This is trimBST"


def main():
	low = 1
	high = 5
	root = TreeNode(0, 1, 2)
	obj = Solution()
	return obj.trimBST(root, low, high)
	

if __name__ == "__main__":
	print(main())

