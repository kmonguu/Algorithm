// 정수 x와 자연수 n을 입력 받아, x부터 시작하여 x씩 증가하는 숫자를 n개 지니는 리스트를 반환

// 나의 코드
function solution(x, n) {
    let answer = [];
    for (let i = 1; i < n+1; i++){
        answer.push(x*i);
    }
    return answer;
}


// 다른 사람 코드
// 미리 배열을 n길이 만큼 생성해두고 map 함수를 이용하여 x를 제곱하여 배열에 채워넣음.

function solution(x, n) {
    return Array(n).fill(x).map((v, i) => (i + 1) * v)
}


// fill(0)으로 배열을 미리 0으로 채운 다음 map 메소드를 실행한 방법
// Array()와 new Array()는 차이가 없으므로 배열 선언할 때 아무거나 사용해도 무방

function solution(x, n) {
    return new Array(n).fill(0).map((_, i) => (i + 1) * x);
}
