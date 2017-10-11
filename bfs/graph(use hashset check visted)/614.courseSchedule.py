class Solution:
    # @param {int} numCourses a total of n courses
    # @param {int[][]} prerequisites a list of prerequisite pairs
    # @return {boolean} true if can finish all courses or false
    def canFinish(self, numCourses, prerequisites):
        # Write your code here
        inDegree = [0]*numCourses
        neighbors = [[] for _ in xrange(numCourses)] #len is out-degree
        for i in range(len(prerequisites)):
            second = prerequisites[i][0]
            first = prerequisites[i][1]
            inDegree[second] += 1
            neighbors[first].append(second)
        #print neighbors
        #print inDegree
        # Pick a 0 in-degree to start
        result = []
        queue = []
        for i in range(numCourses):
            if inDegree[i] == 0:
                #inDegree[i] -= 1
                result.append(i)
                queue.append(i)

        # BFS to add more
        while queue:
            head = queue.pop(0)
            for neighbor in neighbors[head]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)
                    result.append(head)

        #print result
        return len(result) == numCourses