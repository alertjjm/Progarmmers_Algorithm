import heapq

def solution(N, road, K):
    INF=600000
    visited=[False for i in range(N+1)]
    times=[INF for i in range(N+1)]
    answer = 0
    graphlist=[[INF for i in range(N+1)] for j in range(N+1)]
    for r in road:
        a,b,time=r
        graphlist[a][b]=min(graphlist[a][b],time)
        graphlist[b][a]=min(graphlist[b][a],time)
    ##그래프 초기화
    for i in range(N+1):
        times[i]=graphlist[1][i]
    visited[1]=True
    times[1]=0
    for i in range(1,N+1):
        mini=INF
        v=0
        for j in range(1,N+1):
            if(visited[j]==False and mini>times[j]):
                mini=times[j]
                v=j
        visited[v]=True
        for j in range(1,N+1):
            if(visited[j]==False):
                if(times[j]>times[v]+graphlist[v][j]):
                    times[j]=times[v]+graphlist[v][j]
    for i in range(1,N+1):
        if(times[i]<=K):
            answer+=1
    return answer
print(solution(6,[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]],4))