# 게임 화면의 격자의 상태가 담긴 2차원 배열 board와 인형을 집기 위해 크레인을 작동시킨 위치가 담긴 배열 moves가 매개변수로 주어질 때, 
# 크레인을 모두 작동시킨 후 터트려져 사라진 인형의 개수를 반환

# 예제 
# board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], moves = [1,5,3,5,1,2,1,4]
# 매개변수로 주어지는 board를 인형뽑기 기계 칸에 넣으면 아래와 같이 된다.
# |0|0|0|0|0|
# |0|0|1|0|3|
# |0|2|5|0|1|
# |4|2|4|4|2|
# |3|5|1|3|1|
# -----------
#  1 2 3 4 5  각 칸의 번호는 다음과 같고, moves에 따라 각 칸에서 크레인이 움직여 각 칸에서 숫자를 뽑는다.

# 가장 먼저, 1번째 칸의 가장 위의 인형을 뽑는데 0이면 무시되므로 4가 바구니에 담기게 된다.
# 다음 5번째 칸에서 가장 위의 숫자 3, 
# 다음 3번째 칸에서 1, 그 다음 5번째 칸에서 1이 뽑히고 바구니에 담기면 바로 직전에 담긴 숫자와 같은 수 이므로 모두 바구니에서 나오게 된다.
# 현재 바구니에는 [4|3] 이 담겨있고, 다음 1번째 칸에서 3이 뽑히면 바구니엔 [4|3|3]이 담기게 되므로 숫자 3이 모두 바구니에서 나오게 된다.
# 다음 2번째 칸에서 2를 뽑고, 다음 1번째 칸에서 인형으로 뽑으려고 하면 아무것도 없기 때문에 다음 moves로 넘어간다.
# 마지막으로 4번째 칸에서 4를 뽑고, 최종적으로 바구니에는 [4|2|4]가 담겨있고 터트려져 사라진 숫자의 개수는 4개 이다.
# 다음과 같은 칸에서 여러번 수를 뽑을 때, 뽑혔던 수는 다시 뽑히지 않게 뽑히고 나면 해당 숫자를 0으로 바꾸어주어 무시되도록 만든다.

# 내가 푼 코드
def solution(board, moves):
    stack = [0]
    answer = 0
    
    for move in moves:
         for b in board:
                if b[move-1] != 0:
                    
                    if stack[-1] == b[move-1]:
                        stack.pop()
                        answer += 2
                    else:
                        stack.append(b[move-1])
                        
                    b[move-1] = 0
                    break
    return answer
