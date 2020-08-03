# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        s = slow.next
        slow.next = None
        self.sortList(head)
        self.sortList(s)
        return self.merge(head,s)
    def merge(self,f,s):
        h = m = ListNode()
        while f and s:
            if f.val > s.val:
                m.next = s
                s = s.next
            else:
                m.next = f
                f = f.next
            m = m.next
        if f:
            m.next = f
        if s:
            m.next = s
        return h.next