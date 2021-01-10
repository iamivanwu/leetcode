# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        arr = []
        while head:
            last = head
            head = head.next
            last.next = None
            arr.append(last)
        s = ListNode(0)
        start = s
        for i in range(0,len(arr)):
            if i == k-1:
                s.next = arr[len(arr)-k]
            elif i == len(arr)-k:
                s.next = arr[k-1]
            else:
                s.next = arr[i]
            s = s.next
        return start.next