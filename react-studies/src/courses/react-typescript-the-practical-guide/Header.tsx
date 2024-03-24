import { type ReactNode } from "react";

interface HeaderProps {
  image: {
    src: string;
    alt: string;
  };
  children: ReactNode;
}

export default function Header({ children, image }: HeaderProps): JSX.Element {
  return (
    <div>
      {image?.src}
      {image?.alt}
      {children}
    </div>
  );
}
