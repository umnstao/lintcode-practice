class Solution:
    # @param {int[]} nums an integer array
    # @return nothing, do this in-place
    def moveZeroes(self, nums):
        # Write your code here
        i = 0
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        for k in range(j, len(nums)):
            nums[k] = 0