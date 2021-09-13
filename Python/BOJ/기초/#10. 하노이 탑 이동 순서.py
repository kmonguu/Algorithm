# 세 개의 막대에 N개의 원판이 있다. 한 번에 한 개의 원판을 움직이며 위로 갈수록 원판이 작아지게 놓아야한다.
# 이때 최소 이동횟수를 출력

# 핵심
# 1. 시작점(start)에 있는 N 번째 원판을 목적지(to)로 옮기기 위해 N-1개의 원판을 경유지(via)로 옮긴다.
# 2. N 번째 원판을 목적지로 옮긴다.
# 3. 경유지에 있는 원판을 목적지로 옮긴다.

# 첫 번째 코드
N = int(input())

def hanoi(N, start, to, via):       # 하노이 탑 함수 구현
  if N == 1:                        # 원판의 개수가 1인 경우
    print (start, to)               # 그냥 원판 하나만 목적지로 옮기면 되므로 시작점과 목적지를 출력

  else:
    hanoi(N-1, start, via, to)      # 재귀함수 호출을 하여 N-1개의 원판을 경유지(via)로 이동
    print(start, to)                # 시작점에 있는 N 번째 원판을 목적지 to로 이동 후 경로를 출력
    hanoi(N-1, via, to, start)      # 경유지에 있는 N-1개의 원판을 목적(to)로 이동

print(2**N-1)                       # 이동 횟수는 2의 N제곱에 -1로 구함
hanoi(N, 1, 3, 2)                   # 하노이 탑 함수 실행



# 두 번째 코드
N = int(input())

def hanoi(N, start, to, via): 
  if N == 1:                                                    # 원판의 갯수가 1이면
    move.append([start, to])                                    # 원판 하나의 이동 경로 시작점, 목적지를 move 배열에 저장

  else:
    hanoi(N-1, start, via, to)                                  # N-1 개의 원판을 시작점에서 경유지로 이동
    move.append([start, to])                                    # 시작점에 있는 N 번째 원판의 목적지로 가는  경로를 move 배열에 저장
    hanoi(N-1, via, to, start)                                  # 경유지에 있는 원판을 목적지로 이동

move = []                                                       # 이동 경로를 저장하는 move 리스트 선언
hanoi(N, 1, 3, 2)

print(len(move))                                                # 배열 길이를 출력하여 이동 횟수를 구함
print('\n'. join([' '.join(str(i)for i in j)for j in move]))    # 배열에 담긴 이동 경로를 출력




# 세 번째 코드
N = int(input())

def move(N, start, to):                                         # 이동 경로를 출력하는 move 함수구현
  print(start, to)

def hanoi(N, start, to, via):                                   # hanoi 함수 구현
  if N == 1:
    print(start, to)

  else:
    hanoi(N-1, start, via, to)
    move(N, start, to)
    hanoi(N-1, via, to, start)

print(2**N-1)
hanoi(N, 1, 3, 2)
