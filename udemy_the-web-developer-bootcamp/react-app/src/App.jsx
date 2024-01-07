import { useState } from "react";
// import Counter from './Counter'
import "./App.css";
// import ScoreKeeper from "./ScoreKeeper";
import ShoppingList from "./ShoppingList";
function App() {
  const [count, setCount] = useState(0);

  return (
    <>
      {/* <ScoreKeeper /> */}
      <ShoppingList />
      {/* <Counter /> */}
    </>
  );
}

export default App;
