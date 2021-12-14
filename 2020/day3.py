import pathlib

inputx = '''..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#'''

inputy = pathlib.Path('./day3.input').read_text()

input = inputx

rows = input.splitlines()
height = len(rows)
width = len(rows[0])


def tfs(dx, dy):  # treesForSlope
    (xpos, ypos) = (0, 0)

    hits = 0
    while ypos < height:
        if ypos < height and rows[ypos][xpos % width] == '#':
            hits += 1
        (xpos, ypos) = (xpos + dx, ypos + dy)

    print(dx, dy, hits)
    return hits


print(tfs(3, 1) * tfs(1, 1) * tfs(5, 1) * tfs(7, 1) * tfs(1, 2))
