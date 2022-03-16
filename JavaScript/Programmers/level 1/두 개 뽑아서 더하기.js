// 정수 배열 numbers가 주어질 때 numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 반환

// 내가 푼 코드
// 중첩 for문을 사용하여 numbers 배열 중 두 개의 수를 뽑아 arr배열에 push
// 중복되는 값이 없으면서 오름차순으로 정렬된 배열을 반환하기 위해 전개 연산자를 사용하여 set
// 오름차순 정렬 후 반환

function solution(numbers) {
    const arr = [];
    
    for (let i = 0; i < numbers.length; i++) {
        for (let j = i+1; j < numbers.length; j++) {
            arr.push(numbers[i] + numbers[j]);
        }
    }
    const answer = [...new Set(arr)]
    return answer.sort((a, b) => a - b);
}
