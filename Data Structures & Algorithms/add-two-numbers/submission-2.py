# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""

        curr = l1
        while curr:
            num1 += str(curr.val)
            curr = curr.next

        curr = l2
        while curr:
            num2 += str(curr.val)
            curr = curr.next
        
        finalNum1 = ""
        finalNum2 = ""

        for i in range(len(num1)-1, -1, -1):
            finalNum1 += num1[i]
        
        for i in range(len(num2)-1, -1, -1):
            finalNum2 += num2[i]

        finalNum1, finalNum2 = int(finalNum1), int(finalNum2)
        newNum = str(finalNum1+finalNum2)
        dummy = ListNode()
        tail = dummy

        for i in range(len(newNum)-1, -1, -1):
            num = int(newNum[i])
            tail.next = ListNode(num)
            tail = tail.next
        
        return dummy.next