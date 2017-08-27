class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        # write your code here
        # if every number can be used multiple times, then there should not be any duplicates in the problem.

        result = []
        path = []
        self.removeDuplicates(candidates)
        candidates.sort()
        self.helper(candidates, target, path, result, 0)
        return result
    # remove the duplicates in candidate
    def removeDuplicates(self, candidates):
        j = 1
        for i in xrange(1, len(candidates)):
            if candidates[i] != candidates[i-1]:
                candidates[j] = candidates[i]
                j += 1
        candidates = candidates[:j]


    def helper(self, candidates, leftTarget, path, result, index):
        if leftTarget < 0:
            return
        if leftTarget == 0:
            result.append(path[:])
        for i in range(index, len(candidates)):
            path = path + [candidates[i]]
            self.helper(candidates, leftTarget - candidates[i], path, result, i)
            path.pop()