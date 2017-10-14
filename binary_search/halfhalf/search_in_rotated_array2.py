class Solution:
    """
    @param A : an integer ratated sorted array and duplicates are allowed
    @param target : an integer to be searched
    @return : a boolean
    """
    def search(self, A, target):
        # write your code here

        if A is None or len(A) == 0:
            return False
        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = start + (end-start)/2
            if target > A[len(A) - 1]:
                if A[mid] > target:
                    end = mid
                elif A[mid] == target:
                    return True
                elif A[mid] < A[end]:
                    end = mid
                elif A[mid] > A[end]:
                    start = mid
                else:
                    end -= 1
            elif target < A[len(A) - 1]:
                if A[mid] < target:
                    start = mid
                elif A[mid] == target:
                    return True
                elif A[mid] < A[end]:
                    end = mid
                elif A[mid] > A[end]:
                    start = mid
                else:
                    end -= 1
            else:
                return True
        return False
        """
        if A is None or len(A) == 0:
            return False
        for i in xrange(len(A)):
            if A[i] == target:
                return True

        return False
        """