import * as fs from 'fs';
import * as readline from 'readline';

const rucksacks: string[][] = [];
const badgePriority: number[] = [];

const readFile = async () => {
  const rl = readline.createInterface({
    input: fs.createReadStream('day3-input'),
    crlfDelay: Infinity,
  });

  rl.on('line', (line) => {
    rucksacks.push(line.split(''));
  });

  await new Promise((res) => rl.once('close', res));
};

const read = async () => {
  await readFile();
  for (let i = 0; i < rucksacks.length / 3; i++) {
    let commonChar = '';
    rucksacks[i * 3].forEach((charA) => {
      rucksacks[i * 3 + 1].forEach((charB) => {
        rucksacks[i * 3 + 2].forEach((charC) => {
          if (charA === charB && charB === charC) commonChar = charA;
        });
      });
    });
    const ascii = commonChar.charCodeAt(0);
    if (ascii >= 97 && ascii <= 122) badgePriority.push(ascii - 96);
    if (ascii >= 65 && ascii <= 90) badgePriority.push(ascii - 38);
    console.log(commonChar, ascii, badgePriority);
  }
  console.log(badgePriority.reduce((partialSum, a) => partialSum + a, 0)); // correct!
};

read();
