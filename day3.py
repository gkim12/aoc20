f = open("day3_input.txt", "r")
input = [x for x in f]

def solve(input, dx, dy):
    count = 0
    x = 0
    y = 0
    for line in input:
        if y % dy == 0:
            if line[x] == '#':
                count +=1 
            x += dx
            x %= len(line)-1
        y += 1
    return count

def solve2(input):
    r1d1 = solve(input, 1, 1)
    r3d1 = solve(input, 3, 1)
    r5d1 = solve(input, 5, 1)
    r7d1 = solve(input, 7, 1)
    r1d2 = solve(input, 1, 2)
    return r1d1*r3d1*r5d1*r7d1*r1d2

if __name__ == "__main__":
    print('-----------------PART 1 SOLUTION:------------------')
    print(solve(input, dx=3, dy=1))
    print('-----------------PART 2 SOLUTION:------------------')
    print(solve2(input))