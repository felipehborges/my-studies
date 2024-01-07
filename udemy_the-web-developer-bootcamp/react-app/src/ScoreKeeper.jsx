import { useState } from "react";

export default function ScoreKeeper() {
  const [scores, setScores] = useState({ p1Score: 0, p2Score: 0 });

  function increaseP1Score() {
    const newScores = { ...scores, p1Score: scores.p1Score + 1 };
    setScores(newScores);
  }

  function increaseP2Score() {
    const newScores = { ...scores, p2Score: scores.p2Score + 1 };
    setScores(newScores);
  }
  //   function increaseP2Score() {
  //     scores.p2Score += 1;
  //     console.log(scores);
  //     setScores(scores);
  //   }
  //   const increaseP1Score = () => {};
  //   const increaseP2Score = () => {};

  return (
    <>
      <p>Player 1:</p>
      <h1>{scores.p1Score}</h1>
      <p>Player 2:</p>
      <h1>{scores.p2Score}</h1>
      <hr />
      <button onClick={increaseP1Score}>+1 = P1</button>
      <hr />
      <button onClick={increaseP2Score}>+1 = P2</button>
      <hr />
    </>
  );
}
