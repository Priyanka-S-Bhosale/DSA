#https://leetcode.com/problems/remove-linked-list-elements/description/

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        prev = dummy
        curr = head
        
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next
        return dummy.next
