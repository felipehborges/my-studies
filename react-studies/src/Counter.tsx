import { useState } from "react";
import Block from "./components/Block";
import Button from "./components/Button";
import Title from "./components/Title";

interface CounterProps {
  countNumber: number;
}

export default function Counter({ countNumber }: CounterProps): JSX.Element {
  const [count, setCount] = useState(0);

  const onClickHandler = () => setCount((count) => count + countNumber);

  return (
    <Block className="bg-amber-600">
      <Title title="Counter" />

      <p>Press the button to sum!</p>

      <p className="font-bold mt-2">{count}</p>

      <Button
        type="button"
        className="hover:bg-amber-500 active:bg-amber-400 transition-all duration-100"
        onClick={onClickHandler}
      >
        {countNumber}
      </Button>
    </Block>
  );
}
