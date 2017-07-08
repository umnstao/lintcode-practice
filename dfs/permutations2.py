class Solution:
    """
    @param nums: A list of integers.
    @return: A list of unique permutations.
    """
    def permuteUnique(self, nums):
        # write your code here

        ret = []
        if nums is None:
            return ret
        nums.sort() #  有重复就要sort
        used = [False]*len(nums)
        self.helper(nums, [], 0, ret, used)
        return ret

    def helper(self, nums, path, k, ret, used):
        if len(path) == len(nums):
            ret.append(path[:])
        for i in range(len(nums)):
            if used[i]:
                continue
            if used[i-1] is False and i!= k and nums[i] == nums[i-1]:
                continue
            used[i] = True
            self.helper(nums, path +[nums[i]], 0, ret, used)
            used[i] = False

