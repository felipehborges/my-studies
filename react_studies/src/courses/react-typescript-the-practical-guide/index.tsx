import CourseGoal from "./CourseGoal";
import Header from "./Header";

function AppCourse() {
  return (
    <div className="w-full flex justify-center">
      <Header image={{ alt: "A list of goals", src: "XABLAU" }}>
        <h1>Your course goals</h1>
      </Header>

      <CourseGoal title={""}>''</CourseGoal>
    </div>
  );
}

export default AppCourse;
