/**
 * @param {number} n
 * @param {number} x
 * @return {number}
 */
var numberOfWays = function (n, x) {
  const arr = [];
  let i = 1;
  while (true) {
    const p = Math.pow(i, x);
    if (p > n) {
      break;
    }
    arr.push(p);
    i += 1;
  }
  const dp = new Array(n + 1).fill(0);
  dp[0] = 1;
  for (const a of arr) {
    for (let i = n; i >= a; i--) {
      dp[i] = (dp[i] + dp[i - a]) % 1000000007;
    }
  }
  return dp[n];
};
