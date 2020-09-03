# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    ans = 0
    count = 0
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def find(node: TreeNode):
            if node and self.count < k:                
                find(node.left)
                self.count += 1
                if self.count == k:
                    print(k,node.val)
                    self.ans = node.val
                find(node.right)
        find(root)
        return self.ans
