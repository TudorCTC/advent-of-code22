input = open("./day9/input.txt", "r")
lines = input.read().splitlines()


visited = set()
visited.add((0, 0))

directions = {"L" : (-1, 0), "R" : (1, 0), "U" : (0, 1), "D": (0, -1)}

def move(d, h):
    direction = directions[d]
    h = (h[0] + direction[0], h[1] + direction[1])
    return h

def resolve_pair(h, t):
    if (h == t) or (abs(h[1] - t[1]) <= 1 and abs(h[0] - t[0]) <= 1):
        return t
    elif h[0] - t[0] == 0 and abs(h[1] - t[1]) > 1:
        t[1] += 1 if h[1] > t[1] else -1
    elif h[1] - t[1] == 0 and abs(h[0] - t[0]) > 1:
        t[0] += 1 if h[0] > t[0] else -1
    else:
        t[0] += 1 if h[0] > t[0] else -1
        t[1] += 1 if h[1] > t[1] else -1
    
    return t

def resolve_list(knots):
    i = len(knots) - 2
    while i >= 0:
        resolve_pair(knots[i + 1], knots[i])
        i -= 1
    return knots
        

def simulate_movements(h, t):
    for line in lines:
        tokens = line.split(" ")
        d = tokens[0]
        c = int(tokens[1])
        for i in range(c):
            h = move(d, h)
            t = resolve_pair(h, t)
            visited.add((t[0], t[1]))

def simulate_movements2(knots):
    for line in lines:
        tokens = line.split(" ")
        d = tokens[0]
        c = int(tokens[1])
        for i in range(c):
            knots[len(knots) - 1] = move(d, knots[len(knots) - 1])
            knots = resolve_list(knots)
            visited.add((knots[0][0], knots[0][1]))

simulate_movements2([[0, 0] for i in range(10)])
print(len(visited))
        