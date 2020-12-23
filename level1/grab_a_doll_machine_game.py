def solution(board, moves):
    answer = 0
    stack=[]    #인형을 담을 바구니
    height=len(board)   #board의 높이
    for i in moves: #moves 리스트 순회
        j=0
        while(j<height):    #위에서부터 아래로 높이를 넘지 않는 한도로 순회
            if(board[j][i-1]!=0):   #인형을 발견할 시 탈출(j에는 y축 좌표 저장)
                break
            j+=1
        if(j<height):   #높이 이상일 경우는 해당 line에 인형이 없는 경우
            if(len(stack)!=0 and stack[len(stack)-1]==board[j][i-1]):   #스택의 꼭대기와 크레인이 뽑은 인형이 같은 경우
                stack.pop()     #꼭대기 인형 삭제
                answer+=2   #인형 2개가 만나 터트려짐
            else:
                stack.append(board[j][i-1])     #스택 맨 위에 쌓기
            board[j][i-1]=0
    return answer
print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))