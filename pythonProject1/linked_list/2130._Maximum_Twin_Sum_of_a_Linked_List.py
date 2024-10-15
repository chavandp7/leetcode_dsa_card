# 2130. Maximum Twin Sum of a Linked List
# In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as
# the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.
# For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2.
# These are the only nodes with twins for n = 4.
# The twin sum is defined as the sum of a node and its twin.
# Given the head of a linked list with even length, return the maximum twin sum of the linked list.
from typing import Optional

from linked_list.ListNode import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def find_middle_node(self, first, second):

        while first and second:
            first = first.next
            second = second.next
            if second:
                second = second.next

        return first

    def reverse_linked_list(self, head):
        if not head:
            return head

        curr = head
        prev = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev

    def pairSum(self, head: Optional[ListNode]) -> int:
        first = head
        second = head.next

        if not second.next:
            return first.val + second.val

        head2 = self.find_middle_node(first, second)
        head2 = self.reverse_linked_list(head2)
        ans = 0

        while head and head2:
            ans = max(ans, head.val + head2.val)
            head = head.next
            head2 = head2.next

        return ans


if __name__ == "__main__":
    solution = Solution()

    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(18)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(3)

    print(solution.pairSum(head))
