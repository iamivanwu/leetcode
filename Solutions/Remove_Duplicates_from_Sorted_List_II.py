from re import L
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        new = ListNode(-101)
        start = new
        count, value = 1, head.val
        head = head.next
        while head:
            if head.val == value:
                count += 1
            else:
                if count == 1:
                    new.next = ListNode(value)
                    new = new.next
                count = 1
                value = head.val
            head = head.next
        if count == 1:
             new.next = ListNode(value)
        return start.next
