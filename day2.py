f = open("day2_input.txt", "r")
input = [x.split() for x in f]

def parse(line):
    policy, letter, password = line
    policy = list(map(int, policy.split('-')))
    letter = letter[0]
    return [policy, letter, password]

input = [parse(line) for line in input]

def solve(input):
    count = 0

    for line in input:
        policy, letter, password = line
        if policy[0] <= password.count(letter) <= policy[1]:
            count += 1

    return count

def solve2(input):
    count = 0

    for line in input:
        policy, letter, password = line

        if (password[policy[0]-1] == letter) ^ (password[policy[1]-1] == letter):
            count += 1

    return count

if __name__ == "__main__":
    print('-----------------PART 1 SOLUTION:------------------')
    print(solve(input))
    print('-----------------PART 2 SOLUTION:------------------')
    print(solve2(input))