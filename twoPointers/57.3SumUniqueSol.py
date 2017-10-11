class Solution:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        numbers.sort()
        ret = []
        for i in range(0, len(numbers) - 2):
            if i > 0 and numbers[i] == numbers[i-1]:
                continue
            target = -numbers[i]
            l,r = i+1, len(numbers)-1
            while l < r:
                if numbers[l] + numbers[r] == target:
                    ret.append((numbers[i],numbers[l],numbers[r]))
                    l += 1
                    r -= 1
                    while l< r and numbers[l]==numbers[l-1]:
                        l += 1
                    while l< r and numbers[r] ==numbers[r+1]:
                        r -= 1
                elif numbers[l] + numbers[r] < target:
                    l += 1
                else:
                    r -= 1
        return ret

