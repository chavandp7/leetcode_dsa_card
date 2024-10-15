# 82. Remove Duplicates from Sorted List II
# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers
# from the original list. Return the linked list sorted as well.
from enum import unique
from typing import Optional

from linked_list.ListNode import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        node = ListNode(-200)
        node.next = head

        curr = head
        prev = head = node

        while curr:
            val = curr.val
            node = curr.next
            unique = True

            while node and node.val == val:
                unique = False
                node = node.next

            if unique:
                prev.next = curr
                prev = curr
                curr = node
            else:
                prev.next = node
                curr = node

        return head.next


if __name__ == "__main__":
    solution = Solution()

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    # head.next.next.next = ListNode(4)
    # head.next.next.next.next = ListNode(5)

    head = solution.deleteDuplicates(head)
    while head:
        print(head.val, end=" --> ")
        head = head.next
