"use strict";
let ballotData = [];

        function generateFields() {
            const num = parseInt(document.getElementById('numNames').value);
            const container = document.getElementById('nameFieldsContainer');
            const form = document.getElementById('votingForm');
            
            container.innerHTML = ''; 
            document.getElementById('output').style.display = 'none'; 

            if (isNaN(num) || num < 1) {
                alert('Please enter a valid number of names.');
                return;
            }

            for (let i = 1; i <= num; i++) {
                const div = document.createElement('div');
                div.className = 'input-group';

                const label = document.createElement('label');
                label.innerText = `Name #${i}:`;
                label.setAttribute('for', `name_${i}`);

                const input = document.createElement('input');
                input.type = 'text';
                input.id = `name_${i}`;
                input.className = 'candidate-input';
                input.required = true;
                input.placeholder = `Enter name`;

                div.appendChild(label);
                div.appendChild(input);
                container.appendChild(div);
            }

            form.style.display = 'block';
        }

        function storeNames(event) {
            event.preventDefault();
            
            ballotData = []; 
            const inputs = document.querySelectorAll('.candidate-input');

            inputs.forEach(input => {
                ballotData.push({
                    name: input.value.trim(),
                    votes: 0
                });
            });
        }