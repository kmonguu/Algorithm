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
// 미리 배열을 n길이 만큼 생성해두고 map 함수를 이용하여 x를 제곱하여 배열에 채워넣습니다.

function solution(x, n) {
    return Array(n).fill(x).map((v, i) => (i + 1) * v)
}
