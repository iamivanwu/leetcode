/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function (nums) {
  const res = new Array(nums.length).fill(Infinity);
  res[0] = 0;
  for (let i = 0; i < nums.length; i++) {
    for (let j = 1; j < nums[i] + 1; j++) {
      if (i + j < nums.length) {
        res[i + j] = Math.min(res[i + j], res[i] + 1);
      }
    }
  }
  return res[res.length - 1];
};
