class Solution:
    # @param {string} s A string
    # @return {boolean} Whether the string is a valid palindrome
    def isPalindrome(self, s):
        # Write your code here
        s = s.lower()
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalpha() and not s[l].isdigit():
                l += 1
            while l < r and not s[r].isalpha() and not s[r].isdigit():
                r -= 1
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True