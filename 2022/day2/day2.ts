import * as fs from 'fs';
import * as readline from 'readline';

const scores: number[] = [];

enum RPSMe {
  Rock = 'X',
  Paper = 'Y',
  Scissors = 'Z',
}

enum RPSOpp {
  Rock = 'A',
  Paper = 'B',
  Scissors = 'C',
}

const readFile = async () => {
  const rl = readline.createInterface({
    input: fs.createReadStream('day2-input'),
    crlfDelay: Infinity,
  });

  rl.on('line', (line) => {
    const [opp, me] = line.split(' ');
    let roundScore = 0;
    if (me === RPSMe.Rock) {
      roundScore += 1;
      if (opp === RPSOpp.Rock) roundScore += 3;
      if (opp === RPSOpp.Scissors) roundScore += 6;
    }
    if (me === RPSMe.Paper) {
      roundScore += 2;
      if (opp === RPSOpp.Paper) roundScore += 3;
      if (opp === RPSOpp.Rock) roundScore += 6;
    }
    if (me === RPSMe.Scissors) {
      roundScore += 3;
      if (opp === RPSOpp.Scissors) roundScore += 3;
      if (opp === RPSOpp.Paper) roundScore += 6;
    }
    scores.push(roundScore);
  });

  await new Promise((res) => rl.once('close', res));
};

const read = async () => {
  await readFile();
  console.log(scores);
  console.log(scores.reduce((partialSum, a) => partialSum + a, 0)); // 1. CORRECT!
};

read();
