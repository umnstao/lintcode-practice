import heapq
class Solution:

    # @param {int} k an integer
    def __init__(self, k):
        # initialize your data structure here.
        self.minheap = []
        self.size = k
        heapq.heapify(self.minheap)

    # @param {int} num an integer
    def add(self, num):
        # Write your code here
        heapq.heappush(self.minheap,num)
        if len(self.minheap) > self.size:
            heapq.heappop(self.minheap)

    # @return {int[]} the top k largest numbers
    def topk(self):
        # Write your code here
        return sorted(self.minheap, reverse = True)