# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # Check if there are at least k nodes remaining
        count = 0
        curr = head
        while curr and count < k:
            curr = curr.next
            count += 1

        # If there are fewer than k nodes, no need to reverse
        if count < k:
            return head

        # Reverse the group (basic way to reverse linked list)
        prev, curr = None, head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Recursively reverse the remaining groups
        head.next = self.reverseKGroup(curr, k)
        return prev
        