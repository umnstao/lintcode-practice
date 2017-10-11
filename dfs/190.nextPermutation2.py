class Solution:
    # @param nums: a list of integer
    # @return: return nothing (void), do not return anything, modify nums in-place instead
    def nextPermutation(self, nums):
        # write your code here


        if not nums:
            return None
        if len(nums) <= 1:
            return nums

        i = len(nums) - 1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        self.swapList(nums, i, len(nums) - 1)

        if i > 0:
            j = i
            # compare j with i-1
            while nums[i-1] >= nums[j]:
                j += 1
            nums[i-1], nums[j] = nums[j], nums[i-1]

    def swapList(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    """
    [1,5,4,3]
    [1,3,4,5]
    [3,1,4,5]
    """