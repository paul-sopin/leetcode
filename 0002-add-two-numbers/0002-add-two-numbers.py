# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = l1
        node2 = l2
        sum_ll = ListNode()
        node = sum_ll
        extra = 0
        while node1 or node2:
            if node1 and node2:
                node.next = ListNode(node1.val + node2.val + extra)
                node1 = node1.next
                node2 = node2.next
            elif node1:
                node.next = ListNode(node1.val + extra)
                node1 = node1.next
            elif node2:
                node.next = ListNode(node2.val + extra)
                node2 = node2.next
            node = node.next
            if node.val >= 10:
                node.val -= 10
                extra = 1
            else:
                extra = 0
        if extra == 1:
            node.next = ListNode(1)
        return sum_ll.next