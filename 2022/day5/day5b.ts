import * as fs from 'fs';
import * as readline from 'readline';

let stacks: string[][] = [
  [],
  ['Z', 'J', 'G'],
  ['Q', 'L', 'R', 'P', 'W', 'F', 'V', 'C'],
  ['F', 'P', 'M', 'C', 'L', 'G', 'R'],
  ['L', 'F', 'B', 'W', 'P', 'H', 'M'],
  ['G', 'C', 'F', 'S', 'V', 'Q'],
  ['W', 'H', 'J', 'Z', 'M', 'Q', 'T', 'L'],
  ['H', 'F', 'S', 'B', 'V'],
  ['F', 'J', 'Z', 'S'],
  ['M', 'C', 'D', 'P', 'F', 'H', 'B', 'T'],
];
let lineNo = 0;

const readFile = async () => {
  const rl = readline.createInterface({
    input: fs.createReadStream('input'),
    crlfDelay: Infinity,
  });

  rl.on('line', (line) => {
    lineNo++;
    if (lineNo > 10) {
      console.log(line);
      const rest = line.split('move ');
      const rest2 = rest[1].split(' from ');
      const [moveAmount, fromTo] = rest2;
      const rest3 = fromTo.split(' to ');
      const [fromStack, toStack] = rest3;
      console.log(moveAmount, fromStack, toStack);
      const fromLength = stacks[parseInt(fromStack)].length;

      const popped = stacks[parseInt(fromStack)].splice(
        fromLength - parseInt(moveAmount),
        fromLength
      );

      stacks[parseInt(toStack)] = [...stacks[parseInt(toStack)], ...popped];
    }
  });

  await new Promise((res) => rl.once('close', res));
};

const read = async () => {
  await readFile();
  const topStack: string[] = [];
  stacks.forEach((s) => {
    const top = s.pop();
    topStack.push(top ?? '');
  });
  console.log(topStack);
};

read();
