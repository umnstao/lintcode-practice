class Solution:
    # @param {int[]} nums a mountain sequence which increase firstly and then decrease
    # @return {int} then mountain top
    def mountainSequence(self, nums):
        # Write your code here
        if nums is None or len(nums) == 0:
            return None
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start)/2
            if nums[mid] - nums[mid-1] > 0:
                start = mid
            else:
                end = mid
        return nums[start] if nums[start]>nums[end] else nums[end]
