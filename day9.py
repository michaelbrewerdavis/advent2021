from pathlib import Path

DEBUG = False


def debug(*args):
    if DEBUG:
        print(*args)


inputx = '''2199943210
3987894921
9856789892
8767896789
9899965678'''

inputy = Path('./day9.input').read_text()


inputreal = inputy

heightMap = [[int(c) for c in line] for line in inputreal.splitlines()]

rows = len(heightMap)
cols = len(heightMap[0])

debug(heightMap)


def isLocalMin(x, y):
    val = heightMap[y][x]
    if y > 0 and val >= heightMap[y-1][x]:
        return False
    elif y < rows - 1 and val >= heightMap[y+1][x]:
        return False
    elif x > 0 and val >= heightMap[y][x-1]:
        return False
    elif x < cols - 1 and val >= heightMap[y][x+1]:
        return False
    else:
        return True


def debugSquare(xrange=range(cols), yrange=range(rows)):
    print()
    for row in yrange:
        if row < 0 or row >= rows:
            continue
        for col in xrange:
            if col < 0 or col >= cols:
                continue
            print(heightMap[row][col], end='')
        print()
    print()


def flood(x, y, c):
    size = 0
    queue = [[x, y]]

    while len(queue) > 0:
        [x, y] = queue.pop(0)
        if y < 0 or x < 0 or y >= rows or x >= cols or heightMap[y][x] == 9 or heightMap[y][x] == c:
            continue
        heightMap[y][x] = c
        size += 1
        queue.append([x-1, y])
        queue.append([x+1, y])
        queue.append([x, y-1])
        queue.append([x, y+1])

    return size


def go():
    lowPoints = []
    sum = 0
    for y in range(rows):
        for x in range(cols):
            if isLocalMin(x, y):
                lowPoints.append([x, y])
                sum += heightMap[y][x] + 1

    print("total risk", sum)

    sizes = []
    for i, lowPoint in enumerate(lowPoints):
        size = flood(*lowPoint, chr(65 + (i % 26)))
        sizes.append(size)

    [a, b, c] = sorted(sizes)[-3:]
    print("product", a * b * c)

    debugSquare()


go()
