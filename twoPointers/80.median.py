class Solution:
    """
    @param nums: A list of integers.
    @return: An integer denotes the middle number of the array.
    """
    def median(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return None
        if len(nums)%2 == 0:
            med = len(nums)/2
        else:
            med = len(nums)/2 + 1

        return self.helper(nums, 0, len(nums)-1, med)

    def helper(self, nums, start, end, med):
        if start == end:
            return nums[start]
        pivot = nums[(start+end)/2]
        left = start
        right = end
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if start + med - 1 <= right:
            return self.helper(nums, start, right, med)
        if start + med - 1 >= left:
            return self.helper(nums, left, end, med - (left - start))
        return nums[right + 1]
