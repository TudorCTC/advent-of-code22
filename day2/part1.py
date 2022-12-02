input = open("./day2/input.txt", "r")
lines = input.read().splitlines()

translate = {"X" : "A", "Y" : "B", "Z" : "C"}
scores = {"A" : 1, "B" : 2, "C" : 3}

# check if player 2 beats player 1
def outcome(p1, p2):
    if (p1 == p2):
        return 3
    if (p1 == 'A' and p2 == 'C'):
        return 0
    if (p1 == 'C' and p2 == 'A'):
        return 6
    
    return 6 if p1 < p2 else 0

total = 0
for i in range(0, len(lines)):
    line = lines[i].split(" ")
    p1 = line[0]
    p2 = translate[line[1]]
    score = scores[p2] + outcome(p1, p2)
    total += score

print(total)
    

    