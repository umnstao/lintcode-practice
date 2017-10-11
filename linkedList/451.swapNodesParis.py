class Solution:
    """
    @param: head: a ListNode
    @return: a ListNode
    """
    def swapPairs(self, head):
        # write your code here
        cur = head
        dummy = ListNode(-1)
        dummy.next = cur
        prev = dummy
        while cur and cur.next:
            mynext = cur.next
            prev.next = cur.next
            cur.next = mynext.next
            mynext.next = cur
            prev = cur
            cur = cur.next
        return dummy.next



