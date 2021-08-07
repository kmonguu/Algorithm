#입력은 24시간 표현으로 자정은 0:0, 하루의 끝은 23:59로 표현
#입력받은 시간에서 45분 앞서는 시간을 출력
#24시간 개념과 시간과 분의 관계를 활용하여 간단하게 풀 수 있었음

H, M = map(int, input().split())      #알람을 맞출 시간을 24시 표현으로 입력함
                                      #입력받은 시간에서 45분 빠른 시간을 출력해야하므로 
if 45<=M:                             #만약 분(M)이 45보다 크거나 같을 경우 if문
    print(H, M-45)                    #시간(H)는 그대로 출력, 분(M)은 45를 뺀 값을 출력
elif M<45:                            #elif문에서 만약 분(M)이 45보다 작다면
    if H<1:                           #다시 if문을 사용해서 시간이 1보다 클 경우를 나눈다.
        print((H+24)-1, (M+60)-45)    #24시 시간 표현을 사용해야하므로 입력받은 시간에 24를 더한 뒤 
                                      #분으로 넘겨 줄 1(한시간)을 빼준다. 분에 60(1시간)을 더한 뒤 45(분)를 뺀다.
    else: print((H-1), (M+60)-45)     #만약 H가 1보다 크다면 1을 빼고 M에 60을 더한 뒤 45를 빼준다.
