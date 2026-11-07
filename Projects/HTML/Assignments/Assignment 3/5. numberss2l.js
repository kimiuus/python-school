"use strict";
let numberList = [];
function submitNum(event) {
    event.preventDefault();
    let numInput = document.getElementById("num");
    let number = parseInt(numInput.value);
    if (isNaN(number)) {
        return;
    }
    
    if (numberList.includes(number)) {
        alert("Duplicate number");
        document.getElementById("inputGroup").style.display = "none";
        numberList.sort(function(a, b) {
            return a - b;
        });
        console.log(numberList);
    }
    else {
        numberList.push(number);
        document.getElementById("inputGroup").reset();
    }
}