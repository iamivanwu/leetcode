# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.dfs(root,0)
    def dfs(self, node: TreeNode, depth: int):
        if node:
            depth += 1
            return max(self.dfs(node.left,depth),\
            self.dfs(node.right,depth))
        else:
            return depth