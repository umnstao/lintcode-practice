class Solution:
    # @param {int[]} nums an array of integers
    # @return {int} the number of unique integers
    def deduplication(self, nums):
        # Write your code here
        if nums is None or len(nums) == 0:
            return 0
        nums.sort()
        j = 1
        for i in xrange(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
        return j