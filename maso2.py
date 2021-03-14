from itertools import combinations
pclist=list()
moneylist=list()
def recursive(i,h,money):
    global pclist
    global moneylist
    pc = pclist[i]
    pc.sort(reverse=True)
    for hour in pc:
        if (hour <= h):
            money += 1000 * hour
            h = h - hour
            recursive(i,h,money)
    moneylist[i]=money

def main():
    global pclist
    global moneylist
    #PC의 대수 pp, 예약한 손님의 수 nn, 피시방 운영 시간 hh
    p,n,h = map(int,input().split(' '))
    pclist=[[] for i in range(p+1)]
    moneylist=[0 for i in range(p+1)]
    for i in range(n):
        x,y=map(int,input().split(' '))
        pclist[x].append(y)
    for i in range(1,p+1):
        recursive(i,h,0)
    for i in range(1, p + 1):
        print(str(i)+" "+moneylist[i])






if __name__ == "__main__":
    main()