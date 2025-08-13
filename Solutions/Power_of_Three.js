/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfThree = function (n) {
  let max3 = 1162261467;
//   while (max3 * 3 < Math.pow(2, 31) - 1) {
//     max3 = max3 * 3;
//   }
  return n > 0 && max3 % n === 0;
};
