import collections
f = open("day1_input.txt", "r")
input = [int(x) for x in f]

# O(n) time, O(n) space
def solve(input, target=2020):
    conjugates = set()
    for num in input:
        if target-num in conjugates:
            return (target-num) * num
        conjugates.add(num)
    return None

# O(n^2) time, O(n^2) space
def solve2(input, target=2020):
    # fix first, run solve on rest of list
    for i, first in enumerate(input):
        exclude_first = collections.deque(input)
        del exclude_first[i]
        ret = solve(exclude_first, 2020-first)
        if ret:
            return ret * first
    return None



if __name__ == "__main__":
    print('-----------------PART 1 SOLUTION:------------------')
    print(solve(input))
    print('-----------------PART 2 SOLUTION:------------------')
    print(solve2(input))