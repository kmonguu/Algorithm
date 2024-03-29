// 문자열 "hello"에서 각 문자를 오른쪽으로 한 칸씩 밀고 마지막 문자는 맨 앞으로 이동시키면 "ohell"이 됩니다. 이것을 문자열을 민다고 정의한다면 문자열 A와 B가 매개변수로 주어질 때,
// A를 밀어서 B가 될 수 있다면 몇 번 밀어야 하는지 횟수를 반환,
// B가 될 수 없으면 -1을 반환

// 예제
// "hello"	"ohell"	1
// "apple"	"elppa"	-1

// 내가 푼 코드


function solution(A, B) {
    return (B+B).indexOf(A) ?? -1
}


// 다른 사람 풀이

let solution=(a,b)=>(b+b).indexOf(a)
