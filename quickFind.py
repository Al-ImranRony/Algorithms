# The eager approach

import sys

# sys.stdin = open("input.txt", "r")
# sys.stdout = open("output.txt", "w")

class quickFindUF:
    id = []
    def __init__(self, n):
        for i in range(n):
            id[i] = i
    
    def connected(self, p, q):
        return id[p] == id[q]

    def union(self, p, q):
        pid, qid = id[p], id[q]
        for i in range(len(id)):
            if (id[i] == pid): id[i] = qid


if __name__ == "__main__":
    g = Graph(10)
    g.connected(4, 3)
    g.connected(6, 5)
    g.connected(3, 8)
    g.connected(9, 4)
    g.connected(2, 1)
    g.connected(8, 9)
    g.connected(5, 0)
    g.connected(7, 2)
    g.connected(1, 0)
    g.connected(6, 1)

    