from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def mergeTwo(a: ListNode,b: ListNode):
            res = head = ListNode(0)
            while a and b:
                if a.val <= b.val:
                    head.next = ListNode(a.val)
                    a = a.next
                else:
                    head.next = ListNode(b.val)
                    b = b.next
                head = head.next
            if not a:
                while b:
                    head.next = ListNode(b.val)
                    b = b.next
                # head.hext = b
            else:
                while a:
                    head.next = ListNode(a.val)
                    a = a.next
            return res.next
        if not lists:
            return None
        while len(lists) > 1:
            a = lists.pop(0)
            if lists:
                b = lists.pop(0)
            lists.append(mergeTwo(a,b))
        return lists[0]