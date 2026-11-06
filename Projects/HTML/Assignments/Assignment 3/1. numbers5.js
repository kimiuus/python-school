"use strict";
document.getElementById("mainForm").addEventListener("submit", function(event) {
    event.preventDefault();


const numbers = [];
for (let i = 1; i <= 5; i++) {
    let value = document.getElementById("num"+ i).value;
    numbers.unshift(value);
}
console.log(numbers);
});