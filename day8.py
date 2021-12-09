from functools import reduce
from itertools import chain
from pathlib import Path

DEBUG = False


def debug(*args):
    if DEBUG:
        print(*args)


input0 = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |cdfeb fcadb cdfeb cdbaf'

inputx = '''be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce'''

inputy = Path('./day8.input').read_text()

input = inputy

lines = [[field.strip().split(" ") for field in line.split("|")]
         for line in input.splitlines()]

debug(lines)

signalSets = [line[0] for line in lines]
outputs = [line[1] for line in lines]

segmentsForDigit = {
    0: 'ABCEFG',
    1: 'CF',
    2: 'ACDEG',
    3: 'ACDFG',
    4: 'BCDF',
    5: 'ABDFG',
    6: 'ABDEFG',
    7: 'ACF',
    8: 'ABCDEFG',
    9: 'ABCDFG'
}

digitsForSegmentCount = reduce(
    lambda acc, digit: acc.setdefault(
        len(segmentsForDigit[digit]), []).append(digit) or acc,
    segmentsForDigit,
    {})

# part 1
unique = [value for value in chain(
    *outputs) if len(digitsForSegmentCount[len(value)]) == 1]
print('unique output values', len(unique))


def intersect(lhs, rhs):
    return ''.join([value for value in lhs if value in rhs])


signals = signalSets[0]


def numSignals(signals, char):
    return len([s for s in signals if char in s])


def join(*args):
    return ''.join(sorted(args))


def parseSignals(signals):
    one = next(s for s in signals if len(s) == 2)
    seven = next(s for s in signals if len(s) == 3)
    debug("1,7", one, seven)
    A = next(c for c in seven if c not in one)
    C = next(c for c in one if numSignals(signals, c) == 8)
    F = next(c for c in one if c != C)
    debug("A:", A, "C:", C, "F:", F)
    four = next(s for s in signals if len(s) == 4)
    bd = [c for c in four if c not in one]
    B = next(c for c in bd if numSignals(signals, c) == 6)
    D = next(c for c in bd if c != B)
    ABCDF = ''.join([A, B, C, D, F])
    eight = next(s for s in signals if len(s) == 7)
    nine = next(s for s in signals if len(s) ==
                6 and len(intersect(s, ABCDF)) == 5)
    G = next(c for c in nine if c not in ABCDF)
    E = next(c for c in eight if c not in nine)
    debug(A, B, C, D, E, F, G)
    return [
        join(A, B, C, E, F, G),
        join(C, F),
        join(A, C, D, E, G),
        join(A, C, D, F, G),
        join(B, C, D, F),
        join(A, B, D, F, G),
        join(A, B, D, E, F, G),
        join(A, C, F),
        join(A, B, C, D, E, F, G),
        join(A, B, C, D, F, G)
    ]


sum = 0

for (signals, outputs) in lines:
    debug(signals, outputs)
    parsed = parseSignals(signals)
    debug(parsed)
    digits = [parsed.index(join(*o)) for o in outputs]
    num = int(''.join([str(d) for d in digits]))
    sum += num
    debug(num)

print("total:", sum)
