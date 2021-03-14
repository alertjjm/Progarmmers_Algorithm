def distance(item, area):
    if(area[0]<=item<=area[1]):
        return [-1,-1]
    else:
        distancelong=[abs(area[0]-item),abs(area[1]-item)]
        mini=min(distancelong)
        pos=distancelong.index(mini)
        return [pos,mini]
def main():
    N,M,E=map(int, input().split(' '))
    peanuts=list(map(int,input().split(' ')))
    area=[E,E]
    while(area[0]>=peanuts[0] and area[1]<=peanuts[-1]):
        cnt=0
        poslist=[]
        dlist=[]
        for item in peanuts:
            distancel=distance(item,area)
            if(distancel[0]==-1):
                cnt+=1
            else:
                dlist.append(distancel[1])
                poslist.append(distancel[0])
        if(cnt==E):
            print(area[1]-area[0])
            break
        else:
            mini=min(dlist)
            minpos=dlist.index(mini)
            area[poslist[minpos]]=mini
    print(area[1],area[0])
if __name__ == "__main__":
    main()