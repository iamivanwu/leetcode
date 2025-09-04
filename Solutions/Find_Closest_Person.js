/**
 * @param {number} x
 * @param {number} y
 * @param {number} z
 * @return {number}
 */
var findClosest = function (x, y, z) {
  return Math.abs(z - x) > Math.abs(z - y) ? 2 : Math.abs(z - x) < Math.abs(z - y) ? 1 : 0;
};
