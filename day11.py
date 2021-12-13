input0 = '''11111
19991
19191
19991
11111
'''

inputx = '''5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526'''

inputy = '''6111821767
1763611615
3512683131
8582771473
8214813874
2325823217
2222482823
5471356782
3738671287
8675226574'''

input = inputy

state = [[int(x) for x in line] for line in input.splitlines()]


def printSquare(square, cols=None, rows=None):
    numRows = len(square)
    numCols = len(square[0])

    if cols == None:
        cols = range(numCols)
        rows = range(numRows)

    print()
    for row in rows:
        if row < 0 or row >= numRows:
            continue
        for col in cols:
            if col < 0 or col >= numCols:
                continue
            cell = square[row][col]
            print('*' if cell == 10 else cell, end='')
        print()
    print()


def incr(square):
    return [[cell + 1 for cell in row] for row in square]


def flash(square):
    updated = [[cell for cell in row] for row in square]
    numFlashes = 0
    checkFlashes = []
    for r, row in enumerate(updated):
        for c, cell in enumerate(row):
            if cell == 10:
                checkFlashes.append((c, r, False))

    while len(checkFlashes) > 0:
        (c, r, increment) = checkFlashes.pop(0)

        if c < 0 or c >= len(updated[0]) or r < 0 or r >= len(updated):
            continue
        cell = updated[r][c]
        if cell == 0:
            continue

        if increment:
            cell += 1
            updated[r][c] += 1

        if cell == 10:
            numFlashes += 1
            cell = 0
            updated[r][c] = 0
            checkFlashes.append((c-1, r, True))
            checkFlashes.append((c+1, r, True))
            checkFlashes.append((c, r-1, True))
            checkFlashes.append((c, r+1, True))
            checkFlashes.append((c-1, r-1, True))
            checkFlashes.append((c+1, r+1, True))
            checkFlashes.append((c-1, r+1, True))
            checkFlashes.append((c+1, r-1, True))

    return (updated, numFlashes)


def step(s):
    s = incr(s)
    return flash(s)


totalFlashes = 0
# for i in range(100):
i = 0
while True:
    i += 1
    (state, numFlashes) = step(state)
    totalFlashes += numFlashes

printSquare(state)
print(totalFlashes)
