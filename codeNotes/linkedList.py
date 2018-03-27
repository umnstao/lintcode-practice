"""
This is to summarize all important codes about linked list.

1. First start with the definition.

class ListNode:

    def __init__(self, val, next = None):
        self.val = val
        self.next = next

"""

# reverse a linked List
class Reverse:
    """
    paramter is head
    """
    def reverse(self, head):
        prev = None
        cur = head
        while cur:
            myNext = cur.next
            cur.next = prev
            prev = cur
            cur  = myNext
        return prev #prev.next = None

# merge lists
class Merge:
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(-1)
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l2 is None else l2
        return dummy.next

    def mergeKsortedLists(self, lists):
        import heapq
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
            if node.next:
                heapq.heappush(minheap, (node.next.val, node.next))

# delete a node
class Delete:
    def deleteElementsVal(self, head, val):
        dummy = ListNode(-1)
        dummy.next = head
        cur = head
        prev = dummy
        while cur:
            if cur.val == val:
                cur = cur.next
                prev.next = cur
            else:
                prev = cur
                cur = cur.next
        return dummy.next

    def deleteElementPos1(self, head, n):
        # n from the head
        dummy = ListNode(-1)
        dummy.next = head
        cur = head
        prev = dummy
        while n > 0:
            n -= 1
            prev = prev.next
        prev.next = prev.next.next
        return dummy.next
        """
        example:
        1->2->3->4->5->None n = 4, remove 4
        """


    def deleteElementPos2(self, head, n):
        # n from the end
        dummy = ListNode(-1)
        dummy.next = head
        cur = head
        prev = dummy

        fast = head
        for _ in range(n):
            fast = fast.next
        while fast:
            cur = cur.next
            prev = prev.next
            fast = fast.next
        prev.next = cur.next
        return dummy.next
        """
        example:
        1->2->3->4->5->None n = 4, remove 2
        fast -> 5
        go in while
            cur = 2
            prev = 1
            fast = None
        """

    def deleteAllButOneDuplicates(self, head):
        dummy = ListNode(-1)
        dummy.next = head
        cur = head
        prev = dummy
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur = cur.next
                prev.next = cur
            else:
                prev = cur
                cur = cur.next
        return dummy.next

    def deleteAllDuplicates(self, head):
        dummy = ListNode(-1)
        dummy.next = head
        cur = head
        prev = dummy
        while cur and cur.next:
            while cur and cur.next and cur.val == cur.next.val:
                cur = cur.next
            if prev.next != cur:
                cur = cur.next
                prev.next = cur
            else:
                prev = cur
                cur = cur.next

# node position
class Position:
    def middle(self, head):
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    """
    example: 1->2->3->4->None   slow = 3
    example: 1->2->3->4->5->None   slow = 3
    """
    def NthToLast(self, head, n):
        fast = head
        cur = head
        for _ in range(n):
            fast = fast.next
        while fast:
            fast = fast.next
            cur = cur.next
        return cur

    def NthToBegin(self, head, n):
        dummy = ListNode(-1)
        dummy.next = head
        cur = head
        prev = dummy
        while n > 0:
            n -= 1
            prev = prev.next
        return prev.next






