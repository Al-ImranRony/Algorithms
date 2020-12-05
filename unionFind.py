# Find out the connected components
# I'm using graph here !

import sys

# sys.stdin = open("input.txt", "r")
# sys.stdout = open("output.txt", "w")

class Graph:
 
    def __init__(self, V):              # declared class variables 
        self.V = V                      
        self.adj = [[] for i in range(V)]

    def dfs(self, temp, vtx, visited):
        visited[vtx] = True
        temp.append(vtx)

        for i in self.adj[vtx]:
            if not visited[i]: 
                temp = self.dfs(temp, i, visited)

        return temp 

    def addEdge(self, v, w):    # method to add undirected edge
        self.adj[v].append(w)
        self.adj[w].append(v) 

    def connectedComponents(self):
        visited = []
        cc = []
        for i in range(self.V):
            visited.append(False)
        for v in range(self.V):
            if not visited[v]:
                temp = []
                cc.append(self.dfs(temp, v, visited))

        return cc


if __name__ == "__main__": 
    g = Graph(10)
    g.addEdge(4, 3)
    g.addEdge(6, 5)
    g.addEdge(3, 8)
    g.addEdge(9, 4)
    g.addEdge(2, 1)
    g.addEdge(8, 9)
    g.addEdge(5, 0)
    g.addEdge(7, 2)
    g.addEdge(1, 0)
    g.addEdge(6, 1)

    cc = g.connectedComponents()
    print("Following are connected components: ", cc)