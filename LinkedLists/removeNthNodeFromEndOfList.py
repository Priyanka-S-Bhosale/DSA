#https://leetcode.com/problems/remove-nth-node-from-end-of-list/

 class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        #create a dummy node to be on the exact node that needs to be deleted
        dummy = ListNode(0, head)
        
        # use 2 ptrs and right should go upto n times ahead of left
        left = dummy
        right = head

        while n>0:
            right = right.next
            n -=1

        #reach left till that node:
        
        while right:
            left = left.next
            right = right.next
        print(left.next.val)
        left.next = left.next.next
        return dummy.next
