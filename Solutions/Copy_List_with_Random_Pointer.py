# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        start = Node(0)
        node = start
        table,ori = {},{}
        index = 0
        temp = head
        while head != None:
            node.next = Node(head.val)
            table[index] = node.next
            ori[index] = head
            node = node.next
            head = head.next
            index += 1
        node = start.next
        head = temp
        while head != None:
            if head.random:
                key = list(ori.values()).index(head.random)
                node.random = table[key]
            node = node.next
            head = head.next
        return start.next