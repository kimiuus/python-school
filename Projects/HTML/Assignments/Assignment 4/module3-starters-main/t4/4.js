'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];

const select = document.querySelector("#target");

for (let i = 0; i < students.length; i++) {
    const opt = document.createElement("option");
    opt.value = students[i].id
    opt.innerHTML = `${students[i].name}`;
    select.appendChild(opt);
}