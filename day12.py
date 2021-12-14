import re

input0 = '''start-A
start-b
A-c
A-b
b-d
A-end
b-end'''

input1 = '''dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc'''

input2 = '''fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW'''

inputy = '''he-JK
wy-KY
pc-XC
vt-wy
LJ-vt
wy-end
wy-JK
end-LJ
start-he
JK-end
pc-wy
LJ-pc
at-pc
xf-XC
XC-he
pc-JK
vt-XC
at-he
pc-he
start-at
start-XC
at-LJ
vt-JK'''

inputreal = inputy

parsed = [row.split('-') for row in inputreal.splitlines()]

print(parsed)

adjacency = {}
for (lhs, rhs) in parsed:
    adjacency.setdefault(lhs, {})[rhs] = 1
    adjacency.setdefault(rhs, {})[lhs] = 1


def printPaths(paths):
    l = [s for s in sorted([','.join(p) for p in paths])]
    seen = set()
    unique = [x for x in l if x not in seen and not seen.add(x)]
    [print(x) for x in l]
    print(len(l))
    print(len(unique))


def allPaths(allowOneRepeat=False):
    partialPaths = [(['end'], False)]
    completePaths = []

    while len(partialPaths) > 0:
        partial, usedRepeat = partialPaths.pop()
        # print("pop ", partial, usedRepeat)
        start = partial[0]
        nextCaves = adjacency[start]
        for c in nextCaves:
            pathUsedRepeat = usedRepeat
            small = False
            if re.match('^[a-z]+$', c):
                small = True
            if small and c in partial:
                if pathUsedRepeat or c == 'start' or c == 'end':
                    # print("skip", c)
                    continue
                else:
                    # print("usedRepeat", c)
                    pathUsedRepeat = True

            newPath = [c, *partial]
            if c == 'start':
                completePaths.append(newPath)
            else:
                partialPaths.append((newPath, pathUsedRepeat))
                # print("push", newPath, pathUsedRepeat)
    return completePaths


paths = allPaths(True)
printPaths(paths)
print(len(paths))
