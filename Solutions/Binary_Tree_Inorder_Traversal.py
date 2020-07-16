from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        return self.search(root,[])
    def search(self,tree,path):
        if not tree:
            return path
        self.search(tree.left,path)
        path.append(tree.val)
        self.search(tree.right,path)
        return path
root = TreeNode(1,None,TreeNode(2,TreeNode(3)))
print(Solution().inorderTraversal(root))