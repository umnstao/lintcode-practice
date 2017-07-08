class Solution:
    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    def numIslands(self, grid):
        # Write your code here

        if grid == None or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        m = len(grid)
        n = len(grid[0])
        island = 0
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    self.BFS(grid, i, j)
                    island += 1
        return island

    #BFS to go through all points
    def BFS(self, grid, i, j):
        rowDirection = [1,0,0,-1]
        colDirection = [0,1,-1,0]
        queue = [(i,j)]
        while queue:
            point = queue.pop(0)
            for k in range(4):
                x = point[0] + rowDirection[k]
                y = point[1] + colDirection[k]
                if not self.isValid(grid,x,y):
                    continue
                if grid[x][y] == 1:
                    grid[x][y] = 0
                    queue.append((x,y))

    # check if the point is still valid
    def isValid(self, grid, i, j):
        m = len(grid)
        n = len(grid[0])
        return i>= 0 and i<m and j<n and j>=0