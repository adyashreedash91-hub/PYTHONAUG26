import React from 'react'

function App() {
  let[Count, setCount] =useState(0);
  let[name, setName]=useState("");
  let[age,setAge]=useState(0);
  let[email,setEmail]=useState("");

  let handleClick = useState(0);
  setCount((prev) => prev +1);

  return (

    <div className ="max-w-7Xl mx-auto">
      App
      <br/>
      <div className="text-2xl" font-bold>
        <p>Count : {Count}</p>
      </div>
      <button>
        className="bg-white text-blue-500 hover "
      </button>

      function App() {
        
      }
    </div>
  )
}

export default App
