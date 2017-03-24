class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):
        # write your code here
        
        if A is None or len(A) == 0 :
             return -1
        
        start = 0
        end = len(A) - 1
        
        while start + 1 < end:
            mid = start + (end - start)/2
            if target == A[end]:
                return end
                
            if A[mid] > A[end] and target < A[end]:
                start = mid
            elif A[mid] > A[end] and target > A[end]:
                if A[mid] > target:
                    end = mid
                else:
                    start = mid
            
            elif A[mid] <=A[end] and target > A[end]:
                end = mid
            elif A[mid] <= A[end] and target < A[end]:
                if A[mid] > target:
                    end = mid
                else:
                    start = mid
        
        if A[start] == target :
            return start
        if A[end] == target:
            return end
        return -1
                