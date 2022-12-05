input = open("./day5/input.txt", "r")
lines = input.read().splitlines()
stacks = [[] for i in range(9)]

def initStacks():
    i = 0
    while (len(lines[i]) != 0):
        line = lines[i]
        for j in range(1, len(line), 4):
            if (line[j].isalpha()):
                stacks[j // 4].append(line[j])
        i += 1
    i += 1 # skip empty line
    return i

def moveCrates():
    i = initStacks()
    while (i < len(lines)):
        tokens = lines[i].split(' ');
        count = int(tokens[1])
        src = int(tokens[3]) - 1
        dest = int(tokens[5]) - 1
        while count > 0 and len(stacks[src]) > 0:
            crate = stacks[src].pop(0)
            stacks[dest].insert(0, crate)
            count -= 1
        i += 1
    
    result = ""
    for j in range(9):
        result += stacks[j][0]
    return result

def moveMultipleCrates():
    i = initStacks()
    while (i < len(lines)):
        tokens = lines[i].split(' ');
        count = int(tokens[1])
        src = int(tokens[3]) - 1
        dest = int(tokens[5]) - 1
        
        move = stacks[src][0:count]
        remainder = stacks[src][count:]
        stacks[src] = remainder
        stacks[dest] = move + stacks[dest]
        
        i += 1
    
    result = ""
    for j in range(9):
        result += stacks[j][0]
    return result

print(moveMultipleCrates())