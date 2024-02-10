import Block from "./components/Block";
import Button from "./components/Button";
import Title from "./components/Title";

export default function RandomImage(): JSX.Element {
  return (
    <Block className="bg-green-700">
      <Title title="Random Image" />

      <p>Press the button to generate a random image!</p>

      <img src="" alt="" />

      <Button>Generate Image</Button>
    </Block>
  );
}
