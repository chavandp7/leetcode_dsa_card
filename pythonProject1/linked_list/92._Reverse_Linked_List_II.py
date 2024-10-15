# 92. Reverse Linked List II
# Given the head of a singly linked list and two integers left and right where left <= right,
# reverse the nodes of the list from position left to position right, and return the reversed list.
from typing import Optional

from linked_list.ListNode import ListNode


class Solution:
    def reverse_linked_list(self, head):
        next = prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev = None
        node1 = head

        position = 1
        while node1 and position != left:
            prev = node1
            node1 = node1.next
            position += 1

        if not node1:
            return head

        next = head.next
        node2 = head

        position = 1
        while node2 and position != right:
            node2 = node2.next
            if node2:
                next = node2.next
            position += 1

        if not node2:
            return head

        node2.next = None
        head2 = self.reverse_linked_list(node1)
        if prev:
            prev.next = head2
        node1.next = next

        return head if prev else head2


if __name__ == "__main__":
    solution = Solution()

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    left, right = 3, 3

    # head = ListNode(5)
    # left, right = 1, 1

    head = solution.reverseBetween(head, left, right)
    while head:
        print(head.val, end=" --> ")
        head = head.next
