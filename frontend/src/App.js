import React from "react";
import NavBar from "./Components/NavBar/NavBar";
import CardPresentation from "./Components/CardPresentation/CardPresentation";
import SmallCard from "./Components/Card/Card";
import Mode from "./Components/Mode/Mode";
import { useSelector } from "react-redux";
import { body } from "./style";

const App = () => {
  const mode = useSelector((state) => state.knowledge.mode);

  return (
    <section style={body}>
      <NavBar></NavBar>
      {mode && <Mode />}
      <CardPresentation></CardPresentation>
      <SmallCard></SmallCard>
    </section>
  );
};

export default App;
