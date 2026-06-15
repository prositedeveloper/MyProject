'use strict';

const buttons = document.querySelectorAll('button');

buttons.forEach(button => {
    button.addEventListener('click', () => {
        alert('Вы нажали на кнопку');
    });
});

