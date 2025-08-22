/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfFour = function (n) {
  return n > 0 && (0b1010101010101010101010101010101 & n) === n && (n & n - 1) === 0;
};
