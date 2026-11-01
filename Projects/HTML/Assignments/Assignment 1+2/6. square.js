"use strict";
document.getElementById("mainForm").addEventListener("submit", function(event) {
    event.preventDefault();

let num = document.getElementById("num").value;
let numint = parseInt(num);

if (num <=0) {
    document.querySelector("#target").innerHTML =
    "Invalid value.";
} else if (num > 0) {
let sqr = Math.sqrt(numint)
document.querySelector("#target").innerHTML =
    "Square root of " + num +" is " + sqr + "";
}
});