function findKeyWithHighestValue(obj) {
  let highestKey = null;
  let highestValue = -Infinity;

  for (const key in obj) {
    if (obj.hasOwnProperty(key) && typeof obj[key] === "number") {
      if (obj[key] > highestValue) {
        highestValue = obj[key];
        highestKey = key;
      }
    }
  }

  return highestKey;
}

module.exports = findKeyWithHighestValue;
