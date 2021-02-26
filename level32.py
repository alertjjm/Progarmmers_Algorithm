from itertools import permutations
def solution(n, weak, dist):
    mini=99999
    answer = 0
    walls=[0 for i in range(n)]
    for w in weak:
        walls[w]=1
    for w in weak:
        permute = permutations(dist,len(dist))
        for case in permute:
            newwall = walls[w:] + walls[:w]
            cnt = 0
            for i in case:
                idx=newwall.index(1)
                end=min([len(newwall)-1,idx+i])
                for clear in range(idx,end):
                    newwall[clear]=0
                cnt+=1
                if(1 not in newwall):
                    break
            if(mini>cnt and 1 not in newwall):
                mini=cnt
        permute = permutations(dist, len(dist))
        for case in permute:
            newwall = walls[w:] + walls[:w]
            newwall.reverse()
            cnt = 0
            for i in case:
                idx = newwall.index(1)
                end = min([len(newwall) - 1, idx + i])
                for clear in range(idx, end):
                    newwall[clear] = 0
                cnt += 1
                if (1 not in newwall):
                    break
            if (mini > cnt and 1 not in newwall):
                mini = cnt
    if(mini==99999):
        return -1
    return mini
print(solution(12,[1, 3, 4, 9, 10],[3, 5, 7]))