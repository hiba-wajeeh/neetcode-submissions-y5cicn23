import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        min_heap = []
        
        for num in nums:
            heapq.heappush(min_heap, num)        # Step 2a: Push number
            if len(min_heap) > k:                # Step 2b: Exceed k?
                heapq.heappop(min_heap)          # Pop smallest
        
        return min_heap[0]                       # Step 3-4: Top = kth largest


        