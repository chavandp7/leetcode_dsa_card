# 1290. Convert Binary Number in a Linked List to Integer
# Given head which is a reference node to a singly-linked list. The value of each node in the linked list is
# either 0 or 1. The linked list holds the binary representation of a number.
#
# Return the decimal value of the number in the linked list.
#
# The most significant bit is at the head of the linked list.
from linked_list.ListNode import ListNode


class Solution:
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

    def getDecimalValue(self, head: ListNode) -> int:
        head = self.reverse_linked_list(head)

        ans = 0
        power_of_2 = 1
        while head:
            ans = ans + head.val * power_of_2
            power_of_2 *= 2
            head = head.next

        return ans


if __name__ == "__main__":
    solution = Solution()

    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(1)

    print(solution.getDecimalValue(head))
