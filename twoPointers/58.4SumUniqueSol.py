class Solution:
    """
    @param: numbers: Give an array
    @param: target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """
    def fourSum(self, numbers, target):
        # write your code here
        numbers.sort()
        ret=[]
        for i in range(len(numbers)-3):
            if i > 0 and numbers[i] == numbers[i-1]:
                i += 1
                continue
            for j in range(i+1, len(numbers)-2):
                if j > i+1 and numbers[j] == numbers[j-1]:
                    j += 1
                    continue
                localTarget = target - numbers[i] - numbers[j]
                l = j+1
                r = len(numbers) - 1
                while l < r:
                    if numbers[l] + numbers[r] == localTarget:
                        ret.append((numbers[i],numbers[j],numbers[l],numbers[r]))
                        l += 1
                        r -= 1
                        while l < r and numbers[l] == numbers[l-1]:
                            l += 1
                        while l < r and numbers[r] == numbers[r+1]:
                            r -= 1

                    elif numbers[l] + numbers[r] < localTarget:
                        l += 1
                    else:
                        r -= 1
        return ret
