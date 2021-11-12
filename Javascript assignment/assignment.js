const button1 = document.getElementById('btn1');
const button2 = document.getElementById('btn2');
const number = document.getElementById('number');

let count = 0;

button1.onclick = function() {
    count +=1;
    number.innerHTML = "Number: " + count;
};

button2.onclick = function() {
    count -=1;
    number.innerHTML = "Number: " + count;
}