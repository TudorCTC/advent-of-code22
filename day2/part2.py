input = open("./day2/input.txt", "r")
lines = input.read().splitlines()

scores = {"A" : 1, "B" : 2, "C" : 3}
outcomes = {"X" : 0, "Y" : 3, "Z" : 6}
beats = {"A" : "C", "B" : "A", "C" : "B"}
loses = {"A" : "B", "B" : "C", "C" : "A"}

total = 0
for i in range(0, len(lines)):
    line = lines[i].split(" ")
    p1 = line[0]
    outcome = line[1]
    total += outcomes[outcome]
    if (outcome == "X"):
        total += scores[beats[p1]]
    elif (outcome == "Y"):
        total += scores[p1]
    else:
        total += scores[loses[p1]]

print(total)