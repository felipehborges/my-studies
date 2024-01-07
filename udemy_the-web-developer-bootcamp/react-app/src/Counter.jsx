import { useState } from "react";

export default function Counter() {
  const [count, setCount] = useState(0);

  const incrementCount = () => {
    setCount((count) => count + 1);
    setCount((count) => count + 1);
    setCount((count) => count + 1);
  };

  return (
    <>
      <h2>{count}</h2>
      <button onClick={incrementCount}>+1</button>
    </>
  );
}
