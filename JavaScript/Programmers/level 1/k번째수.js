function solution(array, commands) {
  let result = [];
  commands.forEach(([i, j, k]) => {
    result.push(array.slice(i - 1, j).sort((a, b) => a - b)[k - 1]);
  });
  return result;
}
