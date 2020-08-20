# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        back = []
        s = f = head
        while f.next and f.next.next:
            s = s.next
            f = f.next.next
        last = s
        s = s.next
        last.next = None
        while s:
            last = s
            back.append(s)
            s = s.next
            last.next = None
        s = head
        while s.next:
            temp = s.next
            if back:
                s.next = back.pop()
            s = s.next
            s.next = temp
            s = s.next
        if back:
            s.next = back.pop()