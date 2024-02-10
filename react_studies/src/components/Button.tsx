import { type ReactNode } from "react";
import { twMerge } from "tailwind-merge";

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  className?: string;
  children: ReactNode;
}

// value, type and onClick types are already defined in React component

export default function Button({
  className,
  onClick,
  type,
  children,
}: ButtonProps): JSX.Element {
  return (
    <button
      type={type}
      onClick={onClick}
      className={twMerge(
        className,
        "ring-2 ring-zinc-200 hover:ring-white transition-all duration-100 py-2 px-5 m-4 rounded-xl"
      )}
    >
      {children}
    </button>
  );
}
