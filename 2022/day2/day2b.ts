import * as fs from 'fs';
import * as readline from 'readline';

const scores: number[] = [];

enum Result {
  Lose = 'X',
  Draw = 'Y',
  Win = 'Z',
}

enum RPSMe {
  Rock = 1,
  Paper = 2,
  Scissors = 3,
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
    if (me === Result.Lose) {
      if (opp === RPSOpp.Rock) roundScore += RPSMe.Scissors; // lose with scissors
      if (opp === RPSOpp.Paper) roundScore += RPSMe.Rock; // lose with rock
      if (opp === RPSOpp.Scissors) roundScore += RPSMe.Paper; // lose with paper
    }
    if (me === Result.Draw) {
      roundScore += 3;
      if (opp === RPSOpp.Rock) roundScore += RPSMe.Rock; // draw with rock
      if (opp === RPSOpp.Paper) roundScore += RPSMe.Paper; // draw with paper
      if (opp === RPSOpp.Scissors) roundScore += RPSMe.Scissors; // draw with scissors
    }
    if (me === Result.Win) {
      roundScore += 6;
      if (opp === RPSOpp.Rock) roundScore += RPSMe.Paper; // win with paper
      if (opp === RPSOpp.Paper) roundScore += RPSMe.Scissors; // win with scissors
      if (opp === RPSOpp.Scissors) roundScore += RPSMe.Rock; // win with rock
    }
    scores.push(roundScore);
  });

  await new Promise((res) => rl.once('close', res));
};

const read = async () => {
  await readFile();
  console.log(scores);
  console.log(scores.reduce((partialSum, a) => partialSum + a, 0)); // 2. CORRECT!
};

read();
