import Title from "./components/Title";
import Block from "./components/Block";
import { twMerge } from "tailwind-merge";

interface GreeterProps {
  className?: string;
  name: string;
}

export default function Greeter({
  className,
  name,
}: GreeterProps): JSX.Element {
  return (
    <Block className="bg-red-700">
      <Title title="Greeter" />
      <p className={twMerge(className, "")}>Greetings, {name}!</p>
    </Block>
  );
}

// // Default

// interface GreeterProps {
//   className?: string;
//   name: string;
// }

// const Greeter = (props: GreeterProps) => {
//   return (
//     <div>
//       <h1 className="font-bold text-2xl mb-2">Greeter</h1>
//       <p>Greetings, {props?.name}!</p>
//     </div>
//   );
// };
