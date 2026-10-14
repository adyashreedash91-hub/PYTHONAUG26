import React from "react";

function Card({ product }) {
  return (
    <div className="w-60 p-1 border rounded shadow-xl">

      <div className="w-full h-40 overflow-hidden rounded-xl">
        <img
          src={product?.img}
          alt=""
          className="w-full h-full rounded object-cover"
        />
      </div>

      <p className="text-center font-bold text-xl">
        {product?.title || "No Title"}
      </p>

      <p className="text-start text-gray-500 text-sm line-clamp-3">
        {product?.desc}
      </p>

      <p className="text-center font-bold text-green-600 text-lg">
        {product?.price}
      </p>

    </div>
  );
}

export default Card;