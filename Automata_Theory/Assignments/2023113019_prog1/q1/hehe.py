import numpy as np
file = open('5_in[1].txt', 'r') 
# Convert the first line to integer
t = int(file.readline())
# print(t)
index = 1

for i in range(t):
    # Read and parse the next line
    n, m, s, x = map(int, file.readline().split())
    # print("hello")
    index += 1
    
    # Initialize transitions array
    transitions = np.zeros(n + 1, dtype=int)
    
    # Read the transitions
    for j in range(m):
        a, b = map(int, file.readline().split())
        transitions[a] = b
        # print("hello")
        index += 1

    # Initialize solution array
    solution = np.zeros(n + 1, dtype=int)
    curr = s
    cycle = []
    count = 0

    # Process to find the cycle
    while count < x:
        if solution[curr] == 1:
            cycle.append(curr)
            # print("hello")

        if solution[curr] == 2:
            break  # cycle
        count += 1
        
    p = len(cycle)
    
    if(p!=0): # there can be instances where count is exahusted, while loop se termination
        #but koi cycle nahi mila: eg tree case
        for i in cycle:
            solution[i] += (x-count)//p
        curr = cycle[0] # yeh kyuki our cycle detection also ended at end of cycle
        # toh start of cycle se hi next iter chalu hoga

        for i in range((x-count)%p):
            #x-count >= 0 always
            solution[curr] += 1
            curr = transitions[curr]

    for i in range(1,n+1):
        print(solution[i],end = " ") # end changes default delimiter newline
    print() # using default delimiter in empty print statement