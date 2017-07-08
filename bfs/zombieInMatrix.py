class Solution:
    # @param {int[][]} grid  a 2D integer grid
    # @return {int} an integer
    def zombie(self, grid):
        # Write your code here
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return -1
        q = []
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == 1:
                    q.append([i,j])
        return self.myBFS(grid, q, 0)

    def myBFS(self, grid, q, time):
        time += 1
        newq = []
        #print q
        while len(q) > 0:
            [i,j] = q.pop(0)
            deltaX = [1, 0, 0, -1]
            deltaY = [0, 1, -1, 0]
            for k in xrange(4):
                x = i + deltaX[k]
                y = j + deltaY[k]
                if x > len(grid) - 1 or x < 0 or y > len(grid[0]) - 1 or y < 0:
                    continue
                if grid[x][y] == 2:
                    continue
                if grid[x][y] == 0:
                    grid[x][y] = 1
                    newq.append([x,y])
        if self.check(grid):
            return time
        elif len(newq) > 0:
            return self.myBFS(grid, newq, time)
        else:
            return -1
    def check(self,grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    return False
        return True

































        m = len(grid)
        n = len(grid[0])
        queue = []
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    queue.append((i,j))
        count = self.BFS(queue, grid)

        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 0:
                    return -1
        return count

    # BFS
    def BFS(self, queue, grid):
        rowDirection = [-1, 0, 0, 1]
        colDirection = [0, 1, -1, 0]
        count = -1
        while len(queue)>0:

            size = len(queue)
            count += 1
            #print size,count

            for _ in xrange(size):
                point = queue.pop(0)
                for k in xrange(4):
                    x = point[0] + rowDirection[k]
                    y = point[1] + colDirection[k]
                    if not self.isValid(grid, x, y):
                        continue
                    if grid[x][y] == 0:
                        grid[x][y] = 1
                        queue.append((x,y))

            #print queue
        return count

    # check valid
    def isValid(self, grid, i, j):
        m = len(grid)
        n = len(grid[0])
        return i >= 0 and i < m and j >= 0 and j < n and grid[i][j] != 2