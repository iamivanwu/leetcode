from turtle import st
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        start = head
        count = 0
        while head:
            count += 1
            if not head.next:
                head.next = start
                break
            head = head.next
        head = new = start
        for i in range(count):
            if (count - i - 1) % count == k % count:
                new = head.next
                head.next = None
                break
            head = head.next
        return new
