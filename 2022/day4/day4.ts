import * as fs from 'fs';
import * as readline from 'readline';

let total = 0;

const readFile = async () => {
  const rl = readline.createInterface({
    input: fs.createReadStream('day4-input'),
    crlfDelay: Infinity,
  });

  rl.on('line', (line) => {
    const [areaA, areaB] = line.split(',');
    const [startA, endA] = areaA
      .split('-')
      .map((numAsString) => parseInt(numAsString));
    const [startB, endB] = areaB
      .split('-')
      .map((numAsString) => parseInt(numAsString));
    console.log(startA, endA, startB, endB);
    if (endA - startA > endB - startB) {
      // A has bigger range than B
      console.log('A>B');
      if (startA <= startB && endA >= endB) total++;
    } else if (endA - startA < endB - startB) {
      // B has bigger range than A
      console.log('A<B');
      if (startB <= startA && endB >= endA) total++;
    } else {
      // same length
      console.log('A==B');
      if (startA === startB && endA === endB) total++;
    }
    console.log(total);
  });

  await new Promise((res) => rl.once('close', res));
};

const read = async () => {
  await readFile();
  console.log(total);
};

read();
