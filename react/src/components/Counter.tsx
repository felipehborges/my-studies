import { useState } from "react";

export default function Counter() {
  const [count, setCount] = useState(0);

  const increaseCount = () => {
    setCount((c) => c + 1);
  };

  const clearCount = () => {
    setCount(0);
  };

  //   How can I take the submit value and pass it to the "increaseCount" button?
  const onSubmitHandler = () => {};

  return (
    <>
      <h1>Counter</h1>
      <p>{count}</p>
      <button onClick={increaseCount}>+1</button>
      <p></p>
      <button onClick={clearCount}>Clear</button>
      <p></p>
      <hr />
      <p></p>
      <form onSubmit={onSubmitHandler}>
        <input type="number" placeholder="Define number" />
        <p></p>
        <button type="submit">Submit</button>
      </form>
    </>
  );
}
