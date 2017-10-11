class Solution:
    """
    @param: head: a ListNode
    @param: val: An integer
    @return: a ListNode
    """
    def removeElements(self, head, val):
        # write your code here
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        cur = head
        while cur:
            if cur.val == val:
                cur = cur.next
                prev.next = cur
            else:
                prev = cur
                cur = cur.next
        return dummy.next


