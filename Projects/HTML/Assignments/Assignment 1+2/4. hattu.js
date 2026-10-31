"use strict";
document.getElementById("mainForm").addEventListener("submit", function(event) {
    event.preventDefault();

let name = document.getElementById("name").value;


const Houses = ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"];

const randValue =  Math.random()
let House;
if (randValue >= 0.75) {
    House = Houses[0];
} else if (randValue >= 0.5) {
    House = Houses[1];
} else if (randValue >= 0.25) {      
    House = Houses[2];
} else {
    House = Houses[3];
}


document.querySelector("#target").innerHTML =
    "" + name +", your house is " + House + "";
});