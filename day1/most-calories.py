import os
input = open("./day1/input.txt", "r")
lines = input.readlines();

max = 0
i = 0

while i < len(lines):
    sum = 0
    while (i < len(lines) and lines[i] != '\n'):
        num = lines[i][:-1]
        sum = sum + int(lines[i])
        i = i + 1
    if sum > max:
        max = sum
    i = i + 1

print(max)
    