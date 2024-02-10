import "./App.css";
import Greeter from "./Greeter";
import Counter from "./Counter";
import ToggleEmoji from "./ToggleEmoji";
import RandomImage from "./RandomImage";

// The Block and Title component is not customizable in this component

function App() {
  return (
    <div className="flex flex-col items-center lg:flex-row lg:justify-center gap-5">
      <Greeter name="Hamasaki" />

      <Counter countNumber={6} />

      <ToggleEmoji />

      <RandomImage />

      <p>-----------------------</p>
      <h2>React & TypeScript - The Practical Guide</h2>
    </div>
  );
}

export default App;
