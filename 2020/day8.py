import pathlib

inputx = '''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''

inputy = pathlib.Path('./day8.input').read_text()

input = inputy
lines = input.splitlines()

commands = list(map(lambda x: (x[0], int(x[1])), [
                line.split(" ") for line in lines]))
print(commands)


def step(commands, ptr, acc):
    (instruction, arg) = commands[ptr]
    if instruction == 'nop':
        return (ptr+1, acc)
    if instruction == 'jmp':
        return (ptr + arg, acc)
    if instruction == 'acc':
        return (ptr+1, acc + arg)
    raise 'invalid instruction'


def terminates(commands):
    ptr = 0
    acc = 0
    visited = set()

    while True:
        (ptr, acc) = step(commands, ptr, acc)
        if ptr == len(commands):
            break
        if ptr in visited:
            break
        else:
            visited.add(ptr)

    return (ptr == len(commands), acc)


for i in range(len(commands)):
    if commands[i][0] == 'acc':
        continue
    c = commands.copy()
    (instruction, arg) = c[i]
    c[i] = ('jmp', arg) if instruction == 'nop' else ('nop', arg)

    (t, acc) = terminates(c)
    if t:
        print(acc)
        break
