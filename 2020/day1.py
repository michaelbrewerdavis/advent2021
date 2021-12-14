import pathlib

inputx = '''1721
979
366
299
675
1456'''

inputy = pathlib.Path('./day1.input').read_text()

input = inputy

numbers = [int(n) for n in input.splitlines()]

indexed = {n: True for n in numbers}

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        total = numbers[i] + numbers[j]
        remainder = 2020 - total
        if total == 2020:
            print('part1', numbers[i], numbers[j], numbers[i] * numbers[j])
        elif remainder in indexed:
            print('part2', numbers[i], numbers[j],
                  remainder, numbers[i] * numbers[j] * remainder)
