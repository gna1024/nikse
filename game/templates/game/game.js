document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('form').onsubmit = function(){
        const name = document.querySelector('#name').value;
        alert(`Hi, ${name}. You find my secret game. If you pass all levels I will give you a surprise`)
    }
})