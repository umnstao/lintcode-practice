class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers that's previous permuation
    """
    def previousPermuation(self, nums):
        # write your code here
        if len(nums) <= 1:
            return nums
        i = len(nums) - 1
        while i > 0 and nums[i-1] <= nums[i]:
            i-=1
        self.swapList(nums, i, len(nums) - 1)
        if i > 0:
            j = i
            while nums[j] >= nums[i-1]:
                j += 1
            nums[i-1], nums[j] = nums[j], nums[i-1]
        return nums

    def swapList(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
    [8,7,6,5]
    [8,7,6,5]
    [8,7,5,6]

    [9,3,4,5,6]
    [9,6,5,4,3]
    [6,9,5,4,3]

    [7,3,4,5,8,9]
    [7,9,8,5,4,3]
    [5,9,8,7,4,3]