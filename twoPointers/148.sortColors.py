class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        if nums is None or len(nums) <= 1:
            return
        left = 0
        right = len(nums) - 1
        cur = 0
        while cur <= right:
            if nums[cur] == 1:
                cur += 1
            elif nums[cur] == 0:
                nums[left], nums[cur] = nums[cur], nums[left]
                left += 1
                cur += 1
            else:
                nums[right], nums[cur] = nums[cur], nums[right]
                right -= 1
            #print nums

        # the condition is between cur and right. left has no relation with right
        # condition must be <=, because all right of 'right' is 2, the right points
        # to 0 probably, left may also point to this 0.

        # [0,0,0,1,1,1,1,0,2,2]
        # the left of left are all zeroes
        # the right of right are all 2's
        # the left/itself of cur are 1s and 2s.
