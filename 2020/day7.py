import re
import pathlib

inputx = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.'''

inputx1 = '''shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.'''

inputy = pathlib.Path('./day7.input').read_text()

input = inputy

def parserule(line):
    match1 = re.match("^(.+) bags contain (.*).$", line)
    color = match1[1]

    contains = [x.strip() for x in match1[2].split(",")]
    rule = {}
    for x in contains:
        match2 = re.match("^(\\d+) (.+) bags?", x)
        if match2:
            rule[match2[2]] = int(match2[1])

    return (color, rule)


rules = {}
for line in input.splitlines():
    (color, rule) = parserule(line)
    rules[color] = rule

def possible(basecolor):
  parents = {}
  for color, rule in rules.items():
      for key in rule.keys():
          parents.setdefault(key, {})
          parents[key][color] = 1

  checklist = list(parents[basecolor].keys())
  possible = set()

  while len(checklist) > 0:
      color = checklist.pop()
      if color in possible:
          continue
      possible.add(color)
      checklist.extend(list(parents.setdefault(color, {}).keys()))
  return possible

print(len(possible('shiny gold')))

innercount = {}

def getinnercount(color):
  print("getting color", color)
  if color in innercount:
    print("cached", innercount[color])
    return innercount[color]
  
  rule = rules[color]
  print(rule)
  count = sum(rule.values()) + sum([int(item[1]) * getinnercount(item[0]) for item in rule.items()])
  innercount[color] = count
  print('caching', color, count)
  return count

print(getinnercount('shiny gold'))
