# Definition for Undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    '''
    @param {UndirectedGraphNode[]} graph a list of Undirected graph node
    @param {UndirectedGraphNode} s, t two Undirected graph nodes
    @return {int} an integer
    '''
    def sixDegrees(self, graph, s, t):
        # Write your code here
        if not graph:
            return -1
        if s == t:
            return 0
        queue = [s]
        time = 0
        mySet = {s:1}
        while len(queue) > 0:
            time += 1
            size = len(queue)
            for _ in range(size):
                node = queue.pop(0)
                for neighborNode in node.neighbors:
                    if neighborNode == t:
                        return time
                    if neighborNode not in mySet:
                        mySet[neighborNode] = 1
                        queue.append(neighborNode)
        return -1
