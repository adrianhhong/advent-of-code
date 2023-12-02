import * as fs from 'fs';
import * as readline from 'readline';

const readFile = async () => {
  const rl = readline.createInterface({
    input: fs.createReadStream('input'),
    crlfDelay: Infinity,
  });

  rl.on('line', (line) => {
    const dict: Record<string, number | undefined> = {};
    const chars = line.split('');
    for (let i = 4; i < chars.length; i++) {
      const window = chars.slice(i - 4, i);
      console.log(window);
      if (new Set(window).size === window.length) return console.log(i);
    }
  });

  await new Promise((res) => rl.once('close', res));
};

const read = async () => {
  await readFile();
};

read();
