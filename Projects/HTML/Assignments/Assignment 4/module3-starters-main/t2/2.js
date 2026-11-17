const div = document.querySelector("#target");

const li1 = document.createElement("li");
li1.innerHTML = `First item`;
const li2 = document.createElement("li");
li2.innerHTML = `Second item`;
const li3 = document.createElement("li");
li3.innerHTML = `Third item`;

div.appendChild(li1);
div.appendChild(li2);
div.appendChild(li3);

const second = document.querySelectorAll("li")[1].className = "my-item"