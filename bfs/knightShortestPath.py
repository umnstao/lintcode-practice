# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param {boolean[][]} grid a chessboard included 0 (False) and 1 (True)
    # @param {Point} source a point
    # @param {Point} destination a point
    # @return {int} the shortest path
    def shortestPath(self, grid, source, destination):
        # Write your code here
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return -1
        queue = [source]
        deltaX = [1,1,-1,-1,2,2,-2,-2]
        deltaY = [2,-2,2,-2,1,-1,1,-1]
        time = 0
        while len(queue) > 0:
            size = len(queue)
            time += 1
            for _ in range(size):
                point = queue.pop(0)
                for k in range(8):
                    x = point.x + deltaX[k]
                    y = point.y + deltaY[k]
                    myPoint = Point(x,y)
                    if x < 0 or y < 0 or x > len(grid)-1 or y > len(grid[0])-1:
                        continue
                    if  x == destination.x and y == destination.y:
                        return time
                    if grid[x][y] == 1:
                        continue
                    elif grid[x][y] == 0:
                        grid[x][y] = 1
                        queue.append(Point(x,y))
        return -1
