// array의 각 요소 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환, 만약 나누어 떨어지는 요소가 하나도 없다면 -1을 반환

// 내가 푼 코드
// array의 각 요소 중 divisor로 나누어 떨어지는 값을 answer에 저장한 후, answer배열에 요소가 존재한다면 오름차순 정렬 후 반환
// answer가 빈 배열이라면 [-1]을 반환

function solution(arr, divisor) {
    let answer = [];
    for (let i = 0; i <= arr.length; i++) {
        if (arr[i] % divisor == 0) {
            answer.push(arr[i])
        }
    }
    return answer.length ? answer.sort((a, b) => a - b) : [-1];  
}
