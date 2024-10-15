# 234. Palindrome Linked List
# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
from typing import Optional

from linked_list.ListNode import ListNode


class Solution:
    def get_middle_node(self, head):
        if not head or not head.next:
            return head

        prev = slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        return prev

    def reverse_linked_list(self, head):
        if not head or not head.next:
            return head

        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        middle_node = self.get_middle_node(head)
        head2 = middle_node.next
        middle_node.next = None

        head2 = self.reverse_linked_list(head2)

        while head and head2:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next

        return True


if __name__ == "__main__":
    solution = Solution()

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(1)

    print(solution.isPalindrome(head))
