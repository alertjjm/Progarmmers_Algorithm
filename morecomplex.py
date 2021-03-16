import sys
working=[]
N=int(input())
for i in range(N-1):
    working.append(list(map(int,sys.stdin.readline().split())))
finalA,finalB=map(int,sys.stdin.readline().split())
working.append([finalA,finalB])
result=min(working[0][0],working[0][1])
now=working[0].index(result) #0이면 A ,1이면 B
for i in range(1,N-1):
    if(now==0):
        if(working[i][now]<working[i][1]+working[i-1][2]):
            result+=working[i][now]
        else:
            result+=working[i][1]+working[i-1][2]
            now=1
    else:
        if (working[i][now] < working[i][0] + working[i - 1][3]):
            result += working[i][now]
        else:
            result += working[i][0] + working[i - 1][3]
            now = 0
i=N-1
if (now == 0):
    if (working[i][now] < working[i][1] + working[i - 1][2]):
        result += working[i][now]
    else:
        result += working[i][1] + working[i - 1][2]
        now = 1
else:
    if (working[i][now] < working[i][0] + working[i - 1][3]):
        result += working[i][now]
    else:
        result += working[i][0] + working[i - 1][3]
        now = 0
print(result)