# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        head1 = headA
        size1 = 0
        while head1:
            head1 = head1.next
            size1 += 1
        head2 = headB
        size2 = 0
        while head2:
            head2 = head2.next
            size2 += 1
        while size1 > size2:
            size1 -= 1
            headA = headA.next
        while size2 > size1:
            size2 -= 1
            headB = headB.next
        while headA and headA != headB:
            headA = headA.next
            headB = headB.next
        return headA
            