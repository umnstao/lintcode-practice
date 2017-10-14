class Solution:
    """
    @param nums: A list of integers.
    @return: A list of unique permutations.
    """
    def permuteUnique(self, nums):
        # write your code here

        if nums is None:
            return None
        if len(nums) == 0:
            return [[]]
        nums.sort()
        ret = []
        used = [False]*len(nums)
        self.helper(nums, ret, [],used)
        return ret
    def helper(self, nums, ret, path,used):
        if len(path) == len(nums):
            ret.append(path[:])
        for i in range(len(nums)):
            if used[i]:
                continue
            if i > 0 and nums[i] == nums[i-1] and used[i-1] == False:
                continue
            path+=[nums[i]]
            used[i] = True
            self.helper(nums,ret,path,used)
            used[i] = False
            path.pop()
    # 这里used[i-1] == False 更好理解，和之前一样但之前那个没有用的话这个就应该skip
