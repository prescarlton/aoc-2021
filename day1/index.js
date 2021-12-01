const fs = require('fs');

const depths = fs
    .readFileSync('./input.txt', 'utf8')
    .toString()
    .trim()
    .split('\n')
    .map(depth => parseInt(depth))

let total1 = 0;
for (let i = 0; i < depths.length - 1; i++) {
    let curr = depths[i];
    let next = depths[i + 1]
    if (next > curr)
        total1++;

}
console.log(total1)