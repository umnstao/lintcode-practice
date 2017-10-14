class Solution:
    # @param {int} numCourses a total of n courses
    # @param {int[][]} prerequisites a list of prerequisite pairs
    # @return {int[]} the course order
    def findOrder(self, numCourses, prerequisites):
        # Write your code here

        # build a hash map
        myHash = [[] for _ in range(numCourses)]
        numDegree = [0 for _ in range(numCourses)]
        for i in range(len(prerequisites)):
            preCourse = prerequisites[i][1]
            postCourse = prerequisites[i][0]
            numDegree[postCourse] += 1
            myHash[preCourse].append(postCourse)
        queue = []
        ret = []
        for k in range(numCourses):
            if numDegree[k] == 0:
                queue.append(k)
        while len(queue) > 0:
            course = queue.pop(0)
            ret.append(course)
            for later in myHash[course]:
                numDegree[later] -=1
                if numDegree[later] == 0:
                    queue.append(later)
        return ret if len(ret) == numCourses else []



