import { twMerge } from "tailwind-merge";

interface TitleProps {
  className?: string;
  title: string;
}

export default function Title({ className, title }: TitleProps): JSX.Element {
  return (
    <h1 className={twMerge(className, "font-bold text-2xl mb-2")}>{title}</h1>
  );
}
