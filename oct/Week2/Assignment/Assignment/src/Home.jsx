import React from "react";

function Home({ num = 40, obj }) {
  return (
    <div>
      Home Page
      <br />

      Number : {num}
    </div>
  );
}

export default Home;