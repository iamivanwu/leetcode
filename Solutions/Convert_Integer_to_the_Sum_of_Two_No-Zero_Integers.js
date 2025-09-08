/**
 * @param {number} n
 * @return {number[]}
 */
var getNoZeroIntegers = function (n) {
  let res = 1;
  while (res < n) {
    if (hasZero(res) || hasZero(n - res)) {
      res += 1;
    } else {
      return [res, n - res];
    }
  }
};

var hasZero = (n) => {
  while (n > 0) {
    if (n % 10 === 0) {
      return true;
    }
    n = Math.floor(n / 10);
  }
  return false;
};
