graphs=list()
visited=[]
skilllist=list()
def dfs(skill,result):
    global graphs
    global total
    global visited
    global skilllist
    temp=result
    if 1 not in graphs[skill]:
        print(' '.join(result))
        return
    for i in range(len(graphs[skill])):
        if(graphs[skill][i]==1 and visited[i]==False):
            temp.append(skilllist[i])
            dfs(i,temp)
            temp.pop()

def main():
    global visited
    global graphs
    global skilllist
    x = input()
    N=int(input())
    skilllist=x.split(' ')
    graphs=[[0 for i in range(len(skilllist))] for j in range(len(skilllist))]

    for i in range(N):
        a,b=input().split(' ')
        apos=skilllist.index(a)
        bpos=skilllist.index(b)
        graphs[apos][bpos]=1
    visited=[False for i in range(len(skilllist))]
    visited[0]=True
    dfs(0,[skilllist[0]])


if __name__ == "__main__":
    main()