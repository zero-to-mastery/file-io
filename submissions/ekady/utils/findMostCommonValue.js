const fs = require("fs");
const csv = require("csv-parser");

const findMostCommonValue = (filePath, columnName) => {
  const valueCountMap = new Map();

  fs.createReadStream(filePath)
    .pipe(csv())
    .on("data", (row) => {
      const columnValue = row[columnName];
      if (columnValue) {
        if (valueCountMap.has(columnValue)) {
          valueCountMap.set(columnValue, valueCountMap.get(columnValue) + 1);
        } else {
          valueCountMap.set(columnValue, 1);
        }
      }
    })
    .on("end", () => {
      let mostCommonValue = "";
      let maxCount = 0;

      valueCountMap.forEach((count, value) => {
        if (count > maxCount) {
          mostCommonValue = value;
          maxCount = count;
        }
      });

      console.log(
        `Most common value in column '${columnName}': ${mostCommonValue} (Count: ${maxCount})`
      );
    });
};

module.exports = findMostCommonValue;
