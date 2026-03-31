# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        #find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 

        
        second = slow.next 
        slow.next = None 
        prev = None
        while second: #reversing the second portion of linked list
            temp = second.next 
            second.next = prev 
            prev = second 
            second = temp
        
        #merge two halves 
        first, second = head, prev 
        while second:
            temp1, temp2 = first.next, second.next 
            first.next = second 
            second.next = temp1 
            first = temp1 
            second = temp2
        
        