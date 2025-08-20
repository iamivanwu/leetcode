/**
 * @param {number[]} nums
 * @return {number}
 */
var zeroFilledSubarray = function (nums) {
  const cal = (n) => {
    return (n * (n + 1)) / 2;
  };
  let count = 0;
  let res = 0;
  for (let i = 0; i <= nums.length; i++) {
    if (nums[i] === 0) {
      count += 1;
    }
    if (nums[i] !== 0 && count !== 0) {
      res += cal(count);
      count = 0;
    }
  }
  if (count !== 0) {
    res += cal(count);
    count = 0;
  }
  return res;
};
