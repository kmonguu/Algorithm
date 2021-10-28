# N을 입력받고 1부터 N까지의 수의 중요도를 입력받아, 중요도를 기준으로 수를 출력한다.

# 예제
# N이 6이고, 중요도가 1 1 9 1 1 1 이라면,
# 중요도에 따라 3 4 5 6 1 2 로 출력이 된다.

# 풀이
# 중요도를 큐에 담고 중요도가 높은 게 큰 수를 가지고 있으므로, 가장 큰 수가 첫 번째 자리에 올 때까지 앞의 수를 popleft() 한다.
# popleft() 한 수를 큐의 제일 뒤로 넣고, popleft 할 때마다 0으로 초기화 된 index 변수를 +1한다.
# 가장 큰 수가 제일 앞으로 왔을 때 N[index]값을 pop한다.

# 고려할 점
# prority의 요소가 popleft할 때마다 index 변수를 +1하여 queue에 담긴 요소를 뺄 때
# 1씩 증가하는 index뿐 아니라 초기의 queue 인덱스를 고려해주어야 한다.
