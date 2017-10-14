# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.dict = {}

    def cloneGraph(self, node):
        if not node:
            return None
        # write your code here
        # Traverse all nodes
        queue = [node]
        mySet = {node:1}
        while queue:
            head = queue.pop(0)
            for neighbor in head.neighbors:
                if neighbor not in mySet:
                    queue.append(neighbor)
                    mySet[neighbor] = 1

        # Copy all nodes
        mapping = {}
        for ele in mySet:
            mapping[ele] = UndirectedGraphNode(ele.label)
        # Copy all edges
        for ele in mySet:
            newNode = mapping[ele]
            for neighbor in ele.neighbors:
                newNeighbor = mapping[neighbor]
                newNode.neighbors.append(newNeighbor)

        return mapping[node]