input = open("./day3/input.txt", "r")
lines = input.read().splitlines()

def getPriority(c):
    if (c.isupper()):
        return 27 + (ord(c) - ord('A'))
    
    return ord(c) - ord('a') + 1

def rucksack_reorganization():
    priority_sum = 0
    for i in range(0, len(lines)):
        rucksack = lines[i]
        half = len(rucksack) // 2
        chars = set(rucksack[0 : half])
        for j in range(half, len(rucksack)):
            if (rucksack[j] in chars):
                priority_sum += getPriority(rucksack[j])
                break
    
    return priority_sum

def find_badges():
    priority_sum = 0
    for i in range(0, len(lines), 3):
        first_set = set(lines[i])
        second_set = set(lines[i + 1])
        third_set = set(lines[i + 2])
        for c in first_set:
            if (c in second_set and c in third_set):
                priority_sum += getPriority(c)
    return priority_sum

print(find_badges())    