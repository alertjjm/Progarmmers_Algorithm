def main():
    N,M,E=map(int, input().split(' '))
    peanuts=list(map(int,input().split(' ')))
    #오른쪽
    pos=E
    cnt=0
    while pos<=peanuts[-1]:
        if(pos in peanuts):
            cnt+=1
        pos=pos+1
        if(cnt==M):
            break
    posleft=E
    cntleft=0
    while posleft>=peanuts[0]:
        if(posleft in peanuts):
            cntleft+=1
        posleft=posleft-1
        if(cntleft==M):
            break
    minlist=[abs(posleft-E),abs(pos-E)]
    print(min(minlist))


if __name__ == "__main__":
    main()