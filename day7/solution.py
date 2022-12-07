input = open("./day7/input.txt", "r")
lines = input.read().splitlines()

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
    
    def get_size(self):
        return self.size
    
    def get_name(self):
        return self.name

class Directory:
    def __init__(self, name):
        self.name = name
        self.directories = {}
        self.files = {}
        self.size = 0
        
    def add_directory(self, directory):
        if not directory.name in self.directories:
            self.directories[directory.name] = directory
    
    def add_file(self, file):
        if not file.name in self.files:
            self.files[file.name] = file
    
    def get_name(self):
        return self.name
    
    def get_size(self):
        if (self.size != 0):
            return self.size
        
        for f in self.files.values():
            self.size += f.get_size()
        for  d in self.directories.values():
            self.size += d.get_size()
    
        return self.size


def get_filesystem():
    path = []
    root = Directory("/")
    curr_directory = root
    path.append(curr_directory)
    for line in lines:
        if line[0] == '$':
            tokens = line.split(' ')
            if (tokens[1] == "cd"):
                if (tokens[2] == ".."):
                    path.pop(len(path) - 1)
                    curr_directory = path[len(path) - 1]
                elif (tokens[2] == "/"):
                    path = []
                    path.append(curr_directory)
                else:
                    curr_directory = curr_directory.directories[tokens[2]]
                    path.append(curr_directory)
        else:
            tokens = line.split(' ')
            if tokens[0] == "dir":
                new_dir = Directory(tokens[1])
                curr_directory.add_directory(new_dir)
            else:
                new_file = File(tokens[1], int(tokens[0]))
                curr_directory.add_file(new_file)
    return root

def sum_dir_size():
    root = get_filesystem()
    sum = 0
    queue = []
    queue.append(root)
    while (len(queue) != 0):
        size = len(queue)
        for i in range(size):
            curr = queue.pop(0)
            if (curr.get_size() <= 100000):
                sum += curr.get_size()
            for d in curr.directories.values():
                queue.append(d)
        
    return sum

def delete_dir():
    root = get_filesystem()
    unused = 70000000 - root.get_size()
    min_delete = root.get_size()
    queue = []
    queue.append(root)
    while (len(queue) != 0):
        size = len(queue)
        for i in range(size):
            curr = queue.pop(0)
            s = curr.get_size()
            if (unused + s > 30000000 and s < min_delete):
                min_delete = s
            for d in curr.directories.values():
                queue.append(d)
    return min_delete

print(delete_dir())