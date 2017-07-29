class Solution:
    #@param A and B: sorted integer array A and B.
    #@return: A new sorted integer array
    def mergeSortedArray(self, A, B):
        # write your code here
        lenA = len(A)
        lenB = len(B)
        idxA = 0
        idxB = 0
        ret = []
        while idxA < lenA  and idxB < lenB:
            if A[idxA] < B[idxB]:
                ret.append(A[idxA])
                idxA += 1
            else:
                ret.append(B[idxB])
                idxB += 1

        while idxA < len(A):
            ret.append(A[idxA])
            idxA += 1
        while idxB < len(B):
            ret.append(B[idxB])
            idxB += 1

        return ret
