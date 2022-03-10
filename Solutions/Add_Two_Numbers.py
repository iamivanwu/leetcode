from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        ans = root = ListNode(0)
        carry = 0
        while l1 or l2:
            temp = 0
            if l1:
                temp += l1.val
                l1 = l1.next
            if l2:
                temp += l2.val
                l2 = l2.next
            temp += carry
            ans.next = ListNode(temp % 10)
            ans = ans.next
            carry = (temp) // 10
        if carry:
            ans.next = ListNode(carry)
        return root.next
