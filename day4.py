f = open("day4_input.txt", "r")
input = [x.split() for x in f.read().split('\n\n')]
input = [dict([x.split(':') for x in y]) for y in input]

def solve(input):
    count = 0
    necessary_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    for passport in input:
        if necessary_fields.issubset(set(passport.keys())):
            count += 1
    return count

def solve2(input):
    count = 0
    necessary_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    for passport in input:
        # check all required fields present
        if not necessary_fields.issubset(set(passport.keys())):
            continue
        
        # check byr
        if not (1920 <= int(passport['byr']) <= 2002): 
            continue
        
        # check iyr
        if not (2010 <= int(passport['iyr']) <= 2020): 
            continue
        
        # check eyr
        if not (2020 <= int(passport['eyr']) <= 2030): 
            continue
        
        # check hgt
        hgt = passport['hgt']
        if hgt[-2:] == 'in':
            if not (59 <= int(hgt[:-2]) <= 76):
                continue
        elif hgt[-2:] == 'cm':
            if not (150 <= int(hgt[:-2]) <= 193):
                continue
        else:
            continue
        
        # check hcl
        hcl = passport['hcl']
        if not len(hcl) == 7 or not hcl[0] == '#' or not hcl[1:].isalnum():
            continue
        
        # check ecl
        if passport['ecl'] not in set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
            continue

        # check pid
        if not len(passport['pid']) == 9 or not passport['pid'].isnumeric():
            continue
        
        count += 1

    return count

if __name__ == "__main__":
    print('-----------------PART 1 SOLUTION:------------------')
    print(solve(input))
    print('-----------------PART 2 SOLUTION:------------------')
    print(solve2(input))