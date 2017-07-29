# Definition for a Directed graph node
# class DirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    """
    @param graph: A list of Directed graph node
    @return: A list of graph nodes in topological order.
    """
    def topSort(self, graph):
        # write your code here

        # The main point of this problem is about
        # establish the dependency relationships
        # i.e. computing in-degree (using hashmap) and out-degree (# of neighbors)

        # use hashmap for in-degree
        hashSet = {}
        for node in graph:
            for neighbor in node.neighbors:
                if neighbor in hashSet:
                    hashSet[neighbor] += 1
                else:
                    hashSet[neighbor] = 1

        # find a 0 in-degree to start
        result = []
        queue = []
        for node in graph:
            if node not in hashSet:
                result.append(node)
                queue.append(node)

        # BFS to decrease in-degree and add to result
        while queue:
            head = queue.pop(0)
            for neighbor in head.neighbors:
                hashSet[neighbor] -= 1
                if hashSet[neighbor] == 0:
                    result.append(neighbor)
                    queue.append(neighbor)
        return result
