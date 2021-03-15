def solution(gems):
    gemlist=list(set(gems))
    N=len(gemlist)
    answer = [1,len(gems)]
    start=0
    end=0
    minilen=len(gems)
    gemdict={gems[0]:1}
    while(start<=end and end<len(gems)):
        if(len(gemdict)!=N):
            end+=1
            if(end<len(gems)):
                if(gems[end] in gemdict):
                    gemdict[gems[end]]+=1
                else:
                    gemdict[gems[end]]=1
        else:
            if(minilen>end-start+1):
                minilen=end-start+1
                answer=[start+1,end+1]
            if(gemdict[gems[start]]==1):
                del gemdict[gems[start]]
            else:
                gemdict[gems[start]]-=1
            start+=1
    return answer
print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
