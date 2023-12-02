import fs from 'fs';
import readline from 'readline';

const sumsArray = [0];

const readFile = async () => {
  const rl = readline.createInterface({
    input: fs.createReadStream('day1-input'),
    crlfDelay: Infinity,
  });

  rl.on('line', (line) => {
    if (line === '') {
      sumsArray.push(0);
    } else {
      sumsArray.push(sumsArray.pop() + parseInt(line));
    }
  });

  await new Promise((res) => rl.once('close', res));
};

await readFile();
console.log(sumsArray);
console.log(Math.max(...sumsArray)); // 1. CORRECT!

const sortedSumsArray = sumsArray.sort((a, b) => {
  return b - a;
});
console.log(sortedSumsArray);
console.log(sortedSumsArray[0] + sortedSumsArray[1] + sortedSumsArray[2]); // 2. CORRECT!
