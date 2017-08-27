class Solution:
    """
    @param S: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, S):
        # write your code here
        if S is None:
            return S
        if len(S) == 0:
            return [[]]
        S.sort()
        ret = []
        self.helper(ret, 0, [], S)
        return ret

    def helper(self, ret, index, path, S):
        ret.append(path[:])
        for i in range(index, len(S)):
            if i!= index and S[i] == S[i-1]:
                continue
            self.helper(ret, i+1, path+[S[i]], S)
