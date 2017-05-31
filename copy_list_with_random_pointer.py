# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        
        if head is None:
            return head
        head2 = head
        dummy = RandomListNode(-1)
        copyHead = dummy
        
        # copy all nodes
        while head :
            Node = RandomListNode(head.label)
            copyHead.next = Node
            head = head.next
            copyHead = copyHead.next
        
        # save all pointers in a hashSet
        hashSet = {}
        head = head2
        while head :
            val = head.label
            pointed = head.random
            hashSet[val] = pointed
            head = head.next
        
        # copy the pointer
        newHead = dummy.next
        while newHead:
            val = newHead.label
            newHead.random = hashSet[val]
            newHead = newHead.next
        
        return dummy.next
            
            