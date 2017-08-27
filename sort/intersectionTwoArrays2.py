class Solution:
    # @param {int[]} nums1 an integer array
    # @param {int[]} nums2 an integer array
    # @return {int[]} an integer array
    def intersection(self, nums1, nums2):
        # Write your code here
        """
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0
        ret = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                ret.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return ret
        """
        myTable1 = {}
        for i in range(len(nums1)):
            if nums1[i] not in myTable1:
                myTable1[nums1[i]] = 1
            else:
                myTable1[nums1[i]] += 1
        ret = []
        for j in range(len(nums2)):
            if nums2[j] in myTable1 and myTable1[nums2[j]]>0:
                myTable1[nums2[j]] -= 1
                ret.append(nums2[j])
        return ret