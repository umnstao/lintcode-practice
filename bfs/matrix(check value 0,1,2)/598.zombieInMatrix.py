class Solution:
    # @param {int[][]} grid  a 2D integer grid
    # @return {int} an integer
    def zombie(self, grid):
        # Write your code here
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return -1
        queue = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    queue.append((i,j))
        dist = self.BFS(grid, queue)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    return -1
        return dist

    def BFS(self, grid, queue):
        dist = -1
        deltaX = [1,0,0,-1]
        deltaY = [0,1,-1,0]
        while len(queue) > 0:
            size = len(queue)
            dist += 1
            for i in range(size):
                point = queue.pop(0)
                x = point[0]
                y = point[1]
                for k in range(4):
                    xnew = x + deltaX[k]
                    ynew = y + deltaY[k]
                    if xnew < 0 or ynew < 0 or xnew >= len(grid) or ynew >= len(grid[0]):
                        continue
                    if grid[xnew][ynew] == 0:
                        grid[xnew][ynew] = 1
                        queue.append((xnew, ynew))
        return dist
