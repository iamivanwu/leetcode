# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        m = []
        self.dfs(root,m)
        return max(m)
    def dfs(self,node: TreeNode,m: list):
        if not node:
            return 0
        l = self.dfs(node.left,m)
        r = self.dfs(node.right,m)
        ma = max(node.val,node.val+l,node.val+r,node.val+l+r)
        # ma contain node left right
        m.append(ma)
        # return must choose only one side
        return max(node.val,node.val+l,node.val+r)
tree = TreeNode(1,TreeNode(2),TreeNode(3))
print(Solution().maxPathSum(tree))