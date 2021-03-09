# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            return TreeNode(v,root)
        start = head = root
        level = 1
        bfs = [head]
        while level < d - 1:
            temp = []
            for node in bfs:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            bfs = temp
            level += 1
        for node in bfs:
            temp = node.left
            node.left = TreeNode(v,temp)
            temp = node.right
            node.right = TreeNode(v,None,temp)
        return start