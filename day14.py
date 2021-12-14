import pathlib

inputx = '''NNCB
CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C'''

inputy = pathlib.Path('./day14.input').read_text()

input = inputy

lines = input.splitlines()

sequence = lines.pop(0)
rules = {}
for line in lines:
    rules[line[0:2]] = line[-1]

print(sequence, rules)

pairs = [sequence[i:i+2] for i in range(len(sequence) - 1)]
counts = {s: pairs.count(s) for s in set(pairs)}

print(pairs, counts)


def step(sequence):
    newsequence = [sequence[0]]
    for i in range(len(sequence) - 1):
        newsequence.append(rules[sequence[i:i+2]])
        newsequence.append(sequence[i+1])

    return ''.join(newsequence)


def stepcounts(counts):
    newcounts = {}

    def add(ch, n):
        newcounts[ch] = newcounts.setdefault(ch, 0) + n

    for k in counts:
        c = rules[k]
        lhs = ''.join((k[0], c))
        rhs = ''.join((c, k[1]))
        add(lhs, counts[k])
        add(rhs, counts[k])

    return newcounts


def countchars(counts):
    allchars = set(''.join(k for k in counts))
    totals = {}
    for c in allchars:
        totals.setdefault(c, 0)
        for k in counts:
            if c == k[0]:
                totals[c] = totals[c] + counts[k]

    totals[sequence[-1]] += 1
    return totals


print(sequence)
print(counts)
for i in range(40):
    # sequence = step(sequence)
    # print(sequence, len(sequence))
    counts = stepcounts(counts)

print(counts)
totals = countchars(counts)
print(totals)
print(max(totals.values()) - min(totals.values()))
