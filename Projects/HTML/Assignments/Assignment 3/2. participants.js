"use strict";
// Visual bullshit starts here, ignore for assignment
function generateFields() {
    const num = parseInt(document.getElementById('numNames').value);
    const container = document.getElementById('nameFields');
    const form = document.getElementById('namesList');
            
    container.innerHTML = ''; 
    document.getElementById('output').style.display = 'none'; 

    for (let i = 1; i <= num; i++) {
        const div = document.createElement('div');
        div.className = 'input-group';

        const label = document.createElement('label');
        label.innerText = `Name #${i}:`;
        label.setAttribute('for', `name_${i}`);

        const input = document.createElement('input');
        input.type = 'text';
        input.id = `name_${i}`;
        input.className = 'name-input';

        div.appendChild(label);
        div.appendChild(input);
        container.appendChild(div);
    }

    form.style.display = 'block';
}
// Visual bullshit ends here, actual assignment code below
let nameList = [];
const container = document.getElementById("target");
let htmlContent
function storeNames(event) {
    event.preventDefault();
    nameList = [];

    const inputs = document.querySelectorAll('.name-input');

    inputs.forEach(input => {
        nameList.push({
            name: input.value.trim(),
        });
    })
    nameList.sort((a, b) => a.name.localeCompare(b.name))
    console.log(nameList);
htmlContent = "<ol>";
for (let i = 0; i < nameList.length; i++) {
        htmlContent += `<li>${nameList[i].name}</li>`;
    }
htmlContent += "</ol>";
container.innerHTML = htmlContent;
}