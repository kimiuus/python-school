"use strict";
document.getElementById("mainForm").addEventListener("submit", function(event) {
    event.preventDefault();

let year = document.getElementById("year").value;
let yearint = parseInt(year);

let status;
if (yearint % 100 === 0) {
    if (yearint % 400 === 0)
        status = "is";
    else
        status = "is not";
} else if (yearint % 4 === 0) {
        status = "is";
} else {
    status = "is not";
}

document.querySelector("#target").innerHTML =
    "" + year +" " + status + " a leap year";
});