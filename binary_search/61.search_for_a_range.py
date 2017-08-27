class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        if A is None or len(A) == 0:
            return [-1,-1]
        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = start + (end - start)/2
            if A[mid] < target:
                start = mid
            else:
                end = mid
        if A[start] == target:
            first = start
        elif A[end] == target:
            first = end
        else:
            return [-1,-1]
        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = start + (end - start)/2
            if A[mid] <= target:
                start = mid
            else:
                end = mid
        if A[end] == target:
            last = end
        elif A[start] == target:
            last = start
        return [first, last]
