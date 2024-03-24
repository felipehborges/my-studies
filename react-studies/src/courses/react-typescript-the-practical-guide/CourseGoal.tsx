import { type ReactNode } from "react";

interface CourseGoalProps {
  title: string;
  children: ReactNode;
}

export default function CourseGoal({
  title,
  children,
}: CourseGoalProps): JSX.Element {
  return (
    <article>
      <div>
        <h2>{title}</h2>
        <p>{children}</p>
      </div>
    </article>
  );
}
