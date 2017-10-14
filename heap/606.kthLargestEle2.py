class Solution:
    # @param nums {int[]} an integer unsorted array
    # @param k {int} an integer from 1 to n
    # @return {int} the kth largest element
    def kthLargestElement2(self, nums, k):
        # Write your code here
        import heapq
        minheap = []
        for i in range(len(nums)):
            heapq.heappush(minheap, nums[i])
            if len(minheap) > k:
                heapq.heappop(minheap)
        return heapq.heappop(minheap)

        # complexity O(k + (n-k)*logk)