input = open("./day12/input.txt")
lines = input.read().splitlines()

def is_valid(pos, heights, visited):
    x, y = pos
    if (x < 0 or x >= len(heights) or y < 0 or y >= len(heights[0])):
        return False
    if ((x, y) in visited):
        return False
    
    return True
 
def bfs(heights, start, end):
    visited = set()
    queue = []
    steps = 0
    queue.append(start)
    visited.add((start[0], start[1]))
    while (len(queue) > 0):
        size = len(queue)
        if (end in queue):
            return steps
        for i in range(size):
            x, y = queue.pop(0)
            if (is_valid([x, y + 1], heights, visited) and heights[x][y] - heights[x][y + 1] >= -1):
                queue.append([x, y + 1])
                visited.add((x, y + 1))
            if (is_valid([x + 1, y], heights, visited) and heights[x][y] - heights[x + 1][y] >= -1):
                queue.append([x + 1, y])
                visited.add((x + 1, y))
            if (is_valid([x, y - 1], heights, visited) and heights[x][y] - heights[x][y - 1] >= -1):
                queue.append([x, y - 1])
                visited.add((x, y - 1))
            if (is_valid([x - 1, y], heights, visited) and heights[x][y] - heights[x - 1][y] >= -1):
                queue.append([x - 1, y])
                visited.add((x - 1, y))
        steps += 1
    
    return -1

def hillclimb():
    start_pos = []
    alternate_starts = []
    end_pos = []
    heights  = []
    for i in range(len(lines)):
        row = []
        for j in range(len(lines[i])):
            if lines[i][j] == 'S':
                start_pos = [i, j]
                row.append(0)
            elif lines[i][j] == 'a':
                alternate_starts.append([i, j])
                row.append(0)
            elif lines[i][j] == 'E':
                end_pos = [i, j]
                row.append(25)
            else:
                row.append(ord(lines[i][j]) - ord('a'))
        heights.append(row)
    min = bfs(heights, start_pos, end_pos)
    print("Part 1: " + str(min))
    print(bfs(heights, [20, 0], end_pos))
    for start in alternate_starts:
        res = bfs(heights, start, end_pos)
        if (res > 0 and res < min):
            min = res
    print("Part 2: " + str(min))
    

hillclimb()