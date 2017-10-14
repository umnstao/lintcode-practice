"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the sorted linked list,
                  using constant space complexity.
    """
    def sortList(self, head):
        # write your code here
        if head is None or head.next is None:
            return head
        mid = self.findMiddle(head)
        right = self.sortList(mid.next)
        mid.next =None
        left = self.sortList(head)

        return self.merge(left,right)

    def findMiddle(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def merge(self, head1, head2):
        dummy = ListNode(0)
        tail = dummy
        while head1 and head2:
            if head1.val < head2.val:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next
        if head1:
            tail.next = head1
        if head2:
            tail.next = head2
        return dummy.next