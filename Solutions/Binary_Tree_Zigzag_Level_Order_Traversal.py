from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        path = []
        self.zigzag(root,path,0)
        for i in range(0,len(path)):
            if i % 2 == 1:
                path[i] = reversed(path[i])
        return path
    def zigzag(self, node: TreeNode, path: List[List[int]], level: int):
        if node:
            if len(path) < level + 1:
                path.append([node.val])
            else:
                path[level].append(node.val)
            self.zigzag(node.left,path,level+1)
            self.zigzag(node.right,path,level+1)
