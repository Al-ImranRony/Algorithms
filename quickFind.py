# The eager approach
# Time Complexity - O(n*n) too slow !

import sys

# sys.stdin = open("input.txt", "r")
# sys.stdout = open("output.txt", "w")

class quickFindUF:
    
    def __init__(self, n):
        self.id = list(range(n))            
    
    def connected(self, p, q):
        return self.id[p] == self.id[q]

    def union(self, p, q):
        pid, qid = self.id[p], self.id[q]
        for i in range(len(self.id)):
            if (self.id[i] == pid): self.id[i] = qid


if __name__ == "__main__":
    g = quickFindUF(6)
    cc = g.connected(4, 3)
    if not cc: g.union(4, 3)

    cc = g.connected(2, 5)
    if not cc: g.union(2, 5)
    
    cc = g.connected(5, 0)
    if not cc: g.union(5, 0)
   
    cc = g.connected(1, 0)
    if not cc: g.union(1, 0)


# before:  0 1 2    after:  0-1-2 
#                               |     
#          3 4 5            3-4 5