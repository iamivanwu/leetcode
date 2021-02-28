# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        self.arr = {}
        def find(node, level):
            flag = True
            if node:
                if not self.arr.get(level):
                    self.arr[level] = []
                else:
                    if self.arr[level][-1] < node.val and level%2:
                        return False
                    elif self.arr[level][-1] > node.val and not level%2:
                        return False
                self.arr[level].append(node.val)
                if node.val%2 == level%2:
                    return False
                flag = flag and find(node.left, level+1)
                flag = flag and find(node.right, level+1)
            return flag

        return find(root, 0)