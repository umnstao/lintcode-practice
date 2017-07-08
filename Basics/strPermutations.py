class Solution:
    # @param {string} A a string
    # @param {string} B a string
    # @return {boolean} a boolean
    def stringPermutation(self, A, B):
        # Write your code here
        myD = [0]*255
        for i in range(len(A)):
            myD[ord(A[i])] += 1
        for j in range(len(B)):
            myD[ord(B[j])] -= 1
        return myD == [0]*255