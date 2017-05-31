class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def totalOccurrence(self, A, target):
        # Write your code here
        if A is None or len(A) == 0:
            return 0
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
            return 0
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
        return last - first + 1