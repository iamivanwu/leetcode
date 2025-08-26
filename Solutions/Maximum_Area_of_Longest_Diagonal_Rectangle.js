/**
 * @param {number[][]} dimensions
 * @return {number}
 */
var areaOfMaxDiagonal = function (dimensions) {
  let m = -1;
  let index = 0;
  for (let i = 0; i < dimensions.length; i++) {
    if (dimensions[i][0] * dimensions[i][0] + dimensions[i][1] * dimensions[i][1] > m) {
      index = i;
      m = dimensions[i][0] * dimensions[i][0] + dimensions[i][1] * dimensions[i][1];
    } else if (dimensions[i][0] * dimensions[i][0] + dimensions[i][1] * dimensions[i][1] === m && dimensions[i][0] * dimensions[i][1] > dimensions[index][0] * dimensions[index][1]) {
      index = i;
    }
  }
  return dimensions[index][0] * dimensions[index][1];
};
