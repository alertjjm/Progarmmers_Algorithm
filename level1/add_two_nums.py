def solution(numbers):
    answer = []
    #이중 루프로 순회
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if(i!=j):   #서로 인덱스가 다를 떄
                answer.append(numbers[i]+numbers[j])    #선택된 두 수를 더하여 리스트에 더하기
    answer=list(set(answer))    #set으로 변환하여 중복 제거 후 다시 list로 변환
    answer.sort()   #오름차순 정렬
    return answer
print(solution([2,1,3,4,1]))