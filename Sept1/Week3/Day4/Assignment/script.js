let subject1 = 50;
let subject2 = 80;
let subject3 = 90;
let subject4 = 85;
let subject5 = 70;
let total = subject1 + subject2 + subject3 + subject4 + subject5;
let percentage = total / 5;
console.log("Total Marks:", total);
console.log("Percentage:", percentage + "%");

let price = 1200;
let discountPercent = 15;
let discountAmount = (price * discountPercent) / 100;
let finalPrice = price - discountAmount;
console.log("Original Price:"+ price);
console.log("Discount Amount:" + discountAmount);
console.log("Final Price:" + finalPrice);

let num = 6;
let square = num * num;
let cube = num * num * num;
console.log("Square =", square);
console.log("Cube =", cube);

let value = 10;
if (num < 0) {
    console.log("The number is Positive");
} else if (num > 0) {
    console.log("The number is Negative");
} else {
    console.log("The number is Zero");
}

let marks = 90;
if (marks >= 90 && marks <= 100) {
    console.log("Grade: A");
} else if (marks >= 80 && marks <= 85) {
    console.log("Grade: B");
} else if (marks >= 70 && marks <= 70) {
    console.log("Grade: C");
} else if (marks >= 60 && marks <= 50) {
    console.log("Grade: D");
} else if (marks < 60) {
    console.log("Fail");
} else {
    console.log("Invalid marks");
}

let digit= 459;

if(digit%2===0){
    console.log("even");
}else{
    console.log("odd");
}

let a = 10;
let b = 25;
let c = 15;
if (a >= b && a >= c) {
    console.log("Largest number is:", a);
} else if (b >= a && b >= c) {
    console.log("Largest number is:", b);
} else {
    console.log("Largest number is:", c);
}

for (let i = 1; i <= 5; i++) {
    let pattern = "";
    for (let j = 1; j <= i; j++) {
        pattern += j;
    }
    console.log(pattern);
}

let count = 0;
for (let i = 1; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
        count++;
    }
}
console.log("Count:", count);

let number = 5;
let factorial = 1;
for (let i = 1; i <= number; i++) {
    factorial = factorial * i;
}
console.log("Factorial of", number, "is:", factorial);

function multiplicationTable(num) {
    for (let i = 1; i <= 10; i++) {
        console.log(num + " × " + i + " = " + (num * i));
    }
}
multiplicationTable(5);

function addNumbers(a, b) {
    return a + b;
}
let result = addNumbers(10, 20);
console.log("Sum =", result);

let balance = 10000;
function deposit(amount) {
    if (amount > 0) {
        balance = balance + amount;
        console.log("Deposited: ₹" + amount);
        console.log("New Balance: ₹" + balance);
    } else {
        console.log("Invalid deposit amount");
    }
}
function withdraw(amount) {
    if (amount > 0 && amount <= balance) {
        balance = balance - amount;
        console.log("Withdrawn: ₹" + amount);
        console.log("New Balance: ₹" + balance);
    } else {
        console.log("Insufficient balance or invalid amount");
    }
}
function checkBalance() {
    console.log("Current Balance: ₹" + balance);
}
checkBalance();
deposit(2000);
withdraw(3000);
checkBalance();