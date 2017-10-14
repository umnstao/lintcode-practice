class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return None
        sum = 0
        maxVal = -float('inf')
        for i in range(len(nums)):
            sum += nums[i]
            maxVal = max(maxVal, sum)
            sum = max(0, sum)
        return maxVal