input = open("./day6/input.txt", "r")
line = input.readline()

packet_start_len = 4
msg_start_len = 14

def find_marker(marker_length):
    start = 0
    left = 0
    right = 0
    chars = set()
    for right in range(len(line)):
        if (line[right] in chars):
            while (left < right and line[right] in chars):
                chars.remove(line[left])
                left += 1
        chars.add(line[right])
        if (right - left + 1 == marker_length):
            start = right + 1
            break;
    
    return start

print(find_marker(packet_start_len))
print(find_marker(msg_start_len))