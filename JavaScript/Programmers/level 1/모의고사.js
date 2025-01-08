function solution(answers) {
  const first = [1, 2, 3, 4, 5];
  const second = [2, 1, 2, 3, 2, 4, 2, 5];
  const third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

  let result = [0, 0, 0];
  for (let i in answers) {
    if (answers[i] === first[i % first.length]) result[0] += 1;
    if (answers[i] === second[i % second.length]) result[1] += 1;
    if (answers[i] === third[i % third.length]) result[2] += 1;
  }
  const max = Math.max(...result);
  const maxIndex = result
    .map((num, index) => (num === max ? index + 1 : -1))
    .filter((num) => num !== -1);
  return maxIndex;
}
