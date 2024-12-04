
with open("in.txt", "r") as f:
    l = f.readlines()

safe = 0

def is_safe(line):
    
    
    differences = [abs(line[i] - line[i+1]) for i in range(len(line) - 1)]
    
    if not all(1 <= diff <= 3 for diff in differences):
        return False

    increasing = all(line[i] < line[i+1] for i in range(len(line) - 1))
    decreasing = all(line[i] > line[i+1] for i in range(len(line) - 1))
    return increasing or decreasing

for line in l:
    
    line = [int(x) for x in line.split()]
    
    if is_safe(line):
        safe += 1
        continue

    
    for i in range(len(line)):
        
        nline = line[:i] + line[i+1:]
        if is_safe(nline):
            safe += 1
            break


print(safe)
