def solution(skill, skill_trees):
    answer=0
    slist=list(skill)   #리스트로 변환
    sdict={slist[i]:i for i in range(len(slist))}   #key(스킬):value(숫자)로 딕셔너리 생성
    for testtree in skill_trees:    #스킬 목록 순회
        tlist=list(testtree)    #스킬 item을 리스트로 변환
        newlist=[sdict[j] for j in tlist if j in slist] #선행 스킬 규칙에 해당되는 스킬만 뽑아 value 리스트로 생성
        if(len(newlist)==0):    #선행스킬 순서의 스킬을 안쓴 경우
            answer+=1
            continue
        comparelist=[j for j in range(max(newlist)+1)]   #0부터 스킬 숫자 최대값까지 생성
        if(newlist==comparelist):   #value 리스트와 대조 리스트가 같은 경우(순서가 맞는 경우)
            answer+=1
    return answer
print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))