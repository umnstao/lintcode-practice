# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head: the list
    # @param k: rotate to the right k places
    # @return: the list after rotation
    def rotateRight(self, head, k):
        # write your code here
        if head is None:
            return None
        leng = 0
        cur = head
        while cur:
            leng += 1
            cur = cur.next
        k = k % leng
        if k == 0:
            return head

        dummy1 = ListNode(0)
        dummy1.next = head
        fast = head
        cur = head
        while k > 0:
            fast = fast.next
            k = k - 1
        while fast:
            fast = fast.next
            dummy1 = dummy1.next
            cur = cur.next
        dummy1.next = None

        dummy = ListNode(-1)
        dummy.next = cur
        while cur.next:
            cur = cur.next
        cur.next = head
        return dummy.next

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head: the list
    # @param k: rotate to the right k places
    # @return: the list after rotation
    def rotateRight(self, head, k):
        # write your code here
        if head is None:
            return None
        leng = 0
        cur = head
        while cur:
            leng += 1
            cur = cur.next
        k = k % leng
        if k == 0:
            return head

        prev = None
        cur = head
        offset = leng - k
        while offset > 0:
            offset -= 1
            prev = cur
            cur = cur.next
        prev.next = None

        dummy = ListNode(-1)
        dummy.next = cur
        while cur.next:
            cur = cur.next
        cur.next = head
        return dummy.next

        """

