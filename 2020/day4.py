import pathlib
import re

inputx = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

inputx1 = '''eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007'''

inputx2 = '''pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719'''

inputy = pathlib.Path('./day4.input').read_text()

input = inputy

allfields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']


def parsepassport(line):
    return {x[0]: x[1] for x in map(lambda x: x.split(":"), re.split("\\s+", line)) if len(x) > 1}


passports = [parsepassport(p) for p in input.split("\n\n")]


reyear = "^\\d{4}$"
rehgt = "^(\\d+)(cm|in)$"
rehcl = "^#[0-9a-f]{6}$"
reecl = "^(amb|blu|brn|gry|grn|hzl|oth)$"
repid = "^\\d{9}$"


def isvalidyear(value, min, max):
    if not re.match(reyear, value):
        return False

    return int(value) >= min and int(value) <= max


def isvalidheight(ht):
    match = re.match(rehgt, ht)
    if match:
        if match[2] == 'cm':
            return int(match[1]) >= 150 and int(match[1]) <= 193
        else:
            return int(match[1]) >= 59 and int(match[1]) <= 76
    return False


def isvalid(p):
    print(p)
    missing = [f for f in allfields if f not in p]
    if len(missing) > 1:
        print("too many missing", missing)
        return False
    elif len(missing) == 1 and missing[0] != 'cid':
        print("required field missing", missing)
        return False

    valid = True
    if not isvalidyear(p['byr'], 1920, 2002):
        print("invalid birth year", p['byr'])
        valid = False
    if not isvalidyear(p['iyr'], 2010, 2020):
        print("invalid issue year", p['iyr'])
        valid = False
    if not isvalidyear(p['eyr'], 2020, 2030):
        print("invalid eyr", p['eyr'])
        valid = False
    if not isvalidheight(p['hgt']):
        print("invalid height", p['hgt'])
        valid = False
    if not re.match(rehcl, p['hcl']):
        print("invalid hcl", p['hcl'])
        valid = False
    if not re.match(reecl, p['ecl']):
        print("invalid ecl", p['ecl'])
        valid = False
    if not re.match(repid, p['pid']):
        print("invalid pid", p['pid'])
        valid = False

    return valid


print("num valid", len([p for p in passports if isvalid(p)]))
