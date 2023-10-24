#https://leetcode.com/problems/intersection-of-two-linked-lists/

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # pA = headA
        # pB = headB

        # while pA != pB:
        #     pA = headB if pA is None else pA.next
        #     pB = headA if pB is None else pB.next
        
        # return pA 

        pA = headA
        pB = headB

        while pA != pB:
            pA = pA.next if pA is not None else headB
            pB = pB.next if pB is not None else headA
        
        return pA
