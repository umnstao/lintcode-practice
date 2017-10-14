class Solution:
    # @param nums {int[]} an array of integer
    # @param target {int} an integer
    # @return {int} an integer
    def twoSum5(self, nums, target):
        # Write your code here
        if nums is None or len(nums) ==0:
            return 0
        nums.sort()
        left = 0
        right = len(nums) - 1
        ret = 0
        while left < right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                ret += right - left
                left += 1
        return ret
