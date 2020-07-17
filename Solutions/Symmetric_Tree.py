# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.compare(root.left,root.right)
    def compare(self, left: TreeNode, right: TreeNode):
        if left and right:
            if left.val != right.val:
                return False
            flag = self.compare(left.left,right.right) and \
            self.compare(left.right,right.left)
            return flag
        if left and not right:
            return False
        if right and not left:
            return False
        if not right and not left:
            return True