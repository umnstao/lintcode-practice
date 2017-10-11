"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
import heapq
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        if not lists:
            return None
        dummy = ListNode(-1)
        cur = dummy
        minheap = []
        for ll in lists:
            if ll:
                heapq.heappush(minheap, (ll.val, ll))
        while minheap:
            node = heapq.heappop(minheap)[1]
            cur.next = node
            cur = cur.next
            if cur.next:
                heapq.heappush(minheap, (cur.next.val, cur.next))
        return dummy.next

