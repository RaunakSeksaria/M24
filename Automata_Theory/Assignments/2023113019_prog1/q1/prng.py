import numpy as np

t = input()
for i in range(int(t)):
    n,m,s,x = map(int,input().split(' '))
    # print(n,m,s,x)
    # print(type(n),type(m),type(s),type(x))

    transitions = np.zeros(n+1,dtype=int)
    for j in range(m):
        a,b = map(int,input().split(' '))
        transitions[a] = b

    solution = np.zeros(n+1,dtype = int) # 1 indexed
    curr = s
    cycle = []
    count = 0
    # print(transitions)

    while count<x:
        if(solution[curr]==1):        
            cycle.append(curr)  
        if(solution[curr]==2):
            break # cycle has been completely detected
        solution[curr] += 1
        curr = transitions[curr]
        count += 1
    # print(solution)

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