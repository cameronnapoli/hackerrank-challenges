#!/bin/python3

import sys

class Pole:
    def __init__(self,height,weight):
        self.h = height
        self.w = weight
    def __repr__(self):
        return "Pole(h: "+str(self.h)+", w: "+str(self.w)+")"
    def poleDifferenceCost(self,pole2):
        return (self.h - pole2.h) * self.w
    def heightDifference(self,pole2):
        return self.h - pole2.h

class PoleRelationship:
    def __init__(self, pole1, pole2):
        self.costDiff   = (pole1.h - pole2.h) * pole1.w
        self.heightDiff = pole1.h - pole2.h
    def __repr__(self):
        return "PoleRelationship(costD: "+str(self.costDiff)+ \
                       ", heightD: "+str(self.heightDiff)+")"



# n,k = input().strip().split(' ')
# n,k = [int(n),int(k)]
#
# for a0 in range(n):
#     h_i,w_i = input().strip().split(' ')
#     h_i,w_i = [int(h_i),int(w_i)]
#     poles.append((h_i, w_i))


poles = [Pole(20,1), Pole(30,1), Pole(40,1)]
relationships = set()
for i in range(len(poles)):
    for j in range(len(poles)):
        if i != j: # tuple, (cost, index of pole1, index of pole2)
            pr = PoleRelationship(poles[i], poles[j])
            if pr.costDiff >= 0:
                relationships.add(pr)

relationships = sorted(list(relationships), key=lambda pr: pr.costDiff)


print(poles)
print(relationships)
