# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        table = {root: None}
        while not p in table or not q in table:
            node = stack.pop()
            if node.left:
                table[node.left] = node
                stack.append(node.left)
            if node.right:
                table[node.right] = node
                stack.append(node.right)
        p_path = [p]
        target = p
        while table[target]:
            p_path.append(table[target])
            target = table[target]
        while q not in p_path:
            q = table[q]
        return q