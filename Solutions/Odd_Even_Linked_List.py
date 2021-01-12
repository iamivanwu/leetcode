# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        start = odd = ListNode(0)
        estart = even = ListNode(0)
        oddFlag = True
        while head:
            temp = head
            head = head.next
            temp.next = None
            if oddFlag:
                odd.next = temp
                odd = odd.next
            else:
                even.next = temp
                even = even.next
            oddFlag = not oddFlag
        odd.next = estart.next
        return start.next