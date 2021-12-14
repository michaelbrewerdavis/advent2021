import pathlib

inputx = '''FBFBBFFRLR
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL'''

inputy = pathlib.Path("./day5.input").read_text()

input = inputy

lines = input.splitlines()


def narrow(min, max, commands):
    # print(min, max, commands)
    if len(commands) == 0:
        return min

    c = commands.pop(0)
    if c == 'F' or c == 'L':
        newmin = min
        newmax = min + (max - min) / 2
    else:
        newmin = min + (max - min) / 2
        newmax = max

    return narrow(newmin, newmax, commands)


def getid(line):
    rowspec = line[0:7]
    colspec = line[7:]

    row = narrow(0, 128, list(rowspec))
    col = narrow(0, 8, list(colspec))
    print(line, row, col, 8 * row + col)
    return 8 * row + col


ids = [getid(line) for line in lines]
print(max(ids))

idmap = {id:1 for id in ids}
for x in range(int(max(ids))):
  if x in idmap:
    continue
  if x+1 in idmap and x-1 in idmap:
    print("found", x)

