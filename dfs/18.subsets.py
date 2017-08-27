class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    def subsets(self, S):
        # write your code here

        ret = []
        self.helper(S, 0, [], ret)
        return ret

    def helper(self,  S, idx, path, ret):
        ret.append(path[:])
        for i in xrange(idx, len(S)):
            path += [S[i]]
            self.helper(S, i+1, path, ret)
            path.pop()
