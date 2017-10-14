class Solution:
    # @param {double} x a double
    # @return {double} the square root of x
    def sqrt(self, x):
        # Write your code here
        start = 0.0
        end = x
        eps = 1e-10
        if x < 1:
            end = 1.0
        while end - start > eps:
            mid = start + (end - start)/2
            if mid * mid < x:
                start = mid
            elif mid * mid == x:
                return mid
            else:
                end = mid
        return start