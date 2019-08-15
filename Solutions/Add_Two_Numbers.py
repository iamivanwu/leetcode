class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = root = ListNode(0)
        carry = 0
        a = 0
        b = 0
        while l1 != None or l2 != None:
            if (l1):
                a = l1.val
            else:
                a = 0
            if (l2):
                b = l2.val
            else:
                b = 0
            temp = a + b + carry
            carry = int(temp / 10)
            temp = temp - carry * 10
            ans.next = ListNode(temp)
            ans = ans.next
            if (l1 != None):
                l1 = l1.next
            if (l2 != None):
                l2 = l2.next
        if (carry > 0):
            ans.next = ListNode(carry)
            ans = ans.next
        return root.next

# l1 = ListNode(1)
# l1.next = ListNode(8)
# l1.next.next = ListNode(3)

# l2 = ListNode(0)
# l2.next = ListNode(6)
# l2.next.next = ListNode(4)

# sol = Solution()
# ans = sol.addTwoNumbers(l1, l2)
# while ans != None:
#     print (ans.val)
#     ans = ans.next