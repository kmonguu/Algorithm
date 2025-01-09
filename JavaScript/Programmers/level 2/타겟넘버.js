function solution(numbers, target) {
  let answer = 0;

  function DFS(index, sum) {
    if (index === numbers.length && sum === target) return (answer += 1);
    if (index === numbers.length && sum !== target) return;

    DFS(index + 1, sum + numbers[index]);
    DFS(index + 1, sum - numbers[index]);
  }
  DFS(0, 0);
  return answer;
}
