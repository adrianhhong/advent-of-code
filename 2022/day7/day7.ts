import * as fs from 'fs';
import * as readline from 'readline';


class FileSysNode {
  name: string
  children: FileSysNode[]

  constructor(name: string) {
    this.name = name;
    this.children = [];
  }
}

const fileSys = new FileSysNode('root');
const pointer = [];

const readFile = async () => {
  const rl = readline.createInterface({
    input: fs.createReadStream('input'),
    crlfDelay: Infinity,
  });

  rl.on('line', (line) => {
    const split = line.split(' ');
    if (split[0] === '$') {
      // command
      if (split[1] === 'cd') {
        if (split[2] === '/') {
          //root
        } else if (split[2] === '..') {
          //go back
        } else {
          // some path
        }
      }
    } else {
      // a file
      if (split[0] !== 'dir') {
        const size = split[1];
        // const file = split[2];
        fileSys[]
      }
    }
  });

  await new Promise((res) => rl.once('close', res));
};

const read = async () => {
  await readFile();
};

read();

