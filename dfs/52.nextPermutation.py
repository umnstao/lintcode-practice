class Solution:
    # @param num :  a list of integer
    # @return : a list of integer
    def nextPermutation(self, num):
        nums = num
        if len(nums) <= 1:
            return nums
        i = len(nums) - 1
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1
        self.swapList(nums, i, len(nums)-1)
        if i != 0:
            j = i
            while nums[j] <= nums[i-1]:
                j+= 1
            nums[j], nums[i-1] = nums[i-1], nums[j]
        return nums

    def swapList(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    [8,3,7,6,5,4]
    [8,3,4,5,6,7]
    [8,4,3,5,6,7]

    [1,7,9,6,4]
    [1,7,4,6,9]
    [1,9,4,6,7]

    [4,5,6]
    [4,6,5]

    [6,5,4,3]
    [3,4,5,6]

