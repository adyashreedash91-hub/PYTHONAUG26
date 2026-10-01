let loginForm = document.querySelector(".login");
let loginInputs = document.querySelectorAll(".login>input");

loginForm.addEventListener("submit", (e) => {
  e.preventDefault();
  
  let email = loginInputs[0].value;
  let password = loginInputs[1].value;
  if (!email || !password) {
    alert("kindly fill the field");
    return;
  }
  let existingUsers =
    JSON.parse(localStorage.getItem("usersData")) || [];
  let existingUser = existingUsers.find(
    (v) => v.email == email
  );

  if (!existingUser) {
    alert("user not exist");
  } else {
    if (existingUser.password == password) {
      alert("login success");
      loginInputs[0].value = "";
      loginInputs[1].value = "";
    } else {
      alert("Invalid password");
    }
  }
});