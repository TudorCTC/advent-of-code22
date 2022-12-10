input = open("./day10/input.txt", "r")
lines = input.read().splitlines()

cycle_results = []
crt_drawing = []
crt_row = []

def execute(instruction, x, count, crt):
    global crt_row
    global crt_drawing
    
    count += 1
    if (count in range(20, 1000, 40)):
        cycle_results.append(x * count)
    
    # draw
    if (crt in range(x - 1, x + 2)):
        crt_row.append("#")
    else:
        crt_row.append(".")
    
    if (len(crt_row) == 40):
        crt_drawing.append(crt_row)
        crt_row = []
        crt = 0
    else:
        crt += 1

    if ("addx" in instruction):
        arg = instruction.split(" ")[1]
        x += int(arg)
    
    return x, count, crt

def compute():
    x = 1
    count = 0
    crt = 0
    for line in lines:
        list = []
        if ("addx" in line):
            list.append("noop")
            list.append(line)
        else:
            list.append("noop")
        for i in list:
            x, count, crt = execute(i, x, count, crt)

compute()
print(cycle_results)
print(sum(cycle_results))
for row in crt_drawing:
    print(''.join(row))