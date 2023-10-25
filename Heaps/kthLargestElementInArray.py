#https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)

        n = len(nums)

        for i in range(n):
            val = nums[i]
            heapq.heappush(heap, val)
            if len(heap)>k:
                heapq.heappop(heap)
        return heap[0]
