class Solution:
    """
    @param nums {int[]} n array of Integer
    @param target {int} = nums[index1] + nums[index2]
    @return {int[]} [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # Write your code here


        """
        if nums is None or len(nums) == 0:
            return 0
        left = 0
        right = len(nums) - 1
        while left < right:
            if  nums[left] + nums[right] == target:
                return [left+1, 1+right]
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1

        """
        if numbers is None or len(numbers) == 0:
            return None
        # Method : hash set, numbers are not sorted.
        mySet = {}
        for i in xrange(len(numbers)):
            if numbers[i] in mySet:
                return [mySet[numbers[i]]+1, i+1]
            else:
                mySet[target - numbers[i]] = i
