from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        path = []
        self.bfs(root,path,0)
        return path
    def bfs(self, node: TreeNode, path: List[List[int]], level: int):
        if node:
            if len(path) < level+1:
                path.append([node.val])
            else:
                path[level].append(node.val)
            self.bfs(node.left,path,level+1)
            self.bfs(node.right,path,level+1)
        