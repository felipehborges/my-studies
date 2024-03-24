import { type ReactNode } from "react";
import { twMerge } from "tailwind-merge";

interface BlockProps {
  className?: string;
  children: ReactNode;
}

export default function Block({
  className,
  children,
}: BlockProps): JSX.Element {
  return (
    <div
      className={twMerge(
        className,
        "cursor-default w-1/2 max-w-[90%] rounded-2xl p-5 ring-4 ring-zinc-600 hover:ring-zinc-400 transition-all duration-150 text-center"
      )}
    >
      {children}
    </div>
  );
}
