import pathlib
import math

inputx = '''[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]'''

inputy = pathlib.Path('./day10.input').read_text()

input = inputy

lines = input.splitlines()


def scoreLine(line):
    stack = []
    for c in line:
        if c == '[' or c == '(' or c == '{' or c == '<':
            stack.append(c)
            continue

        last = stack.pop()
        if last == '(' and c == ')':
            continue
        if last == '[' and c == ']':
            continue
        if last == '<' and c == '>':
            continue
        if last == '{' and c == '}':
            continue

        raise Exception(c)

    score = 0
    print(stack)
    while(len(stack) > 0):
        score *= 5
        c = stack.pop()
        if c == '(':
            score += 1
        elif c == '[':
            score += 2
        elif c == '{':
            score += 3
        elif c == '<':
            score += 4

    return score


autocompleteScores = []
errorTotal = 0

for line in lines:
    try:
        score = scoreLine(line)
        autocompleteScores.append(score)
    except Exception as err:
        c = err.args[0]
        score = 0
        if c == ')':
            score = 3
        elif c == ']':
            score = 57
        elif c == '}':
            score = 1197
        elif c == '>':
            score = 25137

        errorTotal += score

scores = sorted(autocompleteScores)
print(scores)

finalScore = scores[math.floor(len(scores) / 2)]
print("final score", finalScore)
print("error total", errorTotal)
