import collections
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)#collection의 counter이용하여 빼주기
    return list(answer)[0]
print(solution(["leo", "kiki", "eden"],["eden","kiki"]))