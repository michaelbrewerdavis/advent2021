import sys
from pathlib import Path

inputx = '16,1,2,0,4,2,7,1,2,14'
inputy = Path('./day7.input').read_text()

input = inputy.strip().split(',')

positions = [int(n) for n in input]

minPos = min(positions)
maxPos = max(positions)


def cost(delta):
    # # part 1
    # return abs(delta)
    # part 2
    d = abs(delta)
    return d * (d+1) / 2


bestWeight = sys.maxsize
bestPos = -1
for pos in range(minPos, maxPos + 1):
    weight = sum(cost(pos - n) for n in positions)
    if weight <= bestWeight:
        bestWeight = weight
        bestPos = pos

print(bestPos, bestWeight)
