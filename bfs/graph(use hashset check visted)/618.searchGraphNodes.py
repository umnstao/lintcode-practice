# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param {UndirectedGraphNode[]} graph a list of undirected graph node
    # @param {dict} values a dict, <UndirectedGraphNode, (int)value>
    # @param {UndirectedGraphNode} node an Undirected graph node
    # @param {int} target an integer
    # @return {UndirectedGraphNode} a node
    def searchNode(self, graph, values, node, target):
        # Write your code here
        if not graph:
            return None
        queue = [node]
        mySet = [node]
        while len(queue) > 0:
            thisNode = queue.pop(0)
            if values[thisNode] == target:
                return thisNode
            for neighbor in thisNode.neighbors:
                if neighbor not in mySet:
                    mySet.append(thisNode)
                    queue.append(neighbor)
        return None


# This can be used as BFS on a graph. mySet is to check if a node has been searched or not.