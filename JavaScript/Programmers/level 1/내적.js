// 길이가 같은 두 1차원 정수 배열 a, b가 매개변수로 주어집니다. a와 b의 내적을 반환
// a와 b의 내적은 a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1] 이다.

// 나의 코드
// for문 반복을 통해 a와 b배열의 인덱스에 접근하여 두 배열의 요소의 각 곱의 누적합을 구했다.

function solution(a, b) {
    var answer = 0;
    for(let i = 0; i < a.length; i++){
        answer += a[i]*b[i]
    }
    return answer;
}


// 다른 사람 코드
// reduce 함수를 사용하여 각 배열의 인덱스의 곱의 누적합을 반환하였다.

function solution(a, b) {
    return a.reduce((acc, _, i) => acc += a[i] * b[i], 0);
}



// 함수 표현식을 이용한 방법

const solution = (a, b) => a.reduce((answer, _, i) => answer + (a[i] * b[i]), 0);
