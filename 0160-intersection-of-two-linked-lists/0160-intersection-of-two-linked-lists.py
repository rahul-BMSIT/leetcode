# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        count1 = 0
        count2 = 0
        temp1 = headA
        temp2 = headB

        while temp1 or temp2:
            if temp1:
                count1 = count1 + 1
                temp1 = temp1.next
            if temp2:
                count2 = count2 + 1
                temp2 = temp2.next
        
        count = count1 - count2

        if count < 0:
            while count != 0:
                headB = headB.next
                count = count + 1
        else:
            while count != 0:
                headA = headA.next
                count = count - 1
        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return headA
       