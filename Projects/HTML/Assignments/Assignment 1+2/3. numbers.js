"use strict";
document.getElementById("mainForm").addEventListener("submit", function(event) {
    event.preventDefault();

let num1 = document.getElementById("num1").value;
let num2 = document.getElementById("num2").value;
let num3 = document.getElementById("num3").value;

let num1int = parseInt(num1);
let num2int = parseInt(num2);
let num3int = parseInt(num3);

let sum = num1int + num2int + num3int;
let prod = num1int * num2int * num3int;
let average = sum / 3;
document.querySelector("#target").innerHTML =
    "Sum: " + sum +", Product: " + prod +", Average: " + average + "";
    });