"use strict";
document.getElementById("mainForm").addEventListener("submit", function(event) {
    event.preventDefault();

let dice = document.getElementById("dice").value;
let diceint = parseInt(dice);
let sum = document.getElementById("sum").value;
let sumint = parseInt(sum);

let result, match=0;
for (let i = 0; i < 10000; i++) {
    let total = 0;
    for (let t = 0; t < diceint; t++) {
        result = Math.floor(Math.random() * 6) + 1;
        total += result;
    }
    if (total === sumint) {
        match++;
    }
}
let sumtotal = ((match / 10000) * 100).toFixed(2);

document.querySelector("#target").innerHTML =
    "The chance of " + diceint + " dice summing to " + sumint + " is " + sumtotal + "%";
});