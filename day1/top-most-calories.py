input = open("./day1/input.txt", "r")
lines = input.readlines()

i = 0
calories = []

while i < len(lines):
    sum = 0
    while (i < len(lines) and lines[i] != '\n'):
        num = lines[i][:-1]
        sum = sum + int(lines[i])
        i = i + 1
    calories.append(sum)
    i = i + 1

calories.sort(reverse = True)
print(calories[0] + calories[1] + calories[2])