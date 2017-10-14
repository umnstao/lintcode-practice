class Solution:
    # @param nums {int[]} a list of integers
    # @param k {int} size of window
    # @return {int[]} the sum of element inside the window at each moving
    def winSum(self, nums, k):
        # Write your code here
        ret = []
        if nums is None or len(nums) == 0 or len(nums) <k :
            return ret
        prefixnums = nums[:]
        for i in range(1,len(prefixnums)):
            prefixnums[i] += prefixnums[i-1]
        ret.append(prefixnums[k-1])
        for i in range(k,len(prefixnums)):
            val = prefixnums[i] - prefixnums[i-k]
            ret.append(val)
        return ret



