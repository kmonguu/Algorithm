#EOF(End Of File)예외처리를 알아보는 문제 더이상의 입력값이 존재하지 않으면 예외처리로 넘어감.
#try에서 코드를 실행하던 중 오류가 발생하면 예외적으로 except로 넘어가 예외를 처리한다.

while True:
    try:                                  
        A, B = map(int, input().split())
        print(A+B)
    except EOFError: #EOFError가 발생할 때만 except 블록을 수행한다는 의미이다.
        break        #오류가 발생하면 while문을 종료한다.
