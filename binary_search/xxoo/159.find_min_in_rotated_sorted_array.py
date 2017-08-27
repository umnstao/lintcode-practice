class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        # write your code here
        if num is None or len(num) == 0:
            return None
        return self.helper(num)
    def helper(self, num):
        # 1. exit
        if len(num) == 1:
            return num[0]
        start = 0
        end = len(num) - 1
        mid = start + (end - start)/2
        leftmin = self.helper(num[0:mid+1]) #2. divide
        rightmin = self.helper(num[mid+1:])
        return min(leftmin,rightmin) #3. conquer

