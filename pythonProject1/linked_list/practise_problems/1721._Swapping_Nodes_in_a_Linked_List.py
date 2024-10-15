# 1721. Swapping Nodes in a Linked List
# You are given the head of a linked list, and an integer k.
#
# Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node
# from the end (the list is 1-indexed).
from typing import Optional

from linked_list.ListNode import ListNode


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # find second node
        curr = head
        pos = 1

        while curr and pos < k:
            curr = curr.next
            pos += 1
        first = curr

        # find second node
        curr = head
        pos = 0
        while curr and pos < k:
            curr = curr.next
            pos += 1
        second = head
        while curr:
            curr = curr.next
            second = second.next

        temp = first.val
        first.val = second.val
        second.val = temp
        return head


if __name__ == "__main__":
    solution = Solution()

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    head = solution.swapNodes(head, 3)
    while head:
        print(head.val, end=" --> ")
        head = head.next
