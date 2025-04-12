# 2130. Maximum Twin Sum of a Linked List

# In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

#     For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.

# The twin sum is defined as the sum of a node and its twin.

# Given the head of a linked list with even length, return the maximum twin sum of the linked list.


from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0
        if head.next and not head.next.next:
            return head.val + head.next.val

        # iterate through the linked list at rate normal and 2x speed to get to the end sooner
        half_speed = head
        head_copy = head
        while head.next.next:
            half_speed = half_speed.next
            head = head.next.next
        # now, half_speed is halfway through the list,
        # and head is at the end

        prev = None
        # reverse half of list
        while half_speed: # head of list to reverse
            tmp = half_speed.next
            half_speed.next = prev
            prev = half_speed
            half_speed = tmp

        # at this point, we now have a reversed list from the end to the middle starting at half_speed
        # and a normal list starting at head_copy from the start to the middle
        max_val = 0
        while head_copy and prev:
            val = head_copy.val + prev.val
            max_val = max(val, max_val)
            head_copy = head_copy.next
            prev = prev.next
        return max_val
