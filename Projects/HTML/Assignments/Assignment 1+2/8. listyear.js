"use strict";
document.getElementById("mainForm").addEventListener("submit", function(event) {
    event.preventDefault();

let year1 = document.getElementById("year1").value;
let year1int = parseInt(year1);
let year2 = document.getElementById("year2").value;
let year2int = parseInt(year2);
const container = document.getElementById("target");

let htmlContent = "<ul>";
for (let year = year1int; year <= year2int; year++) {
    if ((year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0)) {
        htmlContent += `<li>${year}</li>`;
    }
}
htmlContent += "</ul>";


container.innerHTML = htmlContent;
})