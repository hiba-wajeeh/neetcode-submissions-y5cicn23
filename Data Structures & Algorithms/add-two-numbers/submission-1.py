# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        digits1 = []
        digits2 = []

        curr = l1
        while curr:
            digits1.append(str(curr.val))
            curr = curr.next

        curr = l2
        while curr:
            digits2.append(str(curr.val))
            curr = curr.next

        # reverse and convert
        num1 = int("".join(digits1[::-1]))
        num2 = int("".join(digits2[::-1]))

        newNum = str(num1 + num2)

        dummy = ListNode()
        tail = dummy

        # build result in reverse order
        for digit in reversed(newNum):
            tail.next = ListNode(int(digit))
            tail = tail.next

        return dummy.next