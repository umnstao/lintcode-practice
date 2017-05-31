class Solution:
    #@param A: An integers list.
    #@return: return any of peek positions.
    def findPeak(self, A):
        # write your code here
        if A is None or len(A) == 0:
            return None
        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = start + (end - start)/2
            if A[mid] - A[mid - 1] > 0:
                start = mid
            else:
                end = mid
        if A[start] > A[end]:
            return start
        else:
            return end


