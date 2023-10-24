#https://leetcode.com/problems/palindrome-linked-list/

class Solution:

    def isPalindrome(self, head: ListNode) -> bool:

        mid = self.endOfFirst(head)
        secondHead = self.reverse(mid.next)

        res = True
        first_position = head
        second_position = secondHead

        while res and second_position is not None:
            if first_position.val != second_position.val:
                return False
            else:
                first_position = first_position.next
                second_position = second_position.next
        mid.next = self.reverse(secondHead)
        return res

    def reverse(self,head):
            prev = None
            curr = head

            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev

    def endOfFirst(self,head):
        fast = head
        slow = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            
        return slow
