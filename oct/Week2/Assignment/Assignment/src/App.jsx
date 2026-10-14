import React from "react";
import Home from "./Home";
import About from "./About";
import Card from "./Card";

function App() {
  let a;

  let products = [
    {
      img: "https://static1.xdaimages.com/wordpress/wp-content/uploads/wm/2024/06/surface-laptop-7-3.jpg",
      title: "Laptop",
      desc: "This is a powerful laptop for students and professionals",
      price: "₹55,000",
    },
    {
      img: "https://tse1.mm.bing.net/th/id/OIP.PDvBf7QLNkDN6nHOHR16hAHaHa?r=0&pid=Api&h=220&P=0",
      title: "Smartphone",
      desc: "This is a modern smartphone with a beautiful display",
      price: "₹25,000",
    },
    {
      img: "https://tse1.mm.bing.net/th/id/OIP.3WZN-1_lqJmixwLM1pqpAgHaHa?r=0&pid=Api&h=220&P=0",
      title: "Headphones",
      desc: "These are wireless headphones with excellent sound quality",
      price: "₹3,000",
    },
    {
      img: "https://tse3.mm.bing.net/th/id/OIP.pX60H_w4HC5QF49xrcq14QHaHa?r=0&pid=Api&h=220&P=0",
      title: "Smart Watch",
      desc: "This is a smart watch with fitness tracking features",
      price: "₹5,000",
    },
  ];

  return (
    <div className="max-w-6xl m-auto">
      

      
      <About children={"hello Bhai"}>
       
        <p>This is my Product page</p>
      </About>

      <div className="grid grid-cols-4 gap-4">
        {products?.map((product) => (
          <Card product={product} />
        ))}
      </div>
    </div>
  );
}

export default App;