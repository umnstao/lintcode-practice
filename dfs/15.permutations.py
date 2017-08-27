class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        if nums is None:
            return None
        if len(nums) == 0:
            return [[]]
        ret = []
        self.helper(nums, ret, [])
        return ret
    def helper(self, nums, ret, path):
        if len(path) == len(nums):
            ret.append(path[:])
        for i in range(len(nums)):
            if nums[i] in path:
                continue
            self.helper(nums,ret,path + [nums[i]])