// 정수를 담고 있는 배열 arr의 평균값을 반환

// 풀이
// for문에서 인라인 변수 i를 선언하여 0부터 arr 배열의 길이까지 증가하도록 반복문을 실행하고 arr[i]의 값을 반복적으로 더하여 answer에 저장한다.
// arr의 합이 들어있는 answer에 arr의 길이만큼 나눈 값을 반환

// 코드
function solution(arr) {
    let answer = 0;
    for (let i = 0; i < arr.length; i++){
        answer += arr[i]
    }
    return answer/arr.length;
}
