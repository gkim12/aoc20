f = open("day5_input.txt", "r")
input = [x for x in f]

def ticket_to_id(ticket):
    rl, rr, cl, cr = 0, 127, 0, 7
    row_code, col_code = ticket[:7], ticket[7:]

    for half in row_code:
        if half == 'B':
            rl = (rr+rl)//2 + 1
        else:
            rr = (rr+rl)//2

    for half in col_code:
        if half == 'R':
            cl = (cr+cl)//2 + 1
        else:
            cr = (cr+cl)//2
        
    rval = rl if row_code[-1] == 'F' else rr
    cval = cl if col_code[-1] == 'L' else cr
    ticket_id = rval * 8 + cval
    return ticket_id

def solve(input):
    highest_id = 0
    for ticket in input:
        cid = ticket_to_id(ticket)
        highest_id = max(cid, highest_id)

    return highest_id

def solve2(input):
    ticket_ids = sorted(list(map(ticket_to_id, input)))
    print(ticket_ids)
    prev = ticket_ids[0]
    for tid in ticket_ids[1:]:
        if tid != prev + 1:
            return prev + 1
        prev = tid
    
    return 0

if __name__ == "__main__":
    print('-----------------PART 1 SOLUTION:------------------')
    print(solve(input))
    print('-----------------PART 2 SOLUTION:------------------')
    print(solve2(input))
    print('lol again3')