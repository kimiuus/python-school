"use strict";
document.getElementById("mainForm").addEventListener("submit", function(event) {
    event.preventDefault();

let throws = document.getElementById("throws").value;
let throwsint = parseInt(throws);

let sum=0, thrown=0, result;
do {
result = Math.floor(Math.random() * 6) + 1;
sum += result
thrown += 1
} while (thrown < throwsint);


document.querySelector("#target").innerHTML =
    "" + throwsint +" throws, total " + sum + "";
});