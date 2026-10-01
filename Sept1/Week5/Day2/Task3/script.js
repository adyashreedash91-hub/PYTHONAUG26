 async function getData() {

  let res = await fetch(
    "https://jsonplaceholder.typicode.com/posts"
  );

 let data = await res.json();

  console.log(data);

  let container = document.querySelector("#container");

   data.forEach((post) => {

    let div = document.createElement("div");

    div.innerHTML = `
      <h2>${post.title}</h2>
       <p>${post.body}</p>
       <hr>
     `;

    container.append(div);

  });
 }

 getData();
