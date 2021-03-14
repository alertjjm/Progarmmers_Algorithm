def solution(sticker):
    N=len(sticker)
    if(N==1):
        return sticker[0]
    dplist=[0 for i in range(N)]
    dplist[0]=sticker[0]
    dplist[1]=sticker[0]
    for i in range(2,N-1):
        dplist[i]=max(sticker[i]+dplist[i-2],dplist[i-1])
    dplist2=[0 for i in range(N)]
    dplist2[0]=0
    dplist2[1]=sticker[1]
    for i in range(2,N):
        dplist2[i]=max(sticker[i]+dplist2[i-2],dplist2[i-1])
    return max(max(dplist),max(dplist2))

print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
print(solution([1,4]))