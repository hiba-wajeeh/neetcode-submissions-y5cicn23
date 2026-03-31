# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodesSeen = set()

        while head:
            if head.next not in nodesSeen:
                nodesSeen.add(head.next)
            else:
                return True
            head = head.next
        
        return False