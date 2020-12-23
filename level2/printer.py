def solution(priorities, location):
    queues=[]   #출력 큐 결과 저장
    tuples = [(i,priorities[i]) for i in range(len(priorities))]    #처음 순서를 보존하기 위해 (idx, value)로 튜플의 리스트로 변환
    while len(queues)<len(priorities):  #큐의 길이가 총 길이보다 작을 동안 반복
        maxitem=max([i[1] for i in tuples]) #튜플의 value 중 가장 큰 값
        cur=tuples.pop(0)   #튜플리스트의 맨 앞의 원소 pop
        if(cur[1]<maxitem): #최대값보다 작은 경우
            tuples.append(cur)  #맨 뒤로 이동
        else:   #가장 큰 값인 경우
            queues.append(cur)  #출력 큐로 이동
    for i in range(len(queues)):    #반복하며 location의 순서 찾기
        if(queues[i][0]==location): #초기 위치 비교
            return i+1  #순서 출력
print(solution([2, 1, 3, 2],2))