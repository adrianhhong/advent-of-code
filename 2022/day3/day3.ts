import * as fs from 'fs';
import * as readline from 'readline';

const items: number[] = [];

const readFile = async () => {
  const rl = readline.createInterface({
    input: fs.createReadStream('day3-input'),
    crlfDelay: Infinity,
  });

  rl.on('line', (line) => {
    const mid = line.length / 2;
    const allCharacters = line.split('');
    const bagA = allCharacters.slice(0, mid);
    const bagB = allCharacters.slice(mid);
    let commonChar = '';
    bagA.forEach((charA) => {
      bagB.forEach((charB) => {
        if (charA === charB) commonChar = charA;
      });
    });
    const ascii = commonChar.charCodeAt(0);
    if (ascii >= 97 && ascii <= 122) items.push(ascii - 96);
    if (ascii >= 65 && ascii <= 90) items.push(ascii - 38);
    console.log(commonChar, ascii, items);
  });

  await new Promise((res) => rl.once('close', res));
};

const read = async () => {
  await readFile();
  console.log(items.length);
  console.log(items.reduce((partialSum, a) => partialSum + a, 0)); // correct
};

read();
