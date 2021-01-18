# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        res = node = ListNode(0)
        node.next = head
        while node.next and node.next.next:
            a = node.next
            b = a.next
            node.next,a.next,b.next = b,b.next,a
            node = a
        return res.next