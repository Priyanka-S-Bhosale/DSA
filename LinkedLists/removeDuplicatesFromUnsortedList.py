#https://leetcode.com/problems/remove-duplicates-from-an-unsorted-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import defaultdict
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        hashmap = defaultdict(int)
        dummy = ListNode(-1,head)
        curr = head

        while curr:
            hashmap[curr.val] +=1
            curr= curr.next
        prev = dummy

        while head :
            if hashmap[head.val] >1:
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next
        return dummy.next
