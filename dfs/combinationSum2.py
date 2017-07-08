class Solution:
    """
    @param candidates: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, candidates, target):
        # write your code here
        ret = []
        candidates.sort()
        self.helper(ret, candidates, [], 0, target)
        return ret
    def helper(self, ret, candidates, path, k, target):
        if target < 0:
            return
        if target == 0:
            ret.append(path)
        for i in range(k, len(candidates)):
            if i != k and candidates[i] == candidates[i - 1]:
                continue
            self.helper(ret, candidates, path +[candidates[i]], i+1, target - candidates[i])
