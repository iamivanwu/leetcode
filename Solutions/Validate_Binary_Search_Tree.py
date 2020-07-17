# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        p = []
        self.bfs(root,p)
        if not p:
            return True
        for i in range(1, len(p)):
            if p[i-1] >= p[i]:
                return False
        return True
    def bfs(self, node: TreeNode, path: list):
        if node:
            self.bfs(node.left,path)
            path.append(node.val)
            self.bfs(node.right,path)