class Solution:
    # @param {int[]} nums an integer array
    # @param {int} target an integer
    # @return {int} the difference between the sum and the target
    def twoSumClosest(self, nums, target):
        # Write your code here
        if nums is None and len(nums) == 0:
            return None
        nums.sort()
        left = 0
        right = len(nums) - 1
        ret = float('inf')
        while left < right:
            val = nums[left] + nums[right]
            diff = abs(val - target)
            if diff == 0:
                return 0
            if diff < ret:
                ret = diff
            if val < target:
                left += 1
            if val > target:
                right -= 1
        return ret