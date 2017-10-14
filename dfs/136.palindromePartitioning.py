class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        # write your code here
        ret = []
        self.helper(s, ret, [], 0)
        return ret
    def helper(self, s, ret, path, k):
        if k == len(s):
            ret.append(path[:])
        for i in range(k+1, len(s)+1):
            if self.isPalindrome(s[k:i]):
                path += [s[k:i]]
                self.helper(s,ret,path,i)
                path.pop()
    def isPalindrome(self, s):
        return s == s[::-1]

