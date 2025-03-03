import math

def sub(p1, p0):
    p = [p1[0]-p0[0],
         p1[1]-p0[1],
         p1[2]-p0[2]]
    return p

def mid(p1, p0):
    p = [(p1[0]+p0[0])*0.5,
         (p1[1]+p0[1])*0.5,
         (p1[2]+p0[2])*0.5]
    return p

def to_xyz(p0, p1, p2):
    res = [
      [p0[0], p1[0], p2[0]], #x
      [p0[1], p1[1], p2[1]], #y
      [p0[2], p1[2], p2[2]], #z
    ]
    return res