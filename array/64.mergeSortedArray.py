class Solution:
    """
    @param A: sorted integer array A which has m elements,
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return: void
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        i = m - 1
        j = n - 1
        for k in reversed(range(len(A))):
            if i < 0:
                A[k] = B[j]
                j -= 1
            elif j < 0:
                A[k] = A[i]
                i -= 1
            elif A[i] < B[j]:
                A[k] = B[j]
                j -= 1
            else:
                A[k] = A[i]
                i -= 1

