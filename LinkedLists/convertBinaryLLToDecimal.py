#https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description/

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = head.val
        while head.next:
            num = (num << 1) | head.next.val
            head = head.next
        return num
