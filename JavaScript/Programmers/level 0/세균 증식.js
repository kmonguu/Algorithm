// 어떤 세균은 1시간에 두배만큼 증식한다고 합니다. 처음 세균의 마리수 n과 경과한 시간 t가 매개변수로 주어질 때 t시간 후 세균의 수를 반환

// 예제
// 2	10	2048
// 7	15	229,376

// 내가 푼 코드
function solution(n, t) {
    var answer = n;
    for(let i=1; i<=t; i++){
        answer *= 2;
    }
    return answer;
}

// js 내장함수 사용한 방법
// pow로 제곱을 구현할 수 있다.

function solution(n, t) {
    return n*Math.pow(2,t);
}


// 비트 연산자를 사용한 방법

function solution(n, t) {
  return n << t;
}
