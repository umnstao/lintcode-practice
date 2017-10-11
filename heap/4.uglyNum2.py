class Solution:
    """
    @param {int} n an integer.
    @return {int} the nth prime number as description.
    """
    def nthUglyNumber(self, n):
        # write your code here

        ugly = [0]*n
        ugly[0] =1
        i2, i3, i5 = 0, 0, 0
        fac2 = ugly[i2]*2
        fac3 = ugly[i3]*3
        fac5 = ugly[i5]*5

        for i in range(1,n):
            next_ugly = min(fac2, fac3, fac5)
            ugly[i] = next_ugly
            if next_ugly == fac2:
                i2 += 1
                fac2 = ugly[i2]*2
            if next_ugly == fac3:
                i3+= 1
                fac3 = ugly[i3]*3
            if next_ugly == fac5:
                i5 += 1
                fac5 = ugly[i5]*5

        return ugly[n-1]

