inputx = '''.#.
..#
###'''

inputy = '''#......#
##.#..#.
#.#.###.
.##.....
.##.#...
##.#....
#####.#.
##.#.###'''

input = inputy

lines = input.splitlines()


def newgraph():
    return {
        'minx': 0,
        'maxx': 0,
        'miny': 0,
        'maxy': 0,
        'minz': 0,
        'maxz': 0,
        'minw': 0,
        'maxw': 0
    }


def getgraph(g, x, y, z, w):
    return g.get(w, {}).get(z, {}).get(y, {}).get(x, None)


def setgraph(g, x, y, z, w, value):
    g['minx'] = min(x, g['minx'])
    g['maxx'] = max(x, g['maxx'])
    g['miny'] = min(y, g['miny'])
    g['maxy'] = max(y, g['maxy'])
    g['minz'] = min(z, g['minz'])
    g['maxz'] = max(z, g['maxz'])
    g['minw'] = min(w, g['minw'])
    g['maxw'] = max(w, g['maxw'])
    g.setdefault(w, {})
    g[w].setdefault(z, {})
    g[w][z].setdefault(y, {})
    g[w][z][y][x] = value


graph = newgraph()

for y in range(len(lines)):
    for x, v in enumerate(lines[y]):
        if v == '#':
            setgraph(graph, x, y, 0, 0, v)

print(graph)


def printgraph(g):
    for w in range(g['minw'], g['maxw'] + 1):
        for z in range(g['minz'], g['maxz'] + 1):
            print("w =", w, "z =", z)
            for y in range(g['miny'], g['maxy'] + 1):
                for x in range(g['minx'], g['maxx'] + 1):
                    print(getgraph(g, x, y, z, w) or '.', end='')
                print()


printgraph(graph)

neighboroffsets = [(x, y, z, w) for x in range(-1, 2) for y in range(-1, 2)
                   for z in range(-1, 2) for w in range(-1, 2) if x != 0 or y != 0 or z != 0 or w != 0]


def alive(g, x, y, z, w):
    live = getgraph(g, x, y, z, w) == '#'
    neighbors = [getgraph(g, x + dx, y + dy, z + dz, w + dw)
                 for (dx, dy, dz, dw) in neighboroffsets]
    liveneighbors = len([c for c in neighbors if c == '#'])
    if live:
        if liveneighbors == 2 or liveneighbors == 3:
            return True
    else:
        if liveneighbors == 3:
            return True
    return False


def step(g):
    newg = newgraph()
    for w in range(g['minw'] - 1, g['maxw'] + 2):
        for z in range(g['minz'] - 1, g['maxz'] + 2):
            for y in range(g['miny'] - 1, g['maxy'] + 2):
                for x in range(g['minx'] - 1, g['maxx'] + 2):
                    live = alive(g, x, y, z, w)
                    if live:
                        setgraph(newg, x, y, z, w, '#')
    return newg


def countgraph(g):
    return len([v for x in graph.values() if type(x) is dict for y in x.values() for z in y.values() for v in z.values()])


for i in range(6):
    print("step", i+1)
    graph = step(graph)
    printgraph(graph)
    print(countgraph(graph))
