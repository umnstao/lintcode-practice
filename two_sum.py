class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        if numbers is None or len(numbers) == 0:
            return None
        # Method : hash set, numbers are not sorted.
        mySet = {}
        for i in xrange(len(numbers)):
            if numbers[i] in mySet:
                return [mySet[numbers[i]]+1, i+1]
            else:
                mySet[target - numbers[i]] = i
        