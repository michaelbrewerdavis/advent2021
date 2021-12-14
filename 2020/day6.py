import pathlib

inputx = pathlib.Path('./day6.1.input').read_text()
inputy = pathlib.Path('./day6.2.input').read_text()

input = inputy

groups = [group.splitlines() for group in input.split("\n\n")]

def countunion(group):
  print(group)
  total = set()
  for person in group:
    total = total.union(set(person))

  return len(total)

def countintersection(group):
  print(group)
  total = set(group.pop())
  for person in group:
    total = total.intersection(set(person))

  return len(total)

print(sum([countunion(group) for group in groups]))
print(sum([countintersection(group) for group in groups]))