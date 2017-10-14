class Solution:
    # @param {int[]} nums1 an integer array
    # @param {int[]} nums2 an integer array
    # @return {int[]} an integer array
    def intersection(self, nums1, nums2):
        # Write your code here
        myTable = {}
        ret = []
        """
        #method 1
        for i in range(len(nums1)):
            if nums1[i] not in myTable:
                myTable[nums1[i]] = 1
        for j in range(len(nums2)):
            if nums2[j] in myTable:
                ret.append(nums2[j])
                del myTable[nums2[j]]
        return ret
        
        #method 2
        myTable2 = {}
        for i in range(len(nums1)):
            if nums1[i] not in myTable:
                myTable[nums1[i]] = 1
        for j in range(len(nums2)):
            if nums2[j] in myTable and nums2[j] not in myTable2:
                ret.append(nums2[j])
                myTable2[nums2[j]] = 1
        return ret
        """
        #method 3
        nums1.sort()
        nums2.sort()
        
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                if i == 0 or j == 0 or nums1[i] != nums1[i-1]:
                    ret.append(nums1[i])
                i += 1
                j += 1
                
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return ret
        
        
        
        