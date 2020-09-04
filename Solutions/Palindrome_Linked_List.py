# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        if not head.next.next:
            return head.val == head.next.val
        stack = []
        slow,fast = head,head
        stack.append(slow.val)
        while fast.next and fast.next.next:
            slow = slow.next
            stack.append(slow.val)
            fast = fast.next.next
        if not fast.next:
            stack.pop()
        slow = slow.next
        while slow:
            if slow.val == stack[-1]:
                stack.pop()
                slow = slow.next
            else:
                return False
        return True
head = ListNode(1,ListNode(2,ListNode(2,ListNode(1))))
print(Solution().isPalindrome(head))