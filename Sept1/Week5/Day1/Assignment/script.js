

let registerForm = document.querySelector("#registerForm");

let loginForm = document.querySelector("#loginForm");

let registerBox = document.querySelector("#registerBox");

let loginBox = document.querySelector("#loginBox");

let dashboard = document.querySelector("#dashboard");




function showLogin() {

    registerBox.classList.add("hidden");

    dashboard.classList.add("hidden");

    loginBox.classList.remove("hidden");
}


function showRegister() {

    loginBox.classList.add("hidden");

    dashboard.classList.add("hidden");

    registerBox.classList.remove("hidden");
}




registerForm.addEventListener("submit", function (e) {

    e.preventDefault();


    

    let name =
        document.querySelector("#name").value.trim();

    let age =
        document.querySelector("#age").value.trim();

    let phone =
        document.querySelector("#phone").value.trim();

    let email =
        document.querySelector("#registerEmail")
        .value.trim()
        .toLowerCase();

    let password =
        document.querySelector("#registerPassword").value;


    

    if (!name || !age || !phone || !email || !password) {

        alert("Please fill all the fields.");

        return;
    }


    
    if (age < 1 || age > 100) {

        alert("Please enter a valid age.");

        return;
    }


    

    if (!/^[0-9]{10}$/.test(phone)) {

        alert("Please enter a valid 10 digit phone number.");

        return;
    }


    

    if (password.length < 6) {

        alert("Password must contain at least 6 characters.");

        return;
    }


   
    let users =
        JSON.parse(
            localStorage.getItem("usersData")
        ) || [];


    

    let userExists = users.some(function (user) {

        return user.email === email;

    });


    if (userExists) {

        alert("User with this email already exists.");

        return;
    }


    
    

    let newUser = {

        name: name,

        age: age,

        phone: phone,

        email: email,

        password: password

    };


    

    users.push(newUser);


    
    localStorage.setItem(
        "usersData",
        JSON.stringify(users)
    );


    
    alert("Registration successful!");


   

    registerForm.reset();


    

    showLogin();

});




loginForm.addEventListener("submit", function (e) {

    e.preventDefault();


    

    let email =
        document.querySelector("#loginEmail")
        .value.trim()
        .toLowerCase();

    let password =
        document.querySelector("#loginPassword").value;


    if (!email || !password) {

        alert("Please enter email and password.");

        return;
    }


   
    let users =
        JSON.parse(
            localStorage.getItem("usersData")
        ) || [];


    

    let existingUser = users.find(function (user) {

        return user.email === email;

    });


    
    if (!existingUser) {

        alert("User does not exist.");

        return;
    }


    
    if (existingUser.password !== password) {

        alert("Invalid password.");

        return;
    }


    

    alert("Login successful!");



    loginForm.reset();


    

    loginBox.classList.add("hidden");


    
    dashboard.classList.remove("hidden");


    

    document.querySelector("#welcomeUser").textContent =
        "Welcome, " + existingUser.name + "!";

});




function logout() {

    dashboard.classList.add("hidden");

    loginBox.classList.remove("hidden");

    alert("Logged out successfully.");

}




function togglePassword(inputId, icon) {

    let input =
        document.querySelector("#" + inputId);


    if (input.type === "password") {

        input.type = "text";

        icon.textContent = "hide";

    } else {

        input.type = "password";

        icon.textContent = "show";

    }

}