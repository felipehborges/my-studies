import React from "react";
import ReactDOM from "react-dom/client";
// import App from "./App.tsx";
import AppCourse from "./courses/react-typescript-the-practical-guide/index.tsx";
import "./index.css";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    {/* <App /> */}
    <AppCourse />
  </React.StrictMode>
);
