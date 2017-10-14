class Solution:
    """
    @param: numbers: Give an array numbers of n integer
    @param: target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        numbers.sort()
        mindiff = float('inf')
        closeVal = 0
        for i in range(len(numbers) - 2):
            localTarget = target-numbers[i]
            l, r = i+1, len(numbers)-1
            while l < r:
                if numbers[l] + numbers[r] == localTarget:
                    return target
                elif numbers[l] + numbers[r] < localTarget:
                    val = numbers[l] + numbers[r]
                    diff = abs(val - localTarget)
                    if diff < mindiff:
                        mindiff = diff
                        closeVal = val + numbers[i]
                    l += 1
                else:
                    val = numbers[l] + numbers[r]
                    diff = abs(val - localTarget)
                    if diff < mindiff:
                        mindiff = diff
                        closeVal = val + numbers[i]
                    r -= 1
        return closeVal