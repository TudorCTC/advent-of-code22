input = open("./day4/input.txt", "r")
lines = input.read().splitlines()

fully_contained = 0
overlaps = 0

for line in lines:
    one, two = line.split(',')
    a1, a2 = one.split('-')
    b1, b2 = two.split('-')
    a1, a2, b1, b2 = [int(x) for x in [a1, a2, b1, b2]]
    if a1 <= b1 and b2 <= a2 or b1 <= a1 and a2 <= b2:
        fully_contained += 1
    if a1 <= b2 and b1 <= a1 or b1 <= a2 and a1 <= b1:
        overlaps += 1
    
print(fully_contained)
print(overlaps)