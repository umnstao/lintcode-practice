"""
This includes all important codes about sorting
"""
class mergeSort:
    def sortIntegers(self, A):
        # Write your code here

        # merge sort
        if A is None or len(A) == 0:
            return
        tmp = [0] * len(A)
        self.mergeSort(A, tmp, 0, len(A)-1)

    def mergeSort(self, A, tmp, start, end):
        if start >= end:
            return
        mid = (start + end)/2


        self.mergeSort(A,tmp, start, mid)
        self.mergeSort(A,tmp, mid+1, end)
        self.merge(A, tmp, start, mid, end)

    def merge(self, A, tmp, start, mid, end):
        left = start
        right = mid + 1
        index = start
        while left <= mid and right <= end:
            if A[left] <= A[right]:
                tmp[index] = A[left]
                left += 1
            else:
                tmp[index] = A[right]
                right += 1
            index += 1

        while left <= mid:
            tmp[index] = A[left]
            left += 1
            index += 1
        while right <= end:
            tmp[index] = A[right]
            right += 1
            index += 1

        for i in xrange(start, end+1):
            A[i] = tmp[i]


class quickSort:
    def sortIntegers(self, A):
        if A is None or len(A) == 0:
            return
        self.quickSort(A,0,len(A)-1)

    def quickSort(self, A, start, end):
        if start >= end:
            return
        # 1 pivot is on the value not index
        pivot = A[(start+end)/2]
        left = start
        right = end
        # 2 left <= right
        # 3 A[left] < pivot
        while left <= right:
            while left <= right and A[left] < pivot:
                left += 1
            while left <= right and A[right] > pivot:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1

        self.quickSort(A, start, right)
        self.quickSort(A, left, end)

"""
left <= right gives [start, ..., right, left, ..., end]
example:
[3,5,2,7,9,4]
pivot = 4
left = 1, right = 5
[3,4,2,7,9,5]
left = 3, right = 2

[3,4,2] -> [2,4,3]
left = 1, right = 0
[2], [4,3]->[3,4]
"""
class quickSelect:
    def kthLargestElement(self, k, A):
        if A is None or len(A) == 0 or k > len(A):
            return None
        return self.quickSelect(A, 0, len(A) - 1, k)

    def quickSelect(self, A, start, end, k):
        if start == end:
            return A[start]
        mid = start + (end - start)/2
        pivot = A[mid]
        left = start
        right = end
        while left <= right:
            while left <= right and A[left] > pivot:
                left += 1
            while left <= right and A[right] < pivot:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1

        if start + k -1 <= right:
            return self.helper(A, start, right, k)
        if start + k -1 >= left:
            return self.helper(A, left, end, k - (left - start))
        return A[right+1]








