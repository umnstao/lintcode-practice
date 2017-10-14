class Solution:
    # @param {int} n an integer
    # @param {int[][]} edges a list of undirected edges
    # @return {boolean} true if it's a valid tree, or false
    def validTree(self, n, edges):
        # Write your code here
        if n == 0:
            return False
        # 验证无环
        if len(edges) != n-1:
            return False
        if len(edges) == 0:
            return True
        # 验证联通
        graphSet = self.initializeGraph(n,edges)
        # BFS to check len(mySet) == n
        queue = [0]
        mySet = [0]
        while queue:
            node = queue.pop(0)
            neighbors = graphSet[node]
            for neighbor in neighbors:
                if neighbor not in mySet:
                    mySet.append(neighbor)
                    queue.append(neighbor)
        return len(mySet) == n

    def initializeGraph(self, n, edges):
        hashSet = {}
        for i in range(len(edges)):
            u = edges[i][0]
            v = edges[i][1]
            if u in hashSet:
                hashSet[u].append(v)
            else:
                hashSet[u] = [v]
            if v in hashSet:
                hashSet[v].append(u)
            else:
                hashSet[v] = [u]
        return hashSet