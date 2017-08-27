class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        # write your code here
        nums = num
        if nums is None or len(nums) == 0:
            return None
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start)/2
            if nums[mid] > nums[end]:
                start = mid
            elif nums[mid] < nums[end]:
                end = mid
            else:
                end -= 1
            #print nums[end]
        if nums[start] < nums[end]:
            return nums[start]
        else:
            return nums[end]
# mid compared to end (instead of the last one). Reason is that the first one
#and the last one might be duplicate number.