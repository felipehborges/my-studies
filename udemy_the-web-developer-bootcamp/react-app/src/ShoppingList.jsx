import { useState } from "react";

export default function ShoppingList() {
  const fruits = ["Banana", "Apple", "Papaya", "Melon", "Strawberry"];
  const [shoppingList, setShoppingList] = useState([]);

  const incrementArray = () => {
    setShoppingList(fruits[0]);
  };

  return (
    <>
      <h2>Shopping List</h2>

      <p>{shoppingList}</p>
      <button onClick={incrementArray}>Increment</button>
    </>
  );
}
