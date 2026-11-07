"use strict";
let nameList = [];
const container = document.getElementById("target");
let htmlContent
function storeNames(event) {
    document.getElementsByClassName("dog")
    event.preventDefault();
    nameList = [];

    const inputs = document.querySelectorAll('.dog');

    inputs.forEach(input => {
        nameList.push({
            name: input.value.trim(),
        });
    })
    nameList.sort((a, b) => -1 * a.name.localeCompare(b.name))
    console.log(nameList);
htmlContent = "<ul>";
for (let i = 0; i < nameList.length; i++) {
        htmlContent += `<li>${nameList[i].name}</li>`;
    }
htmlContent += "</ul>";
container.innerHTML = htmlContent;
}