import pathlib

inputx = '''1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc'''

inputy = pathlib.Path('./day2.input').read_text()

input = inputy

lines = [(a[0].strip(), a[1].strip()) for a in (line.split(":") for line in input.splitlines())]

def isvalid1(rule, password):
  (r, c) = rule.split(" ")
  (mincount, maxcount) = map(int, r.split("-"))

  count = len([x for x in password if x == c])
  return count >= mincount and count <= maxcount

def isvalid2(rule, password):
  (r, c) = rule.split(" ")
  (index1, index2) = map(int, r.split("-"))
  c_at_1 = password[index1-1] == c
  c_at_2 = password[index2-1] == c
  return c_at_1 != c_at_2

numValid = 0
for (rule, password) in lines:
  print(rule, password)
  isvalid = isvalid2(rule, password)
  print(rule, password, isvalid)
  if isvalid:
    numValid +=1 

print(numValid)