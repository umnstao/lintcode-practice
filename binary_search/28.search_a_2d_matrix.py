class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        rowNum = len(matrix)
        colNum = len(matrix[0])
        if matrix[0][0] > target or matrix[rowNum-1][colNum-1] < target:
            return False
        start = 0
        end = len(matrix) - 1
        while start + 1 < end:
            mid = start + (end - start)/2
            if matrix[mid][0] < target:
                start = mid
            elif matrix[mid][0] == target:
                return True
            else:
                end = mid
        if matrix[end][0] <= target:
            row = end
        else:
            row = start
        start = 0
        end = colNum - 1
        while start + 1 < end:
            mid = start + (end - start)/2
            if matrix[row][mid] < target:
                start = mid
            elif matrix[row][mid] == target:
                return True
            else:
                end = mid
        if matrix[row][start] == target or matrix[row][end] == target:
            return True
        return False
