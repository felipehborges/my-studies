import { useState } from "react";
import Block from "./components/Block";
import Button from "./components/Button";
import Title from "./components/Title";

export default function ToggleEmoji(): JSX.Element {
  const [changeEmoji, setChangeEmoji] = useState("😈");

  const toggleEmojiHandler = () => {
    setChangeEmoji((prevEmoji) => (prevEmoji === "😈" ? "😇" : "😈"));
  };

  return (
    <Block className="bg-cyan-700">
      <Title title="Toggle Emoji" />

      <p>Press the button to toggle emoji!</p>

      <p className="mt-4">{changeEmoji}</p>

      <Button
        className="hover:bg-cyan-600 active:bg-cyan-500 transition-all duration-150"
        onClick={toggleEmojiHandler}
      >
        Toggle
      </Button>
    </Block>
  );
}
