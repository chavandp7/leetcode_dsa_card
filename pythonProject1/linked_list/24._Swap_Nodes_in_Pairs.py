# 24. Swap Nodes in Pairs
# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem
# without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
from typing import Optional

from linked_list.ListNode import ListNode


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        first = head
        second = first.next

        while first and second:
            temp = first.val
            first.val = second.val
            second.val = temp

            first = second.next
            if first:
                second = first.next

        return head
