inputx = '3,4,3,1,2'
inputy = '1,1,5,2,1,1,5,5,3,1,1,1,1,1,1,3,4,5,2,1,2,1,1,1,1,1,1,1,1,3,1,1,5,4,5,1,5,3,1,3,2,1,1,1,1,2,4,1,5,1,1,1,4,4,1,1,1,1,1,1,3,4,5,1,1,2,1,1,5,1,1,4,1,4,4,2,4,4,2,2,1,2,3,1,1,2,5,3,1,1,1,4,1,2,2,1,4,1,1,2,5,1,3,2,5,2,5,1,1,1,5,3,1,3,1,5,3,3,4,1,1,4,4,1,3,3,2,5,5,1,1,1,1,3,1,5,2,1,3,5,1,4,3,1,3,1,1,3,1,1,1,1,1,1,5,1,1,5,5,2,1,5,1,4,1,1,5,1,1,1,5,5,5,1,4,5,1,3,1,2,5,1,1,1,5,1,1,4,1,1,2,3,1,3,4,1,2,1,4,3,1,2,4,1,5,1,1,1,1,1,3,4,1,1,5,1,1,3,1,1,2,1,3,1,2,1,1,3,3,4,5,3,5,1,1,1,1,1,1,1,1,1,5,4,1,5,1,3,1,1,2,5,1,1,4,1,1,4,4,3,1,2,1,2,4,4,4,1,2,1,3,2,4,4,1,1,1,1,4,1,1,1,1,1,4,1,5,4,1,5,4,1,1,2,5,5,1,1,1,5'

input = [int(x) for x in inputy.split(",")]

print(input)


def newFish():
    return 8


def readyForNewFish(fish):
    return fish == 0


def iterateFish(fish):
    if fish == 0:
        return 6

    return fish - 1


def iterateFishies(fishies):
    oldFishies = []
    newFishies = []
    for fish in fishies:
        if readyForNewFish(fish):
            newFishies.append(newFish())
        oldFishies.append(iterateFish(fish))

    return oldFishies + newFishies


fishies = input

# naive solution
# days = 80
# for _ in range(days):
#     fishies = iterateFishies(fishies)
# print('number of fishies', len(fishies))


def school(fishies):
    s = {}
    for fish in fishies:
        s[fish] = s.setdefault(fish, 0) + 1
    return s


def iterateSchool(school):
    newSchool = {}
    for age in range(8):
        newSchool[age] = school.setdefault(age+1, 0)

    newSchool[8] = school.setdefault(0, 0)
    newSchool[6] = school.setdefault(0, 0) + school.setdefault(7, 0)
    return newSchool


s = school(fishies)

days = 256
for d in range(days):
    s = iterateSchool(s)

print(sum(s.values()))
