# 19. Remove Nth Node From End of List
# Given the head of a linked list, remove the nth node from the end of the list and return its head.
from typing import Optional

from linked_list.ListNode import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head

        prev = None
        curr = next = head

        pos = 0
        while next and pos < n:
            next = next.next
            pos += 1

        while next:
            prev = curr
            curr = curr.next
            next = next.next

        if not prev:
            return head.next

        prev.next = curr.next
        return head


if __name__ == "__main__":
    solution = Solution()

    head = ListNode(1)
    # head.next = ListNode(2)
    # head.next.next = ListNode(3)
    # head.next.next.next = ListNode(4)
    # head.next.next.next.next = ListNode(5)

    head = solution.removeNthFromEnd(head, 1)
    while head:
        print(head.val, end=" --> ")
        head = head.next
