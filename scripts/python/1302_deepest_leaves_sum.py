class Solution:
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

def main():
    import json
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    def build_tree(nodes):
        if not nodes:
            return None
        vals = [None if v is None else v for v in nodes]
        root = TreeNode(vals[0]) if vals[0] is not None else None
        queue = [root]
        i = 1
        while queue and i < len(vals):
            node = queue.pop(0)
            if node is not None:
                # Left child
                if i < len(vals):
                    if vals[i] is not None:
                        node.left = TreeNode(int(vals[i]))
                        queue.append(node.left)
                    else:
                        node.left = None
                    i += 1
                # Right child
                if i < len(vals):
                    if vals[i] is not None:
                        node.right = TreeNode(int(vals[i]))
                        queue.append(node.right)
                    else:
                        node.right = None
                    i += 1
        return root
    arr = json.loads(input("Enter tree as a list (e.g. [1,2,3,null,4]): ").replace('null', 'null').replace('None', 'null'))
    # Convert 'null' or None to Python None
    arr = [None if x == None or (isinstance(x, str) and x.lower() == 'null') else x for x in arr]
    root = build_tree(arr)
    obj = Solution()
    print(obj.deepestLeavesSum(root))

if __name__ == "__main__":
    main()
