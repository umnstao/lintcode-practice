class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        if nums == None  :
            return nums
        if len(nums) == 0:
            return [[]]
        ret = []
        self.helper(nums, ret, [], 0)
        return ret

    def helper(self, nums, ret, path, index):
        if len(path) == len(nums):
            ret.append(path[:])

        for i in range(index, len(nums)):
            if nums[i] in path:
                continue
            path += [nums[i]]
            self.helper(nums,ret,path,0)
            path.pop()