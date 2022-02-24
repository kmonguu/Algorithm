// 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 문제

// 내가 푼 코드
// answer에 n의 크기만큼 배열을 할당하고 true로 배열을 채워준다.
// 0과 1은 소수가 아니므로 false를 저장한다.
// i가 소수일 때, i의 배수는 소수가 아니므로 i의 배수들은 false로 저장한다.
// answer에서 요소가 true인 배열의 길이를 구해 반환한다.

// 배열에서 특정 문자의 개수를 구하는 방법에서 filter를 사용하는 방법을 알게됨

function solution(n) {
    let answer = Array(n+1).fill(true).fill(false, 0, 2)
    
    for(let i = 2; i < +(n**0.5)+1; i++) {
        for (let j = i*i; j < (n+1); j+=i) {
            answer[j] = false;
        }
    }
    return answer.filter(result => result).length;
}
