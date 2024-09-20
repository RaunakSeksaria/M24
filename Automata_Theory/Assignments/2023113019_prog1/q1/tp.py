import numpy as np

def calc(N,M,S,X):
    arr=np.zeros(N+1,dtype=int)
    for j in range(0,M):
        inp=(input().split())
        arr[int(inp[0])]=int(inp[1])
    dict={}
    c=0
    i=1
    while(X>0):
        if S in dict:
            dict[S]+=1
        else:
            dict[S]=1
        X-=1
        if dict[S]==2:
            c+=1    
        if dict[S]>2:
            X+=1
            y=(int)(X/c)
            if(X%c>0):
                y+=1
            dict[S]+=y-1
            X-=y
            c-=1
        # print(S,dict[S],X)
        S=arr[S]
    output=[]
    for i in range(1,N+1):
        if i in dict:
            output.append(str(dict[i]))
        else:
            output.append("0")
    print(" ".join(output))

t=int(input())
for i in range(0,t):
    N,M,S,X=map(int,input().split())
    calc(N,M,S,X)