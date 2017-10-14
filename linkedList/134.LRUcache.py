class LinkedNode:
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        # write your code here
        self.cache = {}
        self.head = LinkedNode(None,'head')
        self.tail = LinkedNode(None,'tail')
        self.capacity = capacity
        self.head.next = self.tail
        self.tail.prev = self.head


    def deleteNode(self, node):
        del self.cache[node.key]
        node.prev.next = node.next
        node.next.prev = node.prev

    def insertNew(self, newNode):
        last = self.tail.prev
        last.next = newNode
        self.tail.prev = newNode
        newNode.next = self.tail
        newNode.prev = last

    # @return an integer
    def get(self, key):
        # write your code here
        if key not in self.cache:
            return -1
        node = self.cache[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        self.insertNew(node)
        return node.value

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        # write your code here
        if key in self.cache:
            self.deleteNode(self.cache[key])
        newNode = LinkedNode(key,value)
        self.cache[key] = newNode
        if len(self.cache) > self.capacity:
            self.deleteNode(self.head.next)
        self.insertNew(newNode)