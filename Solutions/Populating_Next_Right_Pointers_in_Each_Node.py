# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        start = root
        leaf = [start]
        while leaf:
            child = []
            if leaf[0] == None:
                break
            for i in range(0,len(leaf)):
                if i+1 < len(leaf):
                    leaf[i].next = leaf[i+1]
                else:
                    leaf[i].next = Node('#')
                child.append(leaf[i].left)
                child.append(leaf[i].right)
            leaf = child
        return start