# 83. Remove Duplicates from Sorted List
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
# Return the linked list sorted as well.
from typing import Optional

from linked_list import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        first = head

        while first:
            second = first

            while second and first.val == second.val:
                second = second.next

            first.next = second
            first = second

        return head
