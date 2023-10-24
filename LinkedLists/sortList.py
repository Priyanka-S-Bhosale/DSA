# https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hq = []
        
        curr = head
        while curr:
            heapq.heappush(hq, curr.val)
            curr = curr.next
        
        dummy = ListNode()
        
        curr = dummy
        while hq:
            val = heapq.heappop(hq)
            curr.next = ListNode(val)
            curr = curr.next
            
        return dummy.next
