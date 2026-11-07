"use strict";
let numberList = [];
function submitNum(event) {
    event.preventDefault();
    let numInput = document.getElementById("num");
    let number = parseInt(numInput.value);
    if (isNaN(number)) {
        return;
    }
    
    if (number != 0) {
        numberList.push(number);
        document.getElementById("inputGroup").reset();
    }
    else {
        document.getElementById("inputGroup").style.display = "none";
        numberList.sort(function(a, b) {
            return b - a;
        });
        console.log(numberList);
    }
}