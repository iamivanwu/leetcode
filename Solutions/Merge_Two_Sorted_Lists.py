# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = ListNode()
        head = a
        while l1 != None or l2 != None:
            if l1 == None:
                a.next = l2
                break
            elif l2 == None:
                a.next = l1
                break
            elif l1.val >= l2.val:
                a.next = ListNode(l2.val)
                l2 = l2.next
            else:
                a.next = ListNode(l1.val)
                l1 = l1.next
            a = a.next
        return head.next

a = ListNode(1,ListNode(2,ListNode(4)))
b = ListNode(1,ListNode(3,ListNode(4)))
c = Solution().mergeTwoLists(a,b)
while c != None:
    print(c.val)
    c = c.next