import heapq

class Solution:
    '''
    @param {int[]} nums an integer array
    @param {int} k an integer
    @return {int[]} the top k largest numbers in array
    '''
    def topk(self, nums, k):
        # Write your code here
        minheap = []
        for i in range(len(nums)):
            heapq.heappush(minheap, nums[i])
            if len(minheap) > k:
                heapq.heappop(minheap)
        return sorted(minheap, reverse=True)