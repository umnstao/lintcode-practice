# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param l1: the first list
    # @param l2: the second list
    # @return: the sum list of l1 and l2
    def addLists(self, l1, l2):
        # write your code here
        if l2 is None:
            return l1
        if l1 is None:
            return l2
        cur1 = l1
        cur2 = l2
        dummy = ListNode(-1)
        cur = dummy
        sign = 0
        while cur1 and cur2:
            nodeVal = cur1.val + cur2.val + sign
            if nodeVal >= 10:
                sign = 1
                node = ListNode(nodeVal - 10)
            else:
                sign = 0
                node = ListNode(nodeVal)
            cur.next = node
            cur = cur.next
            cur1 = cur1.next
            cur2 = cur2.next
        while cur1:
            nodeVal = cur1.val + sign
            if nodeVal >= 10:
                sign = 1
                node = ListNode(nodeVal - 10)
            else:
                sign = 0
                node = ListNode(nodeVal)
            cur.next = node
            cur = cur.next
            cur1 = cur1.next
        while cur2:
            nodeVal = cur2.val + sign
            if nodeVal >= 10:
                sign = 1
                node = ListNode(nodeVal - 10)
            else:
                sign = 0
                node = ListNode(nodeVal)
            cur.next = node
            cur = cur.next
            cur2 = cur2.next
        if sign == 1:
            cur.next = ListNode(1)
        return dummy.next