class Solution:
    # @param nums {int[]} an array of integer
    # @param target {int} an integer
    # @return {int} an integer
    def twoSum6(self, nums, target):
        # Write your code here

        nums.sort()
        i = 0
        j = len(nums) - 1
        cnt = 0
        myHash = {}
        while i < j:
            if nums[i] + nums[j] == target and (nums[i],nums[j]) not in myHash:
                cnt += 1
                myHash[(nums[i],nums[j])] = 1
                i += 1
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                j -= 1
        return cnt


        """
        if nums is None or len(nums) == 0:
            return 0
        nums.sort()
        #print nums
        left = 0
        right = len(nums) - 1
        ret = 0
        while left < right:
            #print nums[left]
            if nums[left] + nums[right] == target:
                ret += 1
                print nums[left], nums[right]
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1

                while left < right and nums[right] == nums[right+1]:
                    right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1

        return ret
        """