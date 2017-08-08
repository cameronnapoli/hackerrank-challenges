#!/bin/python3
import sys

# algorithm to check if a node is part of a triangle in an
# adjacency matrix graph
def nodeInTriangle(row, col, g):
    gLen = len(g)
    rowSearch = range((row-1) if (row-1>=0) else row, (row+2) if (row+1 < gLen) else (row+1))
    colSearch = range((col-1) if(col-1>=0) else col, (col+2) if (col+1 < gLen) else (col+1))
    # print("row:",row,"col:",col,"   rowSearch:",rowSearch,"colSearch:",colSearch)
    # print("----------------------------------------------------------------")
    for r in rowSearch:
        for c in colSearch:
            if r > c and r != 0 and not (r == row and c == col):
                if g[r][c] == 1 :
                    if g[r][row] == 1:
                        return True
    # print("")
    return False

n = int(input().strip())
g = []
for g_i in range(n):
    g_temp = list(map(int,input().strip().split(' ')))
    g.append(g_temp)

# g = [[0, 1, 1, 0, 0, 0],
#      [1, 0, 1, 1, 0, 0],
#      [1, 1, 0, 1, 0, 0],
#      [0, 1, 1, 0, 1, 1],
#      [0, 0, 0, 1, 0, 1],
#      [0, 0, 0, 1, 1, 0]]

nodesInTriangle = set()

for row in range(1,len(g)):
    for col in range(len(g[0])):
        if col < row:
            if nodeInTriangle(row, col, g):
                nodesInTriangle.add(row+1)
                nodesInTriangle.add(col+1)

nodesInTriangle = sorted(list(nodesInTriangle))

print(len(nodesInTriangle))
print(" ".join(map(lambda x: str(x),nodesInTriangle)))
