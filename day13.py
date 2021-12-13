import itertools
import pathlib
import re

inputx = '''6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5'''

inputy = pathlib.Path('./day13.input').read_text()

input = inputy

lines = input.splitlines()

graph = [[int(x) for x in line.split(',')]
         for line in lines if len(line) > 0 and not line.startswith('fold')]
folds = [line.split(' ')[-1] for line in lines if line.startswith('fold')]


def printGraph(g):
    width = max(line[0] + 1 for line in g)
    height = max(line[1] + 1 for line in g)
    print("graph has size", width, height)
    if width > 200:
        return
    output = []
    for _ in range(height):
        output.append([' '] * width)
    for (x, y) in g:
        output[y][x] = 'X'
    print()
    for row in output:
        print(''.join(row))
    print()


def fold(graph, instruction):
    (direction, svalue) = instruction.split("=")
    value = int(svalue)
    print("folding", direction, value)
    newgraph = []
    for g in graph:
        (x, y) = g
        if direction == 'x' and x > value:
            x = value - (x - value)
        elif direction == 'y' and y > value:
            y = value - (y - value)

        newgraph.append((x, y))
    return newgraph


def count(graph):
    return len(set([','.join(str(gg) for gg in g) for g in graph]))


printGraph(graph)

for foldline in folds:
    graph = fold(graph, foldline)
    printGraph(graph)
