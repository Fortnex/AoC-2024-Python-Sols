# Open the input file and read its contents
with open("in.txt", "r") as f:
    l = f.readlines()
    #print(l)
safe = 0
for line in l:
    line = [int(l) for l in line.split()]
    #print(line)
    increasing = all(line[i] < line[i+1] for i in range(len(line) - 1))
    decreasing = all(line[i] > line[i+1] for i in range(len(line) - 1))

    #print(increasing,decreasing)
    if increasing or decreasing: 
        line = [abs(line[i]-line[i+1]) for i in range(len(line)-1)]
        print(line)
        
        

        if max(line)<=3 and min(line)>0 and increasing:
            
            print("safe")
            safe+=1
        

print(safe)










#fuckin hell idk what the fuck im doing da


