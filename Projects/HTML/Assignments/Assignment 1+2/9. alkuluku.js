"use strict";
document.getElementById("mainForm").addEventListener("submit", function(event) {
    event.preventDefault();

let num = document.getElementById("num").value;

let numint = parseInt(num);

function prime(numint) {
if (numint <= 1) {
    return false;
}
for (
    let i = 2;
    i <= Math.sqrt(numint); i++
) {
    if (numint % i === 0) {
        return false;
    }
}
return true;
}

let result = prime(numint);
if (result) {
document.querySelector("#target").innerHTML =
    "" + num + " is a prime number";
} else {
document.querySelector("#target").innerHTML =
    "" + num + " is not a prime number";
}
    });