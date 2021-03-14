result=[]
def hanoi(n, from_pos, to_pos, aux_pos):
    global result
    if n == 1:
        result.append([from_pos,to_pos])
        return
    hanoi(n - 1, from_pos, aux_pos, to_pos)
    result.append([from_pos, to_pos])
    hanoi(n - 1, aux_pos, to_pos, from_pos)
def solution(n):
    global result
    hanoi(n,1,3,2)
    return result


print(solution(2))