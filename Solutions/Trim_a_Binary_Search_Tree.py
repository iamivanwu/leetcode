# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        def dfs(parent,node):
            if node:
                if node.val < low:
                    if parent.val == -1:
                        parent.right = node.right
                    else:
                        parent.left = node.right
                    dfs(node,node.right)
                elif node.val > high:
                    parent.right = node.left
                    dfs(node,node.left)
                else:
                    dfs(node,node.left)
                    dfs(node,node.right)
        parent = TreeNode(-1)
        parent.right = root
        dfs(parent,root)
        return parent.right