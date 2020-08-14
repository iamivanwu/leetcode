# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        last = None
        while head:
            n = head.next
            head.next = last
            last = head
            head = n
        return last
