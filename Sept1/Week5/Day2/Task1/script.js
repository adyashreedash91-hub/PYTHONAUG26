let registerForm = document.querySelector(".register");

let inputs = document.querySelectorAll(".register>input");

registerForm.addEventListener("submit", (e) => {
  e.preventDefault();

  let name = inputs[0].value;
  let age = inputs[1].value;
  let phone = inputs[2].value;
  let email = inputs[3].value;
  let password = inputs[4].value;
  if (!name || !age || !phone || !email || !password) {
    alert("Kindly fill all the fields");
    return;
  }
  let existingUsers =
    JSON.parse(localStorage.getItem("usersData")) || []

  let newUser = {
    name,
    age,
    phone,
    email,
    password
  };
  let newUserList = [...existingUsers, newUser];
  localStorage.setItem(
    "usersData",
    JSON.stringify(newUserList)
  );
  inputs[0].value = "";
  inputs[1].value = "";
  inputs[2].value = "";
  inputs[3].value = "";
  inputs[4].value = "";
  alert("Registration successful!");
});