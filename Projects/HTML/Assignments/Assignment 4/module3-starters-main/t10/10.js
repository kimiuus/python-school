"use strict";
document.getElementById("source").addEventListener("submit", function(event) {
    event.preventDefault();

let firstname = document.getElementsByName("firstname")[0].value;
let lastname = document.getElementsByName("lastname")[0].value;


document.querySelector("#target").innerHTML =
    `Your name is ${firstname} ${lastname}`
});