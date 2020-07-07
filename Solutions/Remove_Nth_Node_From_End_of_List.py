# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        arr = []
        node = head
        while node != None:
            arr.append(node)
            node = node.next
        if n == len(arr):
            return head.next
        elif n == 1:
            arr[len(arr)-2].next = None
        else:
            arr[len(arr)-1-n].next = arr[len(arr)-1-n+2]
        return head

a = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
a = ListNode(1,ListNode(2))
a = Solution().removeNthFromEnd(a, 1)
while a != None:
    print('v', a.val)
    a = a.next