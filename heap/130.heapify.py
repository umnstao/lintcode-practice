class Solution:
    # @param A: Given an integer array
    # @return: void
    def heapify(self, A):
        # write your code here
        for i in range(len(A)):
            self.siftup(A,i)

    def siftup(self, A, k):
        while k > 0:
            father = (k-1)/2
            if A[k] > A[father]:
                break
            A[k], A[father] = A[father], A[k]
            k = father


        """
        for i in reversed(range(len(A)/2)):
            self.siftdown(A,i)

    def siftdown(self, A, k):
        while k < len(A):
            smallest = k
            if k*2 + 1 < len(A) and A[k*2+1] < A[smallest]:
                smallest = k*2 + 1
            if k*2 + 2 < len(A) and A[k*2+2] < A[smallest]:
                smallest = k*2 + 2
            if smallest == k:
                break
            A[smallest], A[k] = A[k], A[smallest]

            k = smallest

        """